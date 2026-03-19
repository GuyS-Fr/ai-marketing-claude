#!/usr/bin/env python3
"""
Marketing Report PDF Generator — AI Marketing Claude Code Skills
Generates professional, client-ready PDF marketing reports with charts,
score visualizations, and prioritized action plans.

Requires: reportlab (pip install reportlab)
"""

import sys
import json
import os
from datetime import datetime

try:
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.units import inch, mm
    from reportlab.lib.colors import HexColor, white, black, Color
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
    from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                     TableStyle, PageBreak, KeepTogether, HRFlowable)
    from reportlab.graphics.shapes import (Drawing, Rect, Circle, String, Line,
                                            Wedge, ArcPath, Group, PolyLine)
    from reportlab.graphics import renderPDF
    from reportlab.pdfgen import canvas as pdfcanvas
    from reportlab.platypus.flowables import Flowable
except ImportError:
    print("Error: reportlab is required. Install with: pip install reportlab")
    sys.exit(1)


# ---------------------------------------------------------------------------
# Color palette
# ---------------------------------------------------------------------------
COLORS = {
    "primary":    HexColor("#1B2A4A"),
    "accent":     HexColor("#2D5BFF"),
    "highlight":  HexColor("#FF6B35"),
    "success":    HexColor("#00C853"),
    "warning":    HexColor("#FFB300"),
    "danger":     HexColor("#FF1744"),
    "light_bg":   HexColor("#F5F7FA"),
    "mid_bg":     HexColor("#EDF0F5"),
    "text":       HexColor("#2C3E50"),
    "text_light": HexColor("#7F8C9B"),
    "border":     HexColor("#E0E6ED"),
    "white":      white,
    "black":      black,
}

PAGE_W, PAGE_H = letter   # 612 x 792 pts
MARGIN = 48               # pts
CONTENT_W = PAGE_W - 2 * MARGIN


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def score_color(score):
    if score >= 80:  return COLORS["success"]
    if score >= 60:  return COLORS["accent"]
    if score >= 40:  return COLORS["warning"]
    return COLORS["danger"]


def score_grade(score):
    if score >= 90: return "A+"
    if score >= 80: return "A"
    if score >= 70: return "B"
    if score >= 60: return "C"
    if score >= 50: return "D"
    return "F"


def score_status(score):
    if score >= 75: return "Fort"
    if score >= 60: return "Solide"
    if score >= 45: return "À améliorer"
    return "Critique"


# ---------------------------------------------------------------------------
# Custom Flowables
# ---------------------------------------------------------------------------
class ColorBand(Flowable):
    """Full-width colored horizontal band (used as section header background)."""
    def __init__(self, height=36, color=None, text="", text_color=None, font_size=14):
        super().__init__()
        self.band_height = height
        self.color = color or COLORS["primary"]
        self.text = text
        self.text_color = text_color or COLORS["white"]
        self.font_size = font_size
        self.width = CONTENT_W
        self.height = height

    def draw(self):
        self.canv.setFillColor(self.color)
        self.canv.rect(0, 0, self.width, self.band_height, fill=1, stroke=0)
        if self.text:
            self.canv.setFillColor(self.text_color)
            self.canv.setFont("Helvetica-Bold", self.font_size)
            self.canv.drawString(12, self.band_height / 2 - self.font_size / 3, self.text)


