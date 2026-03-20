#!/usr/bin/env python3
"""
merge_full_report.py — Consolidated Marketing Report Generator
Converts all Markdown analysis files to a single professional PDF.

Pipeline:
1. Generate cover PDF with scores/gauges (via existing generate_pdf_report.py)
2. Convert all .md files to styled HTML
3. Render HTML to PDF via Chrome headless
4. Merge cover + detail PDFs into one final document

Requirements: reportlab, pypdf, Chrome browser
Usage: python merge_full_report.py <report_dir> [output.pdf]
  <report_dir>  = folder containing .md files (e.g. ./marketing-output/onpulse.fr/)
  [output.pdf]  = optional output filename (default: RAPPORT-COMPLET-<domain>.pdf)
"""

import sys
import os
import re
import subprocess
import tempfile
import json
import glob
from datetime import datetime
from pathlib import Path

try:
    from pypdf import PdfWriter, PdfReader
except ImportError:
    print("Erreur: pypdf requis. Installer avec: pip install pypdf")
    sys.exit(1)


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
CHROME_PATHS = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"),
    "/usr/bin/google-chrome",
    "/usr/bin/chromium-browser",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
]

# Order of sections in the final report, organized by phase
# Tuples: (filename, title) for sections, or (None, phase_name) for phase headers
SECTION_ORDER = [
    # Phase 1 — Diagnostic
    (None,                    "Phase 1 — Diagnostic"),
    ("MARKETING-AUDIT.md",    "Audit Marketing Complet"),
    ("QUICK-AUDIT.md",        "Évaluation Flash"),
    ("SEO-AUDIT.md",          "Audit SEO — Visibilité Google"),
    ("GEO-AUDIT.md",          "Audit GEO — Visibilité IA"),
    ("BRAND-VOICE.md",        "Voix de Marque"),
    # Phase 2 — Stratégie
    (None,                    "Phase 2 — Stratégie"),
    ("COMPETITOR-REPORT.md",  "Analyse Concurrentielle"),
    ("FUNNEL-ANALYSIS.md",    "Analyse du Tunnel de Vente"),
    ("LANDING-CRO.md",        "Optimisation Landing Page"),
    # Phase 3 — Production
    (None,                    "Phase 3 — Production"),
    ("COPY-SUGGESTIONS.md",   "Suggestions Copywriting"),
    ("EMAIL-SEQUENCES.md",    "Séquences Email"),
    ("SOCIAL-CALENDAR.md",    "Calendrier Social Media"),
    ("AD-CAMPAIGNS.md",       "Campagnes Publicitaires"),
    # Phase 4 — Livrables
    (None,                    "Phase 4 — Livrables"),
    ("LAUNCH-PLAYBOOK.md",    "Plan de Lancement"),
    ("CLIENT-PROPOSAL.md",    "Proposition Commerciale"),
    ("MARKETING-REPORT.md",   "Rapport Marketing Détaillé"),
]

COLORS = {
    "primary":    "#1B2A4A",
    "accent":     "#2D5BFF",
    "highlight":  "#FF6B35",
    "success":    "#00C853",
    "warning":    "#FFB300",
    "danger":     "#FF1744",
    "light_bg":   "#F5F7FA",
    "text":       "#2C3E50",
    "text_light": "#7F8C9B",
    "border":     "#E0E6ED",
    "white":      "#FFFFFF",
}


# ---------------------------------------------------------------------------
# Find Chrome
# ---------------------------------------------------------------------------
def find_chrome():
    for path in CHROME_PATHS:
        if os.path.isfile(path):
            return path
    print("Erreur: Chrome non trouvé. Vérifiez l'installation.")
    sys.exit(1)


