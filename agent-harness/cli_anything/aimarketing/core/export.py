"""Export module — save analysis results as Markdown or PDF files."""

import importlib.util
import json
import os
import sys
from datetime import datetime
from typing import Any, Dict, Optional

# scripts dir: core/ -> aimarketing/ -> cli_anything/ -> agent-harness/ -> ai-marketing-claude/ -> scripts/
_HERE = os.path.dirname(os.path.abspath(__file__))
_SCRIPTS_DIR = os.path.normpath(
    os.path.join(_HERE, "..", "..", "..", "..", "scripts")
)


def ensure_output_dir(output_dir: str) -> str:
    os.makedirs(output_dir, exist_ok=True)
    return output_dir


def _timestamped_filename(prefix: str, ext: str) -> str:
    ts = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    return f"{prefix}_{ts}.{ext}"


# ------------------------------------------------------------------
# Markdown export
# ------------------------------------------------------------------

def export_markdown(data: Dict[str, Any], output_dir: str = "./marketing-output") -> str:
    """Write analysis results to a Markdown file. Returns the file path."""
    ensure_output_dir(output_dir)
    command = data.get("command", "report")
    url = data.get("url", "")
    domain = url.replace("https://", "").replace("http://", "").split("/")[0] if url else "topic"

    filename = _timestamped_filename(f"MARKETING-{command.upper()}-{domain}", "md")
    filepath = os.path.join(output_dir, filename)

    lines = []
    lines.append(f"# Marketing {command.title()} Report")
    lines.append(f"\n**URL/Topic:** {url or data.get('topic', 'N/A')}")
    lines.append(f"**Generated:** {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}")
    lines.append(f"**Status:** {data.get('status', 'unknown')}\n")

    # Scores section
    scores = data.get("scores")
    if scores:
        lines.append("## Overall Score\n")
        overall = scores.get("overall", 0)
        grade = scores.get("grade", "?")
        lines.append(f"**{overall}/100 — Grade {grade}**\n")
        lines.append("| Dimension | Score |")
        lines.append("|-----------|-------|")
        for k, v in scores.items():
            if k not in ("overall", "grade"):
                lines.append(f"| {k.title()} | {v} |")
        lines.append("")

    # Recommendations
    recs = data.get("recommendations", [])
    if recs:
        lines.append("## Recommendations\n")
        for i, r in enumerate(recs, 1):
            lines.append(f"{i}. {r}")
        lines.append("")

    # Revenue impact
    impact = data.get("revenue_impact")
    if impact:
        lines.append("## Revenue Impact Estimate\n")
        lines.append(f"- Monthly visitors assumed: {impact.get('assumed_monthly_visitors', 'N/A')}")
        lines.append(f"- Conversion lift: {impact.get('estimated_conversion_lift_pct', 0)}%")
        lines.append(f"- Monthly revenue impact: ${impact.get('estimated_monthly_revenue_impact_usd', 0):,.0f}")
        lines.append(f"- Confidence: {impact.get('confidence', 'N/A')}\n")

    # Emails
    emails = data.get("emails", [])
    if emails:
        lines.append("## Email Sequence\n")
        overview = data.get("overview", {})
        if overview:
            lines.append(f"**Goal:** {overview.get('goal')}")
            lines.append(f"**Duration:** {overview.get('duration_days')} days | {overview.get('total_emails')} emails\n")
        for email in emails:
            lines.append(f"### Email {email['number']} — {email['send_day']}")
            lines.append(f"**Subject:** {email['subject']}")
            lines.append(f"**Goal:** {email['goal']}")
            lines.append("**Body structure:**")
            for step in email.get("body_structure", []):
                lines.append(f"  - {step}")
            lines.append("")

    # Social calendar (first 7 days in export)
    calendar = data.get("calendar", [])
    if calendar:
        lines.append(f"## Social Calendar ({data.get('platform', 'Social')})\n")
        for post in calendar[:7]:
            lines.append(f"### Day {post['day']} — {post['pillar']}")
            lines.append(f"**Hook:** {post['hook']}")
            lines.append(f"**Caption:** {post['caption']}")
            lines.append(f"**Best time:** {post['best_time']}\n")
        if len(calendar) > 7:
            lines.append(f"*... {len(calendar) - 7} more days in full export*\n")

    # Proposal-specific sections
    executive_summary = data.get("executive_summary")
    if executive_summary:
        lines.append("## Executive Summary\n")
        lines.append(f"{executive_summary}\n")

    scope = data.get("scope", [])
    if scope:
        lines.append("## Scope of Work\n")
        for item in scope:
            lines.append(f"- {item}")
        lines.append("")

    deliverables = data.get("deliverables", [])
    if deliverables:
        lines.append("## Deliverables\n")
        for item in deliverables:
            lines.append(f"- {item}")
        lines.append("")

    investment_tiers = data.get("investment_tiers", {})
    if investment_tiers:
        lines.append("## Investment\n")
        lines.append("| Tier | Price | Includes |")
        lines.append("|------|-------|----------|")
        for tier, info in investment_tiers.items():
            lines.append(f"| {tier.title()} | {info.get('price', '—')} | {info.get('includes', '—')} |")
        lines.append("")

    timeline = data.get("timeline")
    if timeline:
        lines.append("## Timeline\n")
        lines.append(f"{timeline}\n")

    next_steps = data.get("next_steps", [])
    if next_steps:
        lines.append("## Next Steps\n")
        for step in next_steps:
            lines.append(f"{step}")
        lines.append("")

    # Errors
    errors = data.get("errors", [])
    if errors:
        lines.append("## Errors\n")
        for e in errors:
            lines.append(f"- {e}")

    content = "\n".join(lines)
    with open(filepath, "w", encoding="utf-8") as fh:
        fh.write(content)

    return filepath