class GaugeFlowable(Flowable):
    """Ring-style score gauge."""
    def __init__(self, score, size=120):
        super().__init__()
        self.score = int(score)
        self.size = size
        self.width = size
        self.height = size

    def draw(self):
        cx = self.size / 2
        cy = self.size / 2
        r_outer = self.size / 2 - 4
        r_inner = r_outer - 18
        color = score_color(self.score)
        bg = COLORS["light_bg"]

        # Background ring
        self.canv.setFillColor(bg)
        self.canv.setStrokeColor(COLORS["border"])
        self.canv.setLineWidth(1)
        self.canv.circle(cx, cy, r_outer, fill=1, stroke=1)
        self.canv.setFillColor(COLORS["white"])
        self.canv.circle(cx, cy, r_inner, fill=1, stroke=0)

        # Score arc (drawn as filled wedge segments)
        angle = 360 * self.score / 100
        start_deg = 90  # top
        # Draw arc band using thin wedges
        import math
        steps = max(1, int(angle))
        for i in range(steps):
            a_start = math.radians(start_deg - i)
            a_end = math.radians(start_deg - i - 1)
            # outer arc point
            ox1 = cx + r_outer * math.cos(a_start)
            oy1 = cy + r_outer * math.sin(a_start)
            ox2 = cx + r_outer * math.cos(a_end)
            oy2 = cy + r_outer * math.sin(a_end)
            ix1 = cx + r_inner * math.cos(a_start)
            iy1 = cy + r_inner * math.sin(a_start)
            ix2 = cx + r_inner * math.cos(a_end)
            iy2 = cy + r_inner * math.sin(a_end)
            p = self.canv.beginPath()
            p.moveTo(ox1, oy1)
            p.lineTo(ox2, oy2)
            p.lineTo(ix2, iy2)
            p.lineTo(ix1, iy1)
            p.close()
            self.canv.setFillColor(color)
            self.canv.setStrokeColor(color)
            self.canv.setLineWidth(0.3)
            self.canv.drawPath(p, fill=1, stroke=1)

        # Center score text
        self.canv.setFillColor(COLORS["primary"])
        self.canv.setFont("Helvetica-Bold", 26)
        self.canv.drawCentredString(cx, cy + 4, str(self.score))
        self.canv.setFont("Helvetica", 9)
        self.canv.setFillColor(COLORS["text_light"])
        self.canv.drawCentredString(cx, cy - 12, "/ 100")


class BarChartFlowable(Flowable):
    """Horizontal bar chart with full labels."""
    def __init__(self, categories, scores, width=None, row_h=24, gap=8):
        super().__init__()
        self.categories = categories
        self.scores = [int(s) for s in scores]
        self.row_h = row_h
        self.gap = gap
        self.label_w = 195   # room for longest label
        self.score_w = 36
        self.bar_w = (width or CONTENT_W) - self.label_w - self.score_w - 8
        self.width = width or CONTENT_W
        self.height = len(categories) * (row_h + gap) + gap

    def draw(self):
        n = len(self.categories)
        for i, (cat, score) in enumerate(zip(self.categories, self.scores)):
            y = self.height - (i + 1) * (self.row_h + self.gap)
            # Label
            self.canv.setFillColor(COLORS["text"])
            self.canv.setFont("Helvetica", 9)
            self.canv.drawString(0, y + self.row_h / 2 - 4, cat)
            # Background bar
            bar_x = self.label_w
            self.canv.setFillColor(COLORS["light_bg"])
            self.canv.roundRect(bar_x, y, self.bar_w, self.row_h, 4, fill=1, stroke=0)
            # Score bar
            fill_w = max(4, (score / 100) * self.bar_w)
            color = score_color(score)
            self.canv.setFillColor(color)
            self.canv.roundRect(bar_x, y, fill_w, self.row_h, 4, fill=1, stroke=0)
            # Score label
            self.canv.setFillColor(COLORS["primary"])
            self.canv.setFont("Helvetica-Bold", 10)
            self.canv.drawString(bar_x + self.bar_w + 6, y + self.row_h / 2 - 4,
                                 f"{score}")