# ---------------------------------------------------------------------------
# Markdown to HTML conversion
# ---------------------------------------------------------------------------
def md_to_html(md_text):
    """Convert Markdown to HTML with basic formatting support."""
    lines = md_text.split('\n')
    html_lines = []
    in_table = False
    in_list = False
    in_code = False
    table_rows = []
    
    for line in lines:
        stripped = line.strip()
        
        # Code blocks
        if stripped.startswith('```'):
            if in_code:
                html_lines.append('</code></pre>')
                in_code = False
            else:
                lang = stripped[3:].strip()
                html_lines.append(f'<pre class="code-block"><code>')
                in_code = True
            continue
        
        if in_code:
            html_lines.append(escape_html(line))
            continue
        
        # Empty line
        if not stripped:
            if in_table:
                html_lines.append(render_table(table_rows))
                table_rows = []
                in_table = False
            if in_list:
                tag = 'ul' if in_list == 'ul' else 'ol'
                html_lines.append(f'</{tag}>')
                in_list = False
            html_lines.append('')
            continue
        
        # Table rows
        if '|' in stripped and stripped.startswith('|'):
            # Skip separator rows
            if re.match(r'^\|[\s\-:|]+\|$', stripped):
                in_table = True
                continue
            cells = [c.strip() for c in stripped.split('|')[1:-1]]
            if not in_table:
                in_table = True
                table_rows.append(('header', cells))
            else:
                table_rows.append(('row', cells))
            continue
        
        # Close table if we were in one
        if in_table:
            html_lines.append(render_table(table_rows))
            table_rows = []
            in_table = False
        
        # Headers
        if stripped.startswith('######'):
            html_lines.append(f'<h6>{format_inline(stripped[6:].strip())}</h6>')
            continue
        if stripped.startswith('#####'):
            html_lines.append(f'<h5>{format_inline(stripped[5:].strip())}</h5>')
            continue
        if stripped.startswith('####'):
            html_lines.append(f'<h4>{format_inline(stripped[4:].strip())}</h4>')
            continue
        if stripped.startswith('###'):
            html_lines.append(f'<h3>{format_inline(stripped[3:].strip())}</h3>')
            continue
        if stripped.startswith('##'):
            html_lines.append(f'<h2>{format_inline(stripped[2:].strip())}</h2>')
            continue
        if stripped.startswith('#'):
            html_lines.append(f'<h1>{format_inline(stripped[1:].strip())}</h1>')
            continue
        
        # Horizontal rule
        if re.match(r'^[-*_]{3,}$', stripped):
            html_lines.append('<hr>')
            continue
        
        # Unordered list
        if re.match(r'^[-*+]\s', stripped):
            if not in_list:
                html_lines.append('<ul>')
                in_list = 'ul'
            elif in_list == 'ol':
                # Close previous ordered list, open unordered
                html_lines.append('</ol>')
                html_lines.append('<ul>')
                in_list = 'ul'
            content = re.sub(r'^[-*+]\s', '', stripped)
            html_lines.append(f'<li>{format_inline(content)}</li>')
            continue
        
        # Ordered list
        if re.match(r'^\d+\.\s', stripped):
            if not in_list:
                html_lines.append('<ol>')
                in_list = 'ol'
            elif in_list == 'ul':
                # Close previous unordered list, open ordered
                html_lines.append('</ul>')
                html_lines.append('<ol>')
                in_list = 'ol'
            content = re.sub(r'^\d+\.\s', '', stripped)
            html_lines.append(f'<li>{format_inline(content)}</li>')
            continue
        
        # Close list if we hit any non-list content
        if in_list:
            tag = 'ul' if in_list == 'ul' else 'ol'
            html_lines.append(f'</{tag}>')
            in_list = False
        
        # Blockquote
        if stripped.startswith('>'):
            content = stripped[1:].strip()
            html_lines.append(f'<blockquote>{format_inline(content)}</blockquote>')
            continue
        
        # Regular paragraph
        html_lines.append(f'<p>{format_inline(stripped)}</p>')
    
    # Close any open elements
    if in_table:
        html_lines.append(render_table(table_rows))
    if in_list:
        tag = 'ul' if in_list == 'ul' else 'ol'
        html_lines.append(f'</{tag}>')
    if in_code:
        html_lines.append('</code></pre>')
    
    return '\n'.join(html_lines)


def escape_html(text):
    """Escape HTML special characters."""
    return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def format_inline(text):
    """Apply inline Markdown formatting."""
    # Bold + italic
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', text)
    # Bold
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # Italic
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    # Inline code
    text = re.sub(r'`(.+?)`', r'<code class="inline-code">\1</code>', text)
    # Links
    text = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', text)
    # Strikethrough
    text = re.sub(r'~~(.+?)~~', r'<del>\1</del>', text)
    return text