# ------------------------------------------------------------------
# PDF export (uses generate_pdf_report.py from scripts)
# ------------------------------------------------------------------

def _transform_audit_for_pdf(data: Dict[str, Any]) -> Dict[str, Any]:
    """Convert raw CLI audit data to the format expected by generate_pdf_report.py."""
    scores = data.get("scores", {})
    analysis = data.get("analysis", {})
    recs = data.get("recommendations", [])
    impact = data.get("revenue_impact", {})
    url = data.get("url", "")

    # Map dimension scores to category names
    cat_map = {
        "Content & Messaging":      scores.get("content", 50),
        "Conversion Optimization":  scores.get("conversion", 50),
        "SEO & Discoverability":    scores.get("seo", 50),
        "Competitive Positioning":  scores.get("competitive", 50),
        "Brand & Trust":            scores.get("brand", 50),
        "Growth & Strategy":        scores.get("growth", 50),
    }
    categories = {k: {"score": v, "weight": w} for (k, v), w in zip(
        cat_map.items(), ["25%", "20%", "20%", "15%", "10%", "10%"]
    )}

    # Build findings from analysis
    findings = []
    seo = analysis.get("seo", {})
    conversion = analysis.get("conversion", {})
    tracking = analysis.get("tracking", {})
    content = analysis.get("content", {})

    if not seo.get("headings", {}).get("h1"):
        findings.append({"severity": "Critical", "finding": "H1 absent — aucun mot-clé principal visible par Google et les visiteurs."})
    wc = content.get("word_count", 0)
    if wc < 100:
        findings.append({"severity": "Critical", "finding": f"Contenu quasi-inexistant ({wc} mots détectés) — le site est probablement une SPA React non rendue côté serveur (SSR manquant)."})
    if not conversion.get("ctas"):
        findings.append({"severity": "Critical", "finding": "Aucun CTA détecté — aucun appel à l'action visible pour convertir les visiteurs."})
    if not conversion.get("forms"):
        findings.append({"severity": "High", "finding": "Aucun formulaire de capture de leads — impossible de constituer une liste email."})
    if not tracking.get("tools_detected"):
        findings.append({"severity": "High", "finding": "Aucun outil analytics détecté (GA4, GTM, Pixel…) — les performances sont complètement invisibles."})
    title_len = seo.get("title_length", 0)
    if title_len > 60:
        findings.append({"severity": "Medium", "finding": f"Title trop long ({title_len} caractères, max 60) — tronqué dans les résultats Google."})
    meta_len = seo.get("meta_description_length", 0)
    if meta_len > 160:
        findings.append({"severity": "Medium", "finding": f"Meta description trop longue ({meta_len} caractères, max 160) — tronquée dans les SERPs."})
    if not seo.get("og_tags"):
        findings.append({"severity": "Medium", "finding": "Open Graph tags absents — les partages sur réseaux sociaux n'auront pas de visuel ni de titre optimisé."})
    if not tracking.get("schema_types"):
        findings.append({"severity": "Low", "finding": "Aucun Schema markup (JSON-LD) — pas de rich snippets dans Google."})

    # Split recommendations into quick/medium/strategic
    quick_wins = recs[:3]
    medium_term = recs[3:6] if len(recs) > 3 else [
        "Mettre en place le SSR/prerendering pour rendre le contenu React indexable",
        "Créer une page pricing transparente",
        "Lancer une séquence email d'onboarding pour les nouveaux inscrits",
    ]
    strategic = recs[6:] if len(recs) > 6 else [
        "Développer un blog avec 10 articles piliers sur les mots-clés IA/automatisation",
        "Créer un programme de parrainage client",
        "Lancer des campagnes retargeting Meta + Google avec messaging par étape de funnel",
    ]

    monthly_impact = impact.get("estimated_monthly_revenue_impact_usd", 0)
    exec_summary = (
        f"Cet audit marketing de {url} révèle un score global de {scores.get('overall', 0)}/100. "
        f"Le site souffre principalement d'un manque de conversion (score : {scores.get('conversion', 0)}/100) "
        f"et d'un contenu non indexable (SPA React sans SSR). "
        f"La mise en œuvre des actions prioritaires peut générer jusqu'à "
        f"+${monthly_impact:,.0f}/mois de revenus additionnels estimés."
    )

    return {
        "url": url,
        "brand_name": url.replace("https://", "").split("/")[0],
        "date": datetime.utcnow().strftime("%d %B %Y"),
        "overall_score": scores.get("overall", 0),
        "executive_summary": exec_summary,
        "categories": categories,
        "findings": findings,
        "quick_wins": quick_wins,
        "medium_term": medium_term,
        "strategic": strategic,
        "competitors": [],
    }