class SeverityBadge(Flowable):
    """Colored pill badge for severity labels."""
    SEV_COLORS = {
        "Critical": HexColor("#FF1744"),
        "High":     HexColor("#FF6B35"),
        "Medium":   HexColor("#FFB300"),
        "Low":      HexColor("#2D5BFF"),
    }

    def __init__(self, severity):
        super().__init__()
        self.severity = severity
        self.width = 58
        self.height = 18

    def draw(self):
        color = self.SEV_COLORS.get(self.severity, COLORS["text_light"])
        self.canv.setFillColor(color)
        self.canv.roundRect(0, 0, self.width, self.height, 5, fill=1, stroke=0)
        self.canv.setFillColor(COLORS["white"])
        self.canv.setFont("Helvetica-Bold", 8)
        self.canv.drawCentredString(self.width / 2, 5, self.severity.upper())


# ---------------------------------------------------------------------------
# Page template with header stripe + page numbers
# ---------------------------------------------------------------------------
class ReportCanvas(pdfcanvas.Canvas):
    def __init__(self, filename, brand_name="", **kwargs):
        super().__init__(filename, **kwargs)
        self._saved_page_states = []
        self.brand_name = brand_name

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self._draw_page_decoration(num_pages)
            super().showPage()
        super().save()

    def _draw_page_decoration(self, total_pages):
        page_num = self._saved_page_states.index(
            {k: v for k, v in self.__dict__.items() if k in self._saved_page_states[0]}
        ) if False else None  # skip index — use _pageNumber instead

        # Top accent stripe
        self.setFillColor(COLORS["primary"])
        self.rect(0, PAGE_H - 6, PAGE_W, 6, fill=1, stroke=0)

        # Bottom bar
        self.setFillColor(COLORS["light_bg"])
        self.rect(0, 0, PAGE_W, 28, fill=1, stroke=0)
        self.setFillColor(COLORS["text_light"])
        self.setFont("Helvetica", 7.5)
        self.drawString(MARGIN, 10, "AI Marketing Suite — Confidential")
        self.drawRightString(PAGE_W - MARGIN, 10, f"{self.brand_name}  ·  Marketing Audit Report")


class NumberedCanvas(pdfcanvas.Canvas):
    """Canvas that adds page numbers and branding on every page."""
    def __init__(self, filename, **kwargs):
        super().__init__(filename, **kwargs)
        self._saved_page_states = []
        self.brand_name = ""

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for i, state in enumerate(self._saved_page_states):
            self.__dict__.update(state)
            self._draw_decoration(i + 1, num_pages)
            pdfcanvas.Canvas.showPage(self)
        pdfcanvas.Canvas.save(self)

    def _draw_decoration(self, page_num, total_pages):
        # Top stripe
        self.setFillColor(COLORS["primary"])
        self.rect(0, PAGE_H - 5, PAGE_W, 5, fill=1, stroke=0)

        # Bottom footer bar
        self.setFillColor(COLORS["light_bg"])
        self.rect(0, 0, PAGE_W, 26, fill=1, stroke=0)
        self.setStrokeColor(COLORS["border"])
        self.setLineWidth(0.5)
        self.line(MARGIN, 26, PAGE_W - MARGIN, 26)

        self.setFillColor(COLORS["text_light"])
        self.setFont("Helvetica", 7.5)
        self.drawString(MARGIN, 9, "AI Marketing Suite — Confidentiel")
        if page_num > 1:
            self.drawCentredString(PAGE_W / 2, 9, f"{page_num} / {total_pages}")
        brand = getattr(self, "brand_name", "")
        if brand:
            self.drawRightString(PAGE_W - MARGIN, 9, brand)