def render_table(rows):
    """Render table rows as HTML with intelligent column widths."""
    if not rows:
        return ''
    
    # Determine number of columns
    num_cols = max(len(cells) for _, cells in rows)
    
    # Calculate average content length per column to detect "heavy" columns
    col_lengths = [0] * num_cols
    col_counts = [0] * num_cols
    for _, cells in rows:
        for j, cell in enumerate(cells):
            if j < num_cols:
                col_lengths[j] += len(cell)
                col_counts[j] += 1
    
    avg_lengths = [col_lengths[j] / max(col_counts[j], 1) for j in range(num_cols)]
    total_avg = sum(avg_lengths) or 1
    
    # Compute proportional widths based on content
    if num_cols == 2:
        # 2 columns: label / description
        widths = [35, 65]
    elif num_cols == 3:
        # 3 columns: label / status / description
        # Give more space to the column with most content
        raw = [avg_lengths[j] / total_avg * 100 for j in range(num_cols)]
        widths = [max(w, 15) for w in raw]  # minimum 15%
        # Normalize
        total_w = sum(widths)
        widths = [w / total_w * 100 for w in widths]
    elif num_cols == 4:
        # 4 columns: common in audit tables
        raw = [avg_lengths[j] / total_avg * 100 for j in range(num_cols)]
        widths = [max(w, 12) for w in raw]  # minimum 12%
        total_w = sum(widths)
        widths = [w / total_w * 100 for w in widths]
    else:
        # 5+ columns: proportional with minimum
        raw = [avg_lengths[j] / total_avg * 100 for j in range(num_cols)]
        widths = [max(w, 10) for w in raw]  # minimum 10%
        total_w = sum(widths)
        widths = [w / total_w * 100 for w in widths]
    
    # Build colgroup for explicit widths
    html = '<div class="table-wrapper"><table>'
    html += '<colgroup>'
    for w in widths:
        html += f'<col style="width:{w:.1f}%">'
    html += '</colgroup>'
    
    for i, (row_type, cells) in enumerate(rows):
        if i == 0 and row_type == 'header':
            html += '<thead><tr>'
            for cell in cells:
                html += f'<th>{format_inline(cell)}</th>'
            html += '</tr></thead><tbody>'
        else:
            row_class = 'even' if i % 2 == 0 else 'odd'
            html += f'<tr class="{row_class}">'
            for cell in cells:
                html += f'<td>{format_inline(cell)}</td>'
            html += '</tr>'
    
    html += '</tbody></table></div>'
    return html