def export_pdf(data: Dict[str, Any], output_dir: str = "./marketing-output") -> str:
    """Generate a PDF report. Returns the file path."""
    ensure_output_dir(output_dir)
    url = data.get("url", "")
    domain = url.replace("https://", "").replace("http://", "").split("/")[0] if url else "report"
    filename = _timestamped_filename(f"MARKETING-REPORT-{domain}", "pdf")
    filepath = os.path.join(output_dir, filename)

    # Try to use the project's generate_pdf_report.py
    pdf_script = os.path.join(_SCRIPTS_DIR, "generate_pdf_report.py")
    if os.path.exists(pdf_script):
        spec = importlib.util.spec_from_file_location("generate_pdf_report", pdf_script)
        mod = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(mod)
            pdf_data = _transform_audit_for_pdf(data)
            if hasattr(mod, "generate_report"):
                mod.generate_report(pdf_data, filepath)
                return filepath
            elif hasattr(mod, "create_pdf_report"):
                mod.create_pdf_report(pdf_data, filepath)
                return filepath
        except Exception:
            pass  # Fall through to minimal PDF

    # Fallback: minimal PDF via reportlab
    try:
        from reportlab.lib.pagesizes import letter
        from reportlab.pdfgen import canvas as rl_canvas

        c = rl_canvas.Canvas(filepath, pagesize=letter)
        width, height = letter
        y = height - 72

        c.setFont("Helvetica-Bold", 20)
        c.drawString(72, y, "Marketing Analysis Report")
        y -= 30

        c.setFont("Helvetica", 12)
        c.drawString(72, y, f"URL: {data.get('url', data.get('topic', 'N/A'))}")
        y -= 20
        c.drawString(72, y, f"Generated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}")
        y -= 30

        scores = data.get("scores", {})
        if scores:
            c.setFont("Helvetica-Bold", 14)
            c.drawString(72, y, f"Overall Score: {scores.get('overall', 0)}/100 (Grade {scores.get('grade', '?')})")
            y -= 25
            c.setFont("Helvetica", 11)
            for k, v in scores.items():
                if k not in ("overall", "grade") and y > 100:
                    c.drawString(90, y, f"  {k.title()}: {v}")
                    y -= 18

        recs = data.get("recommendations", [])
        if recs and y > 150:
            y -= 10
            c.setFont("Helvetica-Bold", 13)
            c.drawString(72, y, "Top Recommendations:")
            y -= 20
            c.setFont("Helvetica", 11)
            for r in recs[:5]:
                if y > 80:
                    c.drawString(90, y, f"• {r[:90]}")
                    y -= 16

        c.save()
        return filepath

    except ImportError:
        raise RuntimeError(
            "PDF generation requires reportlab. Install with: pip install reportlab"
        )


# ------------------------------------------------------------------
# JSON export
# ------------------------------------------------------------------

def export_json(data: Dict[str, Any], output_dir: str = "./marketing-output") -> str:
    """Write analysis results to a JSON file. Returns the file path."""
    ensure_output_dir(output_dir)
    command = data.get("command", "report")
    filename = _timestamped_filename(f"marketing-{command}", "json")
    filepath = os.path.join(output_dir, filename)
    with open(filepath, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2, default=str)
    return filepath