# ---------------------------------------------------------------------------
# Styles factory
# ---------------------------------------------------------------------------
def make_styles():
    styles = getSampleStyleSheet()

    def ps(name, **kw):
        base = kw.pop("parent", styles["Normal"])
        return ParagraphStyle(name, parent=base, **kw)

    return {
        "title": ps("Ttl",
            fontSize=32, textColor=COLORS["white"],
            fontName="Helvetica-Bold", leading=38,
            alignment=TA_CENTER, spaceAfter=4),
        "subtitle": ps("Sub",
            fontSize=12, textColor=HexColor("#B8C8E8"),
            fontName="Helvetica", leading=16,
            alignment=TA_CENTER, spaceAfter=6),
        "heading": ps("H1",
            fontSize=16, textColor=COLORS["primary"],
            fontName="Helvetica-Bold", spaceBefore=4, spaceAfter=10),
        "subheading": ps("H2",
            fontSize=12, textColor=COLORS["accent"],
            fontName="Helvetica-Bold", spaceBefore=10, spaceAfter=6),
        "body": ps("Bd",
            fontSize=9.5, textColor=COLORS["text"],
            fontName="Helvetica", leading=14, spaceAfter=5),
        "body_sm": ps("BdSm",
            fontSize=8.5, textColor=COLORS["text"],
            fontName="Helvetica", leading=13, spaceAfter=4),
        "label": ps("Lbl",
            fontSize=8, textColor=COLORS["text_light"],
            fontName="Helvetica", leading=11),
        "footer": ps("Ftr",
            fontSize=7.5, textColor=COLORS["text_light"],
            fontName="Helvetica", alignment=TA_CENTER),
        "grade": ps("Grd",
            fontSize=13, textColor=COLORS["text"],
            fontName="Helvetica-Bold", alignment=TA_CENTER, spaceAfter=4),
        "action_item": ps("Act",
            fontSize=9.5, textColor=COLORS["text"],
            fontName="Helvetica", leading=14, spaceAfter=4,
            leftIndent=14, firstLineIndent=-14),
        # White bold style for table header cells (Paragraph overrides TableStyle TEXTCOLOR)
        "th": ps("TH",
            fontSize=9, textColor=COLORS["white"],
            fontName="Helvetica-Bold", leading=12),
    }


# ---------------------------------------------------------------------------
# Section header helper
# ---------------------------------------------------------------------------
def section_header(text, S):
    """Returns a band + spacer for a section title."""
    return [
        Spacer(1, 0.15 * inch),
        ColorBand(height=34, color=COLORS["primary"], text=text, font_size=13),
        Spacer(1, 0.12 * inch),
    ]