# ---------------------------------------------------------------------------
# HTML template with professional CSS
# ---------------------------------------------------------------------------
def build_html_document(body_html, title, brand_name="", section_number=0):
    """Wrap HTML body in a complete styled document."""
    
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>
  @page {{
    size: A4;
    margin: 15mm 0 20mm 0;
  }}

  @page:first {{
    margin-top: 0;
  }}

  * {{ margin: 0; padding: 0; box-sizing: border-box; }}

  body {{
    font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif;
    font-size: 11pt;
    line-height: 1.6;
    color: {COLORS['text']};
    background: {COLORS['white']};
    margin: 0;
    padding: 0;
  }}

  .content {{
    padding: 0 18mm;
  }}

  /* --- Section cover --- */
  .section-cover {{
    background: linear-gradient(135deg, {COLORS['primary']} 0%, #2a4070 100%);
    color: white;
    padding: 35px 18mm;
    margin: 0 0 25px 0;
    page-break-after: avoid;
  }}

  .section-cover h1 {{
    font-size: 26pt;
    font-weight: 800;
    margin: 0 0 8px 0;
    letter-spacing: -0.5px;
  }}

  .section-cover .section-number {{
    font-size: 13pt;
    font-weight: 300;
    opacity: 0.7;
    text-transform: uppercase;
    letter-spacing: 3px;
    margin-bottom: 5px;
  }}

  .section-cover .brand {{
    font-size: 12pt;
    opacity: 0.6;
    margin-top: 10px;
  }}

  /* --- Headings --- */
  h1 {{
    font-size: 22pt;
    font-weight: 800;
    color: {COLORS['primary']};
    margin: 35px 0 15px 0;
    padding-bottom: 8px;
    border-bottom: 3px solid {COLORS['accent']};
  }}

  h2 {{
    font-size: 16pt;
    font-weight: 700;
    color: {COLORS['primary']};
    margin: 28px 0 12px 0;
    padding-bottom: 5px;
    border-bottom: 2px solid {COLORS['border']};
  }}

  h3 {{
    font-size: 13pt;
    font-weight: 700;
    color: {COLORS['accent']};
    margin: 22px 0 10px 0;
  }}

  h4 {{
    font-size: 11.5pt;
    font-weight: 700;
    color: {COLORS['text']};
    margin: 18px 0 8px 0;
  }}

  h5, h6 {{
    font-size: 11pt;
    font-weight: 600;
    color: {COLORS['text_light']};
    margin: 14px 0 6px 0;
  }}

  /* --- Text --- */
  p {{
    margin: 8px 0;
    text-align: justify;
  }}

  strong {{
    color: {COLORS['primary']};
    font-weight: 700;
  }}

  em {{
    font-style: italic;
    color: {COLORS['text']};
  }}

  a {{
    color: {COLORS['accent']};
    text-decoration: none;
  }}

  blockquote {{
    border-left: 4px solid {COLORS['highlight']};
    padding: 12px 18px;
    margin: 15px 0;
    background: {COLORS['light_bg']};
    border-radius: 0 6px 6px 0;
    font-style: italic;
    color: {COLORS['text_light']};
  }}

  hr {{
    border: none;
    border-top: 2px solid {COLORS['border']};
    margin: 25px 0;
  }}

  /* --- Lists --- */
  ul, ol {{
    margin: 8px 0 8px 20px;
    padding-left: 0;
  }}

  /* Empêcher l'indentation croissante des listes imbriquées */
  ul ul, ol ol, ul ol, ol ul {{
    margin-left: 15px;
    margin-top: 4px;
    margin-bottom: 4px;
  }}

  ul ul ul, ol ol ol {{
    margin-left: 10px;
  }}

  li {{
    margin: 4px 0;
    padding-left: 3px;
  }}

  li::marker {{
    color: {COLORS['accent']};
    font-weight: 700;
  }}

  /* --- Tables --- */
  .table-wrapper {{
    margin: 15px 0;
    overflow-x: auto;
    page-break-inside: auto;
  }}

  table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 9.5pt;
    border-radius: 6px;
    overflow: hidden;
    box-shadow: 0 1px 4px rgba(0,0,0,0.06);
    table-layout: fixed;
    word-wrap: break-word;
    overflow-wrap: break-word;
  }}

  thead {{
    background: {COLORS['primary']};
    color: white;
  }}

  th {{
    padding: 8px 10px;
    text-align: left;
    font-weight: 600;
    font-size: 8.5pt;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    word-wrap: break-word;
    overflow-wrap: break-word;
  }}

  td {{
    padding: 7px 10px;
    border-bottom: 1px solid {COLORS['border']};
    word-wrap: break-word;
    overflow-wrap: break-word;
    vertical-align: top;
    font-size: 9pt;
    line-height: 1.4;
  }}

  tr {{
    page-break-inside: avoid;
  }}

  tr.even {{
    background: {COLORS['light_bg']};
  }}

  tr.odd {{
    background: {COLORS['white']};
  }}

  tbody tr:hover {{
    background: #e8ecf4;
  }}

  /* --- Code --- */
  .inline-code {{
    background: {COLORS['light_bg']};
    padding: 2px 6px;
    border-radius: 4px;
    font-family: 'Cascadia Code', 'Fira Code', 'Consolas', monospace;
    font-size: 9.5pt;
    color: {COLORS['highlight']};
  }}

  .code-block {{
    background: {COLORS['primary']};
    color: #e2e8f0;
    padding: 16px 20px;
    border-radius: 8px;
    font-family: 'Cascadia Code', 'Fira Code', 'Consolas', monospace;
    font-size: 9pt;
    line-height: 1.5;
    overflow-x: auto;
    margin: 15px 0;
  }}

  /* --- Footer --- */
  .page-footer {{
    margin-top: 30px;
    padding: 10px 0;
    font-size: 8pt;
    color: {COLORS['text_light']};
    border-top: 1px solid {COLORS['border']};
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}

  .page-footer .confidential {{
    color: {COLORS['danger']};
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
    font-size: 7.5pt;
  }}

  /* --- Print --- */
  @media print {{
    body {{ -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
    .section-cover {{ -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
    thead {{ -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
  }}
</style>
</head>
<body>

<div class="section-cover">
  <div class="section-number">Section {section_number:02d}</div>
  <h1 style="border:none; color:white; margin:0; padding:0; font-size:26pt;">{title}</h1>
  <div class="brand">{brand_name} — AI Marketing Suite</div>
</div>

<div class="content">
{body_html}

<div class="page-footer">
  <span class="confidential">Confidentiel</span>
  <span>{brand_name} — {datetime.now().strftime('%d/%m/%Y')}</span>
  <span>AI Marketing Suite</span>
</div>
</div>

</body>
</html>"""


# ---------------------------------------------------------------------------
# HTML to PDF via Chrome headless
# ---------------------------------------------------------------------------
def html_to_pdf(html_content, output_pdf, chrome_path):
    """Convert HTML string to PDF using Chrome headless."""
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False, encoding='utf-8') as f:
        f.write(html_content)
        html_path = f.name
    
    try:
        cmd = [
            chrome_path,
            '--headless=new',
            '--disable-gpu',
            '--no-sandbox',
            '--disable-software-rasterizer',
            f'--print-to-pdf={output_pdf}',
            '--print-to-pdf-no-header',
            '--no-pdf-header-footer',
            f'file:///{html_path.replace(os.sep, "/")}'
        ]
        
        result = subprocess.run(cmd, capture_output=True, timeout=60)
        
        if not os.path.exists(output_pdf):
            print(f"  ERREUR: Chrome n'a pas généré {output_pdf}")
            if result.stderr:
                print(f"  Chrome stderr: {result.stderr.decode('utf-8', errors='ignore')[:200]}")
            return False
        
        return True
    
    except subprocess.TimeoutExpired:
        print(f"  ERREUR: Timeout Chrome pour {output_pdf}")
        return False
    except Exception as e:
        print(f"  ERREUR: {e}")
        return False
    finally:
        try:
            os.unlink(html_path)
        except:
            pass


# ---------------------------------------------------------------------------
# Merge PDFs
# ---------------------------------------------------------------------------
def merge_pdfs(pdf_files, output_path, brand_name="", section_map=None):
    """Merge multiple PDF files into one and add global page numbers with section names.
    
    section_map: list of (pdf_path, section_number, section_name) tuples.
    """
    # Remove existing output file if it exists
    if os.path.exists(output_path):
        try:
            os.unlink(output_path)
        except PermissionError:
            print(f"  ERREUR: Le fichier '{output_path}' est ouvert dans un autre programme.")
            print(f"  Fermez le PDF et relancez le script.")
            sys.exit(1)
    
    writer = PdfWriter()
    
    # Build page-to-section mapping
    page_sections = []  # list of (section_number, section_name) for each page
    
    for pdf_file in pdf_files:
        if os.path.exists(pdf_file) and os.path.getsize(pdf_file) > 0:
            try:
                reader = PdfReader(pdf_file)
                # Find section info for this file
                sec_num = 0
                sec_name = ""
                if section_map:
                    for entry in section_map:
                        path, num, name = entry
                        if os.path.normpath(path) == os.path.normpath(pdf_file):
                            sec_num = num
                            sec_name = name
                            break
                
                for page in reader.pages:
                    writer.add_page(page)
                    page_sections.append((sec_num, sec_name))
            except Exception as e:
                print(f"  Avertissement: impossible de lire {pdf_file}: {e}")
    
    # Write intermediate file
    temp_merged = output_path + ".tmp"
    with open(temp_merged, "wb") as output:
        writer.write(output)
    
    # Add global page numbers + section names using ReportLab overlay
    try:
        from reportlab.pdfgen import canvas as rl_canvas
        from reportlab.lib.colors import HexColor
        
        reader = PdfReader(temp_merged)
        final_writer = PdfWriter()
        total_pages = len(reader.pages)
        
        for i, page in enumerate(reader.pages):
            page_num = i + 1
            sec_num, section_name = page_sections[i] if i < len(page_sections) else (0, "")
            
            # Skip cover page (page 1) — it has its own footer
            if i == 0 and section_name == "" and sec_num == 0:
                final_writer.add_page(page)
                continue
            
            # Get page dimensions
            media_box = page.mediabox
            page_width = float(media_box.width)
            page_height = float(media_box.height)
            
            # Create overlay with page number
            overlay_path = output_path + f".overlay_{i}.pdf"
            c = rl_canvas.Canvas(overlay_path, pagesize=(page_width, page_height))
            
            # Footer line
            c.setStrokeColor(HexColor("#E0E6ED"))
            c.setLineWidth(0.5)
            c.line(50, 32, page_width - 50, 32)
            
            # Section number + name (left)
            if section_name:
                c.setFont("Helvetica-Bold", 6.5)
                c.setFillColor(HexColor("#1B2A4A"))
                if sec_num > 0:
                    section_label = f"Section {sec_num:02d} — {section_name}"
                else:
                    section_label = section_name
                c.drawString(50, 20, section_label)
            
            # "Confidentiel" + brand (center)
            c.setFont("Helvetica", 6.5)
            c.setFillColor(HexColor("#7F8C9B"))
            center_text = f"CONFIDENTIEL — {brand_name}"
            c.drawCentredString(page_width / 2, 20, center_text)
            
            # Page number (right)
            c.setFont("Helvetica-Bold", 7.5)
            c.setFillColor(HexColor("#2C3E50"))
            c.drawRightString(page_width - 50, 20, f"{page_num} / {total_pages}")
            
            c.save()
            
            # Merge overlay onto page
            overlay_reader = PdfReader(overlay_path)
            page.merge_page(overlay_reader.pages[0])
            final_writer.add_page(page)
            
            # Cleanup overlay
            try:
                os.unlink(overlay_path)
            except:
                pass
        
        with open(output_path, "wb") as output:
            final_writer.write(output)
        
        # Cleanup temp
        try:
            os.unlink(temp_merged)
        except:
            pass
            
    except Exception as e:
        print(f"  Avertissement: numérotation globale impossible ({e}), utilisation du PDF sans numérotation")
        import shutil
        if os.path.exists(output_path):
            try:
                os.unlink(output_path)
            except:
                pass
        try:
            shutil.copy2(temp_merged, output_path)
        except Exception as e2:
            print(f"  ERREUR fallback: {e2}")
        try:
            os.unlink(temp_merged)
        except:
            pass
    
    return output_path


# ---------------------------------------------------------------------------
# Generate Cover Page HTML
# ---------------------------------------------------------------------------
def build_cover_page_html(brand_name, url=""):
    """Build a premium cover page."""
    
    date_str = datetime.now().strftime('%d %B %Y')
    # French month names
    months_fr = {
        'January': 'janvier', 'February': 'février', 'March': 'mars',
        'April': 'avril', 'May': 'mai', 'June': 'juin',
        'July': 'juillet', 'August': 'août', 'September': 'septembre',
        'October': 'octobre', 'November': 'novembre', 'December': 'décembre'
    }
    for en, fr in months_fr.items():
        date_str = date_str.replace(en, fr)
    
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>Page de garde</title>
<style>
  @page {{
    size: A4;
    margin: 0;
  }}
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
    font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif;
    background: {COLORS['white']};
    width: 210mm;
    height: 297mm;
    position: relative;
    overflow: hidden;
  }}
  @media print {{
    body {{ -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
  }}

  .cover {{
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    position: relative;
  }}

  /* Top bar */
  .top-bar {{
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 8px;
    background: linear-gradient(90deg, {COLORS['accent']} 0%, {COLORS['highlight']} 100%);
  }}

  /* Decorative side stripe */
  .side-stripe {{
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    width: 12mm;
    background: linear-gradient(180deg, {COLORS['primary']} 0%, #2a4070 100%);
  }}

  /* Main content */
  .cover-content {{
    text-align: center;
    padding: 0 25mm 0 30mm;
    max-width: 85%;
  }}

  .cover-label {{
    font-size: 11pt;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 5px;
    color: {COLORS['accent']};
    margin-bottom: 25px;
  }}

  .cover-title {{
    font-size: 36pt;
    font-weight: 800;
    color: {COLORS['primary']};
    line-height: 1.15;
    margin-bottom: 20px;
    letter-spacing: -1px;
  }}

  .cover-subtitle {{
    font-size: 14pt;
    font-weight: 400;
    color: {COLORS['text_light']};
    margin-bottom: 40px;
    line-height: 1.5;
  }}

  .cover-brand {{
    display: inline-block;
    background: linear-gradient(135deg, {COLORS['primary']} 0%, #2a4070 100%);
    color: white;
    font-size: 20pt;
    font-weight: 700;
    padding: 18px 45px;
    border-radius: 8px;
    letter-spacing: 0.5px;
    margin-bottom: 30px;
  }}

  .cover-url {{
    font-size: 12pt;
    color: {COLORS['accent']};
    font-weight: 500;
    margin-bottom: 50px;
  }}

  .cover-divider {{
    width: 80px;
    height: 3px;
    background: {COLORS['highlight']};
    margin: 0 auto 35px auto;
    border-radius: 2px;
  }}

  .cover-meta {{
    font-size: 10pt;
    color: {COLORS['text_light']};
    line-height: 2;
  }}

  .cover-meta strong {{
    color: {COLORS['text']};
  }}

  /* Bottom bar */
  .bottom-section {{
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    padding: 20px 25mm;
    background: {COLORS['light_bg']};
    border-top: 1px solid {COLORS['border']};
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}

  .bottom-section .powered {{
    font-size: 8.5pt;
    color: {COLORS['text_light']};
  }}

  .bottom-section .confidential {{
    font-size: 8pt;
    color: {COLORS['danger']};
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 2px;
  }}
</style>
</head>
<body>
<div class="cover">
  <div class="top-bar"></div>
  <div class="side-stripe"></div>
  
  <div class="cover-content">
    <div class="cover-label">Analyse Marketing Digitale</div>
    <div class="cover-title">Audit Marketing<br>Complet & Stratégie</div>
    <div class="cover-subtitle">Diagnostic, recommandations actionnables<br>et plan de croissance priorisé</div>
    
    <div class="cover-brand">{brand_name}</div>
    <div class="cover-url">{url}</div>
    
    <div class="cover-divider"></div>
    
    <div class="cover-meta">
      <strong>Date :</strong> {date_str}<br>
      <strong>Réalisé par :</strong> AI Marketing Suite<br>
      <strong>Classification :</strong> Confidentiel
    </div>
  </div>

  <div class="bottom-section">
    <span class="powered">Propulsé par AI Marketing Suite pour Claude Code</span>
    <span class="confidential">Document confidentiel</span>
  </div>
</div>
</body>
</html>"""


# ---------------------------------------------------------------------------
# Generate Table of Contents HTML
# ---------------------------------------------------------------------------
def build_toc_html(sections, brand_name):
    """Build a Table of Contents page organized by phase."""
    
    # Map sections to their phase
    phases = []
    current_phase = None
    section_num = 0
    
    for filename, title in SECTION_ORDER:
        if filename is None:
            # Phase header
            current_phase = {"name": title, "sections": []}
            phases.append(current_phase)
            continue
        # Check if this section exists in available sections
        found = False
        for fn, sec_title in sections:
            if fn == filename:
                found = True
                section_num += 1
                if current_phase:
                    current_phase["sections"].append((section_num, sec_title, filename, True))
                break
        if not found and current_phase:
            section_num += 1
            current_phase["sections"].append((section_num, title, filename, False))
    
    # Build HTML
    toc_body = ""
    for phase in phases:
        if not any(s[3] for s in phase["sections"]):
            continue  # Skip phases with no available sections
        
        phase_color = COLORS['accent']
        toc_body += f"""
        <tr>
          <td colspan="3" style="
            background: linear-gradient(135deg, {COLORS['primary']} 0%, #2a4070 100%);
            color: white;
            padding: 10px 14px;
            font-weight: 700;
            font-size: 10.5pt;
            letter-spacing: 1px;
            border: none;
          ">{phase['name']}</td>
        </tr>"""
        
        for num, title, filename, available in phase["sections"]:
            if available:
                row_class = 'even' if num % 2 == 0 else 'odd'
                toc_body += f"""
        <tr class="{row_class}">
          <td style="width:40px; text-align:center; font-weight:700; color:{COLORS['accent']};">{num:02d}</td>
          <td style="font-weight:600;">{title}</td>
          <td style="width:180px; color:{COLORS['text_light']}; font-size:9pt;">{filename}</td>
        </tr>"""
            else:
                toc_body += f"""
        <tr style="opacity:0.4;">
          <td style="width:40px; text-align:center; color:{COLORS['text_light']};">{num:02d}</td>
          <td style="color:{COLORS['text_light']}; font-style:italic;">{title} (non généré)</td>
          <td style="width:180px; color:{COLORS['text_light']}; font-size:9pt;">{filename}</td>
        </tr>"""
    
    body = f"""
    <h2 style="margin-top:10px;">Sommaire</h2>
    <p style="color:{COLORS['text_light']}; margin-bottom:25px;">
      Ce rapport compile l'ensemble des analyses marketing réalisées pour <strong>{brand_name}</strong>.
      Les {len([s for s in sections])} sections sont organisées en 4 phases : diagnostic, stratégie, production et livrables.
    </p>
    <div class="table-wrapper">
    <table>
      <thead>
        <tr>
          <th style="width:40px;">N°</th>
          <th>Section</th>
          <th style="width:180px;">Fichier source</th>
        </tr>
      </thead>
      <tbody>
        {toc_body}
      </tbody>
    </table>
    </div>
    
    <div style="margin-top:30px; padding:20px; background:{COLORS['light_bg']}; border-radius:8px; border-left:4px solid {COLORS['accent']};">
      <p style="margin:0; font-size:10pt; color:{COLORS['text_light']};">
        <strong style="color:{COLORS['primary']};">Méthodologie</strong><br>
        Chaque catégorie est évaluée sur 100 points selon les meilleures pratiques du secteur et des benchmarks concurrentiels.
        Le score global est la moyenne pondérée des 6 dimensions principales. L'audit GEO évalue en plus la visibilité dans les réponses des IA génératives (ChatGPT, Gemini, Perplexity, Claude).
        Les recommandations sont priorisées par impact estimé sur le revenu.
      </p>
    </div>
    """
    
    return build_html_document(body, "Table des Matières", brand_name, 0)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    if len(sys.argv) < 2:
        print("Usage: python merge_full_report.py <report_dir> [output.pdf]")
        print("  <report_dir>  = dossier contenant les fichiers .md")
        print("  [output.pdf]  = nom du fichier de sortie (optionnel)")
        sys.exit(1)
    
    report_dir = sys.argv[1]
    
    if not os.path.isdir(report_dir):
        print(f"Erreur: Le dossier '{report_dir}' n'existe pas.")
        sys.exit(1)
    
    # Detect brand name from directory
    brand_name = os.path.basename(os.path.normpath(report_dir))
    
    # Output filename
    if len(sys.argv) > 2:
        output_file = sys.argv[2]
    else:
        safe_name = brand_name.replace('.', '-')
        output_file = os.path.join(report_dir, f"RAPPORT-COMPLET-{safe_name}.pdf")
    
    print(f"")
    print(f"╔══════════════════════════════════════════════════╗")
    print(f"║   Rapport Marketing Consolidé — Génération PDF  ║")
    print(f"╚══════════════════════════════════════════════════╝")
    print(f"")
    print(f"  Dossier : {report_dir}")
    print(f"  Marque  : {brand_name}")
    print(f"  Sortie  : {output_file}")
    print(f"")
    
    # Find Chrome
    chrome = find_chrome()
    print(f"  Chrome  : {chrome}")
    print(f"")
    
    # Find available sections (skip phase headers where filename is None)
    available_sections = []
    total_real_sections = 0
    for filename, title in SECTION_ORDER:
        if filename is None:
            continue  # Phase header, skip
        total_real_sections += 1
        filepath = os.path.join(report_dir, filename)
        if os.path.exists(filepath):
            available_sections.append((filename, title, filepath))
    
    if not available_sections:
        print("Erreur: Aucun fichier .md trouvé dans le dossier.")
        sys.exit(1)
    
    print(f"  Sections trouvées : {len(available_sections)}/{total_real_sections}")
    for fn, title, _ in available_sections:
        print(f"    ✓ {fn}")
    print(f"")
    
    # Create temp directory for intermediate PDFs
    temp_dir = tempfile.mkdtemp(prefix="marketing_report_")
    pdf_parts = []
    section_map = []  # (pdf_path, section_name) for footer
    
    # Detect URL from files
    url = ""
    for fn, _, fp in available_sections:
        try:
            with open(fp, 'r', encoding='utf-8') as f:
                first_lines = f.read(500)
            import re as re_mod
            url_match = re_mod.search(r'https?://[^\s\)]+', first_lines)
            if url_match:
                url = url_match.group(0).rstrip('/')
                break
        except:
            pass
    if not url:
        url = f"https://{brand_name}"
    
    try:
        # --- Step 1: Cover page ---
        print(f"  [1/4] Génération de la page de garde...")
        cover_html = build_cover_page_html(brand_name, url)
        cover_pdf = os.path.join(temp_dir, "00-cover.pdf")
        
        if html_to_pdf(cover_html, cover_pdf, chrome):
            pdf_parts.append(cover_pdf)
            section_map.append((cover_pdf, 0, ""))
            print(f"         ✓ Page de garde générée")
        else:
            print(f"         ✗ Erreur page de garde")
        
        # --- Step 2: Check for existing score cover PDF ---
        cover_candidates = glob.glob(os.path.join(report_dir, "MARKETING-REPORT-*.pdf"))
        cover_candidates = [c for c in cover_candidates if "COMPLET" not in c and "FINAL" not in c]
        
        if cover_candidates:
            cover_score_pdf = cover_candidates[0]
            print(f"  [2/4] Couverture scores : {os.path.basename(cover_score_pdf)}")
            pdf_parts.append(cover_score_pdf)
            section_map.append((cover_score_pdf, 0, "Scores & Synthèse"))
        else:
            print(f"  [2/4] Pas de couverture scores existante")
        
        # --- Step 3: Generate Table of Contents ---
        print(f"  [3/4] Génération du sommaire...")
        toc_sections = [(fn, title) for fn, title, _ in available_sections]
        toc_html = build_toc_html(toc_sections, brand_name)
        toc_pdf = os.path.join(temp_dir, "01-toc.pdf")
        
        if html_to_pdf(toc_html, toc_pdf, chrome):
            pdf_parts.append(toc_pdf)
            section_map.append((toc_pdf, 0, "Table des Matières"))
            print(f"         ✓ Sommaire généré")
        else:
            print(f"         ✗ Erreur sommaire")
        
        # --- Step 4: Convert each section ---
        print(f"  [4/4] Conversion des sections...")
        
        for i, (filename, title, filepath) in enumerate(available_sections, 1):
            print(f"         [{i}/{len(available_sections)}] {title}...", end="", flush=True)
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    md_content = f.read()
                
                # Convert MD to HTML
                body_html = md_to_html(md_content)
                
                # Wrap in styled template
                full_html = build_html_document(body_html, title, brand_name, i)
                
                # Convert to PDF
                section_pdf = os.path.join(temp_dir, f"{i+1:02d}-{filename.replace('.md', '.pdf')}")
                
                if html_to_pdf(full_html, section_pdf, chrome):
                    pdf_parts.append(section_pdf)
                    section_map.append((section_pdf, i, title))
                    size_kb = os.path.getsize(section_pdf) // 1024
                    print(f" ✓ ({size_kb} Ko)")
                else:
                    print(f" ✗ ERREUR")
            
            except Exception as e:
                print(f" ✗ {e}")
        
        # --- Step 5: Merge all PDFs ---
        print(f"")
        print(f"  Fusion de {len(pdf_parts)} PDF...")
        
        if len(pdf_parts) > 0:
            merge_pdfs(pdf_parts, output_file, brand_name, section_map)
            
            if os.path.exists(output_file):
                size_mb = os.path.getsize(output_file) / (1024 * 1024)
                
                # Count pages
                try:
                    reader = PdfReader(output_file)
                    total_pages = len(reader.pages)
                except:
                    total_pages = "?"
                
                print(f"")
                print(f"╔══════════════════════════════════════════════════╗")
                print(f"║              Rapport généré avec succès !        ║")
                print(f"╚══════════════════════════════════════════════════╝")
                print(f"")
                print(f"  Fichier : {output_file}")
                print(f"  Taille  : {size_mb:.1f} Mo")
                print(f"  Pages   : {total_pages}")
                print(f"  Sections: {len(available_sections)}")
                print(f"")
            else:
                print(f"  ERREUR: Le fichier de sortie n'a pas été créé.")
                sys.exit(1)
        else:
            print(f"  ERREUR: Aucun PDF intermédiaire généré.")
            sys.exit(1)
    
    finally:
        # Cleanup temp files
        for f in glob.glob(os.path.join(temp_dir, "*.pdf")):
            try:
                os.unlink(f)
            except:
                pass
        try:
            os.rmdir(temp_dir)
        except:
            pass


if __name__ == "__main__":
    main()