# ---------------------------------------------------------------------------
# Cover page builder
# ---------------------------------------------------------------------------
def build_cover(data, S, elements):
    # Dark header block
    url = data.get("url", "")
    brand = data.get("brand_name", url.replace("https://", "").split("/")[0])
    date_str = data.get("date", datetime.now().strftime("%B %d, %Y"))
    overall = int(data.get("overall_score", 0))
    grade = score_grade(overall)

    # Hero band
    cover_band = ColorBand(height=200, color=COLORS["primary"],
                           text="", font_size=0)
    # We'll use a Table to position text inside the dark band
    cover_table = Table(
        [[Paragraph("Rapport d'Audit Marketing", S["title"])],
         [Paragraph(url, S["subtitle"])],
         [Paragraph(f"Généré le : {date_str}", S["subtitle"])]],
        colWidths=[CONTENT_W]
    )
    cover_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), COLORS["primary"]),
        ("TOPPADDING", (0, 0), (-1, 0), 28),
        ("TOPPADDING", (0, 1), (-1, 1), 6),
        ("TOPPADDING", (0, 2), (-1, 2), 4),
        ("BOTTOMPADDING", (0, -1), (-1, -1), 28),
        ("LEFTPADDING", (0, 0), (-1, -1), 16),
        ("RIGHTPADDING", (0, 0), (-1, -1), 16),
    ]))
    elements.append(cover_table)
    elements.append(Spacer(1, 0.35 * inch))

    # Score gauge centred
    gauge_table = Table([[GaugeFlowable(overall, size=130)]], colWidths=[CONTENT_W])
    gauge_table.setStyle(TableStyle([
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    elements.append(gauge_table)
    elements.append(Spacer(1, 0.15 * inch))

    # Grade + score line
    color = score_color(overall)
    grade_para = Paragraph(
        f'<font color="#{color.hexval()[2:]}" size="18"><b>{overall}/100</b></font>'
        f'  <font color="#7F8C9B" size="12">— Note <b>{grade}</b></font>',
        S["grade"]
    )
    elements.append(grade_para)
    elements.append(Spacer(1, 0.2 * inch))

    # Divider
    elements.append(HRFlowable(width=CONTENT_W, thickness=1,
                                color=COLORS["border"], spaceAfter=12))

    # Executive summary
    exec_summary = data.get("executive_summary", "")
    if exec_summary:
        elements.append(Paragraph(exec_summary, S["body"]))

    elements.append(PageBreak())


# ---------------------------------------------------------------------------
# Score breakdown page
# ---------------------------------------------------------------------------
def build_scores(data, S, elements):
    elements += section_header("Analyse des Scores", S)

    categories = data.get("categories", {})
    cat_names = list(categories.keys()) if categories else [
        "Content & Messaging", "Conversion Optimization", "SEO & Discoverability",
        "Competitive Positioning", "Brand & Trust", "Growth & Strategy"
    ]
    cat_scores = [categories.get(c, {}).get("score", 50) for c in cat_names] if categories else [65]*6

    # Bar chart
    chart = BarChartFlowable(cat_names, cat_scores, width=CONTENT_W)
    elements.append(chart)
    elements.append(Spacer(1, 0.25 * inch))

    # Score table
    score_data = [[
        Paragraph("<b>Catégorie</b>", S["th"]),
        Paragraph("<b>Score</b>", S["th"]),
        Paragraph("<b>Poids</b>", S["th"]),
        Paragraph("<b>Statut</b>", S["th"]),
    ]]
    weights = ["25%", "20%", "20%", "15%", "10%", "10%"]
    for i, (name, score) in enumerate(zip(cat_names, cat_scores)):
        score = int(score)
        status = score_status(score)
        color = score_color(score)
        hex_c = color.hexval()[2:]
        score_data.append([
            Paragraph(name, S["body_sm"]),
            Paragraph(f'<font color="#{hex_c}"><b>{score}/100</b></font>', S["body_sm"]),
            Paragraph(weights[i] if i < len(weights) else "—", S["body_sm"]),
            Paragraph(status, S["body_sm"]),
        ])

    col_w = [CONTENT_W * f for f in [0.42, 0.18, 0.16, 0.24]]
    score_table = Table(score_data, colWidths=col_w, repeatRows=1)
    score_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), COLORS["primary"]),
        ("TEXTCOLOR", (0, 0), (-1, 0), COLORS["white"]),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("ALIGN", (1, 0), (-1, -1), "CENTER"),
        ("ALIGN", (0, 0), (0, -1), "LEFT"),
        ("GRID", (0, 0), (-1, -1), 0.4, COLORS["border"]),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [COLORS["white"], COLORS["light_bg"]]),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ]))
    elements.append(score_table)
    elements.append(PageBreak())


# ---------------------------------------------------------------------------
# Findings page
# ---------------------------------------------------------------------------
def build_findings(data, S, elements):
    elements += section_header("Constats Clés", S)

    findings = data.get("findings", [])

    SEV_HEX = {
        "Critical": "#FF1744",
        "High":     "#FF6B35",
        "Medium":   "#FFB300",
        "Low":      "#2D5BFF",
    }
    SEV_FR = {
        "Critical": "Critique",
        "High":     "Élevé",
        "Medium":   "Moyen",
        "Low":      "Faible",
    }

    findings_data = [[
        Paragraph("<b>Sévérité</b>", S["th"]),
        Paragraph("<b>Constat</b>", S["th"]),
    ]]
    for f in findings:
        sev = f.get("severity", "Medium")
        hex_c = SEV_HEX.get(sev, "#7F8C9B")
        sev_fr = SEV_FR.get(sev, sev)
        findings_data.append([
            Paragraph(f'<font color="{hex_c}"><b>{sev_fr}</b></font>', S["body_sm"]),
            Paragraph(f.get("finding", ""), S["body_sm"]),
        ])

    col_w = [CONTENT_W * 0.16, CONTENT_W * 0.84]
    findings_table = Table(findings_data, colWidths=col_w, repeatRows=1)
    findings_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), COLORS["primary"]),
        ("TEXTCOLOR", (0, 0), (-1, 0), COLORS["white"]),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("ALIGN", (0, 0), (0, -1), "CENTER"),
        ("ALIGN", (1, 0), (1, -1), "LEFT"),
        ("GRID", (0, 0), (-1, -1), 0.4, COLORS["border"]),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [COLORS["white"], COLORS["light_bg"]]),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ]))
    elements.append(findings_table)
    elements.append(PageBreak())


# ---------------------------------------------------------------------------
# Action plan page
# ---------------------------------------------------------------------------
def _action_block(title, items, color, S, elements):
    # Colored sub-header
    sub_band = ColorBand(height=26, color=color, text=title, font_size=11)
    elements.append(sub_band)
    elements.append(Spacer(1, 6))
    for i, item in enumerate(items, 1):
        elements.append(Paragraph(f"{i}.  {item}", S["action_item"]))
    elements.append(Spacer(1, 0.12 * inch))


def build_action_plan(data, S, elements):
    elements += section_header("Plan d'Action Priorisé", S)

    quick_wins = data.get("quick_wins", [])
    medium_term = data.get("medium_term", [])
    strategic = data.get("strategic", [])

    _action_block("Gains Rapides — Cette Semaine", quick_wins,
                  COLORS["success"], S, elements)
    _action_block("Moyen Terme — 1 à 3 Mois", medium_term,
                  COLORS["accent"], S, elements)
    _action_block("Stratégique — 3 à 6 Mois", strategic,
                  COLORS["highlight"], S, elements)

    elements.append(PageBreak())


# ---------------------------------------------------------------------------
# Competitive landscape
# ---------------------------------------------------------------------------
def build_competitive(data, S, elements):
    competitors = data.get("competitors", [])
    if not competitors:
        return

    elements += section_header("Paysage Concurrentiel", S)

    brand = data.get("brand_name", "Cible")
    client_data = data.get("client", {})  # optional client row data

    comps = competitors[:3]
    col_labels = [brand] + [c.get("name", f"Concurrent {i+1}") for i, c in enumerate(comps)]
    n_cols = len(col_labels)

    rows_def = [
        ("Positionnement", "positioning"),
        ("Tarifs",         "pricing"),
        ("Preuve Sociale", "social_proof"),
        ("Contenu",        "content"),
    ]

    # Header row
    header = [Paragraph("", S["th"])] + [
        Paragraph(f"<b>{lbl}</b>", S["th"]) for lbl in col_labels
    ]
    table_data = [header]

    for row_label, key in rows_def:
        client_val = client_data.get(key, "—") if client_data else "—"
        row = [Paragraph(f"<b>{row_label}</b>", S["body_sm"])]
        row.append(Paragraph(client_val, S["body_sm"]))
        for comp in comps:
            row.append(Paragraph(comp.get(key, "—"), S["body_sm"]))
        # Pad if fewer than 3 competitors
        while len(row) < n_cols + 1:
            row.append(Paragraph("—", S["body_sm"]))
        table_data.append(row)

    # Column widths: row label + equal share for each brand/comp
    row_label_w = 90
    col_share = (CONTENT_W - row_label_w) / (n_cols)
    col_widths = [row_label_w] + [col_share] * n_cols

    comp_table = Table(table_data, colWidths=col_widths, repeatRows=1)
    comp_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), COLORS["primary"]),
        ("TEXTCOLOR", (0, 0), (-1, 0), COLORS["white"]),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        # Highlight client column header
        ("BACKGROUND", (1, 0), (1, 0), COLORS["accent"]),
        ("BACKGROUND", (0, 1), (0, -1), COLORS["mid_bg"]),
        ("FONTNAME", (0, 1), (0, -1), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 8.5),
        ("GRID", (0, 0), (-1, -1), 0.4, COLORS["border"]),
        ("ROWBACKGROUNDS", (1, 1), (-1, -1), [COLORS["white"], COLORS["light_bg"]]),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("ALIGN", (0, 0), (-1, 0), "CENTER"),
    ]))
    elements.append(comp_table)
    elements.append(PageBreak())


# ---------------------------------------------------------------------------
# Methodology page
# ---------------------------------------------------------------------------
def build_methodology(data, S, elements):
    elements += section_header("Méthodologie", S)

    elements.append(Paragraph(
        "Cet audit évalue six dimensions clés de l'efficacité marketing. "
        "Chaque catégorie est notée de 0 à 100 selon les meilleures pratiques du secteur et des benchmarks concurrentiels.",
        S["body"]
    ))
    elements.append(Spacer(1, 0.1 * inch))

    method_data = [[
        Paragraph("<b>Catégorie</b>", S["th"]),
        Paragraph("<b>Poids</b>", S["th"]),
        Paragraph("<b>Ce que nous évaluons</b>", S["th"]),
    ]]
    rows = [
        ("Content & Messaging",      "25%", "Qualité du contenu, proposition de valeur, clarté des CTA"),
        ("Conversion Optimization",  "20%", "Conception du funnel, formulaires, preuve sociale, réduction des frictions"),
        ("SEO & Discoverability",    "20%", "SEO on-page, SEO technique, schémas, structure de contenu"),
        ("Competitive Positioning",  "15%", "Différenciation, tarification, stratégie face aux alternatives"),
        ("Brand & Trust",            "10%", "Qualité du design, signaux de confiance, indicateurs d'autorité"),
        ("Growth & Strategy",        "10%", "Canaux d'acquisition, email, stratégie contenu, fidélisation"),
    ]
    for cat, w, what in rows:
        method_data.append([
            Paragraph(cat, S["body_sm"]),
            Paragraph(w, S["body_sm"]),
            Paragraph(what, S["body_sm"]),
        ])

    col_w = [CONTENT_W * f for f in [0.35, 0.12, 0.53]]
    method_table = Table(method_data, colWidths=col_w, repeatRows=1)
    method_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), COLORS["primary"]),
        ("TEXTCOLOR", (0, 0), (-1, 0), COLORS["white"]),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("GRID", (0, 0), (-1, -1), 0.4, COLORS["border"]),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [COLORS["white"], COLORS["light_bg"]]),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("ALIGN", (1, 0), (1, -1), "CENTER"),
    ]))
    elements.append(method_table)

    elements.append(Spacer(1, 0.4 * inch))
    elements.append(HRFlowable(width=CONTENT_W, thickness=0.5,
                                color=COLORS["border"], spaceAfter=10))
    elements.append(Paragraph(
        "Généré par AI Marketing Suite pour Claude Code",
        S["footer"]
    ))


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------
def generate_report(data, output_path):
    """Generate a professional marketing PDF report."""

    brand = data.get("brand_name",
                     data.get("url", "").replace("https://", "").split("/")[0])

    class BrandedCanvas(NumberedCanvas):
        pass

    # Patch brand name into canvas class
    _brand = brand
    _orig_draw = NumberedCanvas._draw_decoration
    def _patched_draw(self, page_num, total):
        self.brand_name = _brand
        _orig_draw(self, page_num, total)
    BrandedCanvas._draw_decoration = _patched_draw

    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        rightMargin=MARGIN,
        leftMargin=MARGIN,
        topMargin=MARGIN + 10,
        bottomMargin=MARGIN + 10,
    )

    S = make_styles()
    elements = []

    build_cover(data, S, elements)
    build_scores(data, S, elements)
    build_findings(data, S, elements)
    build_action_plan(data, S, elements)
    build_competitive(data, S, elements)
    build_methodology(data, S, elements)

    doc.build(elements, canvasmaker=BrandedCanvas)
    return output_path


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------
def main():
    if len(sys.argv) < 2:
        sample_data = {
            "url": "https://example.com",
            "date": datetime.now().strftime("%B %d, %Y"),
            "brand_name": "Example Co",
            "overall_score": 62,
            "executive_summary": (
                "This marketing audit reveals several high-impact opportunities to improve "
                "conversion rates and strengthen competitive positioning. The website has solid "
                "content foundations but is underperforming in conversion optimization and "
                "competitive awareness. Implementing the quick wins below can yield a 15–25% "
                "increase in qualified leads within 30 days."
            ),
            "categories": {
                "Content & Messaging":     {"score": 68, "weight": "25%"},
                "Conversion Optimization": {"score": 52, "weight": "20%"},
                "SEO & Discoverability":   {"score": 74, "weight": "20%"},
                "Competitive Positioning": {"score": 48, "weight": "15%"},
                "Brand & Trust":           {"score": 70, "weight": "10%"},
                "Growth & Strategy":       {"score": 55, "weight": "10%"},
            },
            "findings": [
                {"severity": "Critical", "finding": "Homepage headline is generic — doesn't communicate specific value to target audience"},
                {"severity": "Critical", "finding": "No social proof visible above the fold on the homepage"},
                {"severity": "High",     "finding": "Primary CTA button says 'Submit' — should use value-driven text"},
                {"severity": "High",     "finding": "Pricing page lacks comparison features and doesn't address objections"},
                {"severity": "Medium",   "finding": "Missing competitor comparison pages — losing high-intent search traffic"},
                {"severity": "Medium",   "finding": "Blog posts have no internal links to product pages"},
                {"severity": "Low",      "finding": "Social media links in footer but no social proof integration"},
            ],
            "quick_wins": [
                "Rewrite homepage headline: 'We help businesses grow' → 'Get 3x more qualified leads in 30 days — without cold calling'",
                "Add 5 client logos above the fold with 'Trusted by 500+ companies' text",
                "Change form button from 'Submit' to 'Get My Free Marketing Audit'",
                "Add testimonial section with name, photo, company, and specific results",
            ],
            "medium_term": [
                "Build '[Competitor] Alternative' landing pages for top 3 competitors",
                "Create 3 video case studies showing measurable client results",
                "Implement exit-intent popup with lead magnet offer",
                "Launch email nurture sequence for leads who don't convert immediately",
            ],
            "strategic": [
                "Develop content authority hub with 10 pillar pages targeting high-volume keywords",
                "Build referral program with double-sided incentives",
                "Launch retargeting campaigns across Meta and Google with funnel-based messaging",
                "Create free tool or assessment to capture leads at top of funnel",
            ],
            "client": {
                "positioning": "SaaS growth analytics",
                "pricing":     "$99–499/mo",
                "social_proof":"250+ customers",
                "content":     "Blog + landing pages",
            },
            "competitors": [
                {"name": "Comp A", "positioning": "All-in-one platform", "pricing": "$49–199/mo", "social_proof": "10K+ users", "content": "Active blog + YouTube"},
                {"name": "Comp B", "positioning": "Enterprise focus",    "pricing": "Custom",      "social_proof": "Fortune 500 logos", "content": "Whitepapers + webinars"},
                {"name": "Comp C", "positioning": "Budget-friendly",     "pricing": "Free–$29/mo", "social_proof": "4.8★ G2",          "content": "YouTube + community"},
            ],
        }
        output = "MARKETING-REPORT-sample.pdf"
        generate_report(sample_data, output)
        print(f"Sample report generated: {output}")
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "MARKETING-REPORT.pdf"

    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    generate_report(data, output_file)
    print(f"Report generated: {output_file}")


if __name__ == "__main__":
    main()
