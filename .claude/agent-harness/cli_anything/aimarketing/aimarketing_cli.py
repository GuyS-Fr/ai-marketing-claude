"""cli-anything-aimarketing — CLI harness for the ai-marketing-claude suite.

Usage:
    cli-anything-aimarketing [--json] COMMAND [ARGS]
    cli-anything-aimarketing repl
"""

import cmd
import json
import sys
from typing import Optional

import click

from cli_anything.aimarketing.core.session import Session
from cli_anything.aimarketing.core.audit import run_audit, run_quick
from cli_anything.aimarketing.core.content import analyze_copy, generate_copy
from cli_anything.aimarketing.core.email_gen import generate_email_sequence, SEQUENCE_TYPES
from cli_anything.aimarketing.core.social import generate_social_calendar, PLATFORMS
from cli_anything.aimarketing.core.competitor import scan_competitors, scan_competitor
from cli_anything.aimarketing.core.export import export_markdown, export_pdf, export_json

_SESSION = Session()


# ---------------------------------------------------------------------------
# Output helpers
# ---------------------------------------------------------------------------

def _out(ctx: click.Context, data: dict) -> None:
    """Print data as JSON or human-readable text."""
    if ctx.obj.get("json"):
        click.echo(json.dumps(data, indent=2, default=str))
    else:
        _human(data)


def _human(data: dict) -> None:
    command = data.get("command", "")
    status = data.get("status", "")
    url = data.get("url") or data.get("topic", "")

    click.echo(f"\n{'='*60}")
    click.echo(f"  cli-anything-aimarketing  ·  {command.upper()}")
    click.echo(f"{'='*60}")
    if url:
        click.echo(f"  Target : {url}")
    click.echo(f"  Status : {status}\n")

    scores = data.get("scores")
    if scores:
        overall = scores.get("overall", 0)
        grade = scores.get("grade", "?")
        click.echo(f"  Overall Score : {overall}/100  [{grade}]")
        click.echo("")
        dims = {k: v for k, v in scores.items() if k not in ("overall", "grade")}
        for dim, val in dims.items():
            bar = "█" * int(val // 10) + "░" * (10 - int(val // 10))
            click.echo(f"  {dim:<14} {bar}  {val:.0f}")
        click.echo("")

    recs = data.get("recommendations") or data.get("top_3_actions", [])
    if recs:
        click.echo("  Quick Wins:")
        for i, r in enumerate(recs[:5], 1):
            click.echo(f"  {i}. {r}")
        click.echo("")

    impact = data.get("revenue_impact")
    if impact:
        click.echo(f"  Revenue Impact: +${impact.get('estimated_monthly_revenue_impact_usd', 0):,.0f}/month")
        click.echo(f"  Confidence    : {impact.get('confidence', 'N/A')}\n")

    overview = data.get("overview")
    if overview:
        click.echo(f"  Sequence: {overview.get('total_emails')} emails over {overview.get('duration_days')} days")
        click.echo(f"  Goal    : {overview.get('goal')}\n")
        emails = data.get("emails", [])
        for e in emails[:3]:
            click.echo(f"  Email {e['number']} [{e['send_day']}] → {e['subject']}")
        if len(emails) > 3:
            click.echo(f"  ... and {len(emails) - 3} more\n")

    cal = data.get("calendar")
    if cal:
        click.echo(f"  Platform : {data.get('platform')}")
        click.echo(f"  Days     : {data.get('duration_days')}\n")
        for post in cal[:3]:
            click.echo(f"  Day {post['day']:2d} [{post['pillar']:<18}] {post['hook'][:55]}")
        click.echo(f"  ... {len(cal) - 3} more days\n")

    errors = data.get("errors", [])
    if errors:
        click.echo(f"  [!] Errors: {', '.join(errors)}\n")

    click.echo(f"{'='*60}\n")


# ---------------------------------------------------------------------------
# CLI group
# ---------------------------------------------------------------------------

@click.group(context_settings={"help_option_names": ["-h", "--help"]})
@click.option("--json", "output_json", is_flag=True, default=False,
              help="Output results as JSON (for agent/script consumption).")
@click.option("--output-dir", default=None,
              help="Directory for saved output files.")
@click.pass_context
def cli(ctx: click.Context, output_json: bool, output_dir: Optional[str]) -> None:
    """cli-anything-aimarketing — AI-powered marketing analysis CLI.

    Run any command with --json for machine-readable output.
    Use 'repl' for an interactive session.
    """
    ctx.ensure_object(dict)
    ctx.obj["json"] = output_json
    ctx.obj["session"] = _SESSION
    if output_dir:
        _SESSION.output_dir = output_dir


# ---------------------------------------------------------------------------
# audit
# ---------------------------------------------------------------------------

@cli.command()
@click.argument("url")
@click.option("--save", is_flag=True, help="Save report to output directory.")
@click.pass_context
def audit(ctx: click.Context, url: str, save: bool) -> None:
    """Full 6-dimension marketing audit of a URL."""
    result = run_audit(url)
    _SESSION.current_url = url
    _SESSION.last_audit = result
    _SESSION.push_history("audit", url, f"Score: {result['scores'].get('overall')}")
    if save:
        path = export_markdown(result, _SESSION.output_dir)
        result["saved_to"] = path
    _out(ctx, result)


# ---------------------------------------------------------------------------
# quick
# ---------------------------------------------------------------------------

@cli.command()
@click.argument("url")
@click.pass_context
def quick(ctx: click.Context, url: str) -> None:
    """60-second marketing snapshot of a URL."""
    result = run_quick(url)
    _SESSION.current_url = url
    _SESSION.push_history("quick", url, f"Score: {result['scores'].get('overall')}")
    _out(ctx, result)


# ---------------------------------------------------------------------------
# copy
# ---------------------------------------------------------------------------

@cli.command()
@click.argument("url")
@click.option("--save", is_flag=True)
@click.pass_context
def copy(ctx: click.Context, url: str, save: bool) -> None:
    """Analyze and optimize copy on a webpage."""
    result = analyze_copy(url)
    _SESSION.current_url = url
    _SESSION.push_history("copy", url, f"Copy score: {result.get('copy_score')}")
    if save:
        result["saved_to"] = export_markdown(result, _SESSION.output_dir)
    _out(ctx, result)


# ---------------------------------------------------------------------------
# emails
# ---------------------------------------------------------------------------

@cli.command()
@click.argument("topic")
@click.option("--type", "seq_type", default="welcome",
              type=click.Choice(SEQUENCE_TYPES, case_sensitive=False),
              help="Sequence type.")
@click.option("--audience", default="business owners", help="Target audience.")
@click.option("--save", is_flag=True)
@click.pass_context
def emails(ctx: click.Context, topic: str, seq_type: str, audience: str, save: bool) -> None:
    """Generate an email sequence for a topic or URL."""
    result = generate_email_sequence(topic, seq_type, audience)
    _SESSION.push_history("emails", None, f"{seq_type} sequence for '{topic}'")
    if save:
        result["saved_to"] = export_markdown(result, _SESSION.output_dir)
    _out(ctx, result)


# ---------------------------------------------------------------------------
# social
# ---------------------------------------------------------------------------

@cli.command()
@click.argument("topic")
@click.option("--platform", default="LinkedIn",
              type=click.Choice(PLATFORMS, case_sensitive=False))
@click.option("--audience", default="entrepreneurs")
@click.option("--days", default=30, type=int)
@click.option("--save", is_flag=True)
@click.pass_context
def social(ctx: click.Context, topic: str, platform: str, audience: str, days: int, save: bool) -> None:
    """Generate a social media content calendar."""
    result = generate_social_calendar(topic, audience, platform, days)
    _SESSION.push_history("social", None, f"{days}-day {platform} calendar for '{topic}'")
    if save:
        result["saved_to"] = export_markdown(result, _SESSION.output_dir)
    _out(ctx, result)


# ---------------------------------------------------------------------------
# competitors
# ---------------------------------------------------------------------------

@cli.command()
@click.argument("urls", nargs=-1, required=True)
@click.option("--main-url", default=None, help="Your own URL for comparison context.")
@click.option("--save", is_flag=True)
@click.pass_context
def competitors(ctx: click.Context, urls: tuple, main_url: Optional[str], save: bool) -> None:
    """Scan competitor URLs and generate intelligence report."""
    result = scan_competitors(list(urls), main_url=main_url)
    _SESSION.push_history("competitors", main_url, f"Scanned {len(urls)} competitor(s)")
    if save:
        result["saved_to"] = export_markdown(result, _SESSION.output_dir)
    _out(ctx, result)


# ---------------------------------------------------------------------------
# landing
# ---------------------------------------------------------------------------

@cli.command()
@click.argument("url")
@click.option("--save", is_flag=True)
@click.pass_context
def landing(ctx: click.Context, url: str, save: bool) -> None:
    """CRO analysis of a landing page."""
    from cli_anything.aimarketing.utils.scraper import fetch_page_analysis
    raw = fetch_page_analysis(url)
    analysis = raw.get("analysis", {})
    conversion = analysis.get("conversion", {})
    ctas = conversion.get("ctas", [])
    forms = conversion.get("forms", [])

    cro_score = min(100, len(ctas) * 15 + len(forms) * 20 + 30)

    result = {
        "command": "landing",
        "url": url,
        "status": raw.get("status", "unknown"),
        "cro_score": cro_score,
        "ctas_found": ctas,
        "forms_found": forms,
        "cro_checklist": {
            "hero_headline_clear": bool(analysis.get("seo", {}).get("headings", {}).get("h1")),
            "cta_above_fold": len(ctas) > 0,
            "social_proof_present": analysis.get("trust", {}).get("social_link_count", 0) > 0,
            "mobile_ready": bool(analysis.get("seo", {}).get("viewport")),
            "form_present": len(forms) > 0,
            "trust_signals": bool(analysis.get("tracking", {}).get("tools_detected")),
        },
        "recommendations": [
            "Ensure primary CTA is visible without scrolling",
            "Add customer testimonials near the main form",
            "Test contrasting CTA button color against page background",
            "Add urgency element (limited time offer, countdown timer)",
            "Reduce form fields to 3 or fewer for top-of-funnel",
        ],
        "errors": [raw["error"]] if "error" in raw else [],
    }
    _SESSION.current_url = url
    _SESSION.push_history("landing", url, f"CRO score: {cro_score}")
    if save:
        result["saved_to"] = export_markdown(result, _SESSION.output_dir)
    _out(ctx, result)


# ---------------------------------------------------------------------------
# seo
# ---------------------------------------------------------------------------

@cli.command()
@click.argument("url")
@click.option("--save", is_flag=True)
@click.pass_context
def seo(ctx: click.Context, url: str, save: bool) -> None:
    """SEO technical audit of a URL."""
    from cli_anything.aimarketing.utils.scraper import fetch_page_analysis
    from cli_anything.aimarketing.core.audit import _score_seo, _grade
    raw = fetch_page_analysis(url)
    analysis = raw.get("analysis", {})
    s = analysis.get("seo", {})
    seo_score = _score_seo(analysis)

    issues = []
    if not s.get("title"):
        issues.append("Missing <title> tag")
    if not s.get("meta_description"):
        issues.append("Missing meta description")
    if not s.get("headings", {}).get("h1"):
        issues.append("No H1 tag found")
    if not s.get("og_tags"):
        issues.append("No Open Graph tags — impacts social sharing")
    if not s.get("canonical"):
        issues.append("No canonical URL specified")

    result = {
        "command": "seo",
        "url": url,
        "status": raw.get("status", "unknown"),
        "scores": {
            "overall": seo_score,
            "grade": _grade(seo_score),
        },
        "seo_elements": {
            "title": s.get("title", ""),
            "meta_description": s.get("meta_description", ""),
            "h1_tags": s.get("headings", {}).get("h1", []),
            "h2_tags": s.get("headings", {}).get("h2", [])[:5],
            "og_tags": s.get("og_tags", {}),
            "canonical": s.get("canonical", ""),
            "viewport": s.get("viewport", ""),
        },
        "schema_types": analysis.get("tracking", {}).get("schema_types", []),
        "issues": issues,
        "recommendations": [
            "Add unique meta description to every page (150-160 chars)",
            "Include primary keyword in H1 — only one H1 per page",
            "Build schema markup (FAQ, Product, Article) for rich snippets",
            "Create XML sitemap and submit to Google Search Console",
            "Improve Core Web Vitals — target LCP < 2.5s",
        ],
        "errors": [raw["error"]] if "error" in raw else [],
    }
    _SESSION.current_url = url
    _SESSION.push_history("seo", url, f"SEO score: {seo_score}")
    if save:
        result["saved_to"] = export_markdown(result, _SESSION.output_dir)
    _out(ctx, result)


# ---------------------------------------------------------------------------
# brand
# ---------------------------------------------------------------------------

@cli.command()
@click.argument("url")
@click.option("--save", is_flag=True)
@click.pass_context
def brand(ctx: click.Context, url: str, save: bool) -> None:
    """Brand voice and identity analysis."""
    from cli_anything.aimarketing.utils.scraper import fetch_page_analysis
    raw = fetch_page_analysis(url)
    analysis = raw.get("analysis", {})
    seo = analysis.get("seo", {})
    trust = analysis.get("trust", {})

    result = {
        "command": "brand",
        "url": url,
        "status": raw.get("status", "unknown"),
        "voice_dimensions": {
            "formal_to_casual": "Unable to determine without NLP — review manually",
            "serious_to_playful": "Review tone of headlines: " + str(seo.get("headings", {}).get("h1", [])),
            "technical_to_simple": "Review jargon density in copy",
            "reserved_to_bold": "Review CTA language strength",
        },
        "brand_signals": {
            "social_presence": trust.get("social_links", []),
            "tracking_tools": analysis.get("tracking", {}).get("tools_detected", []),
            "schema_markup": analysis.get("tracking", {}).get("schema_types", []),
        },
        "brand_checklist": {
            "consistent_logo": "Verify manually",
            "color_system_defined": "Verify in CSS/design",
            "typography_consistent": "Verify in CSS",
            "tone_guide_exists": "Verify in documentation",
        },
        "recommendations": [
            "Document brand voice in a 1-page guide with do/don't examples",
            "Audit all touchpoints (website, email, social, ads) for tone consistency",
            "Define 3–5 brand personality traits and filter all copy through them",
            "Create a swipe file of on-brand copy that resonates with your audience",
        ],
        "errors": [raw["error"]] if "error" in raw else [],
    }
    _SESSION.current_url = url
    _SESSION.push_history("brand", url, "Brand analysis complete")
    if save:
        result["saved_to"] = export_markdown(result, _SESSION.output_dir)
    _out(ctx, result)


# ---------------------------------------------------------------------------
# report (markdown)
# ---------------------------------------------------------------------------

@cli.command()
@click.argument("url")
@click.pass_context
def report(ctx: click.Context, url: str) -> None:
    """Generate and save a full Markdown marketing report."""
    result = run_audit(url)
    result["command"] = "report"
    _SESSION.current_url = url
    _SESSION.last_audit = result
    filepath = export_markdown(result, _SESSION.output_dir)
    result["saved_to"] = filepath
    _SESSION.push_history("report", url, f"Saved: {filepath}")
    _out(ctx, result)


# ---------------------------------------------------------------------------
# pdf
# ---------------------------------------------------------------------------

@cli.command()
@click.argument("url")
@click.pass_context
def pdf(ctx: click.Context, url: str) -> None:
    """Generate a professional PDF marketing report."""
    result = run_audit(url)
    result["command"] = "pdf"
    _SESSION.current_url = url
    try:
        filepath = export_pdf(result, _SESSION.output_dir)
        result["saved_to"] = filepath
        _SESSION.push_history("pdf", url, f"PDF saved: {filepath}")
    except RuntimeError as exc:
        result["errors"] = [str(exc)]
    _out(ctx, result)


# ---------------------------------------------------------------------------
# launch
# ---------------------------------------------------------------------------

@cli.command()
@click.argument("product")
@click.option("--audience", default="early adopters")
@click.option("--save", is_flag=True)
@click.pass_context
def launch(ctx: click.Context, product: str, audience: str, save: bool) -> None:
    """Generate a product launch playbook."""
    email_result = generate_email_sequence(product, "launch", audience)
    social_result = generate_social_calendar(product, audience, "LinkedIn", 14)

    result = {
        "command": "launch",
        "topic": product,
        "audience": audience,
        "status": "success",
        "launch_phases": {
            "pre_launch": {
                "days": "-14 to -1",
                "tasks": [
                    "Build waitlist landing page",
                    "Start teaser email sequence",
                    "Begin social countdown content",
                    "Set up affiliate/referral program",
                    "Prepare press/media kit",
                ],
            },
            "launch_day": {
                "days": "0",
                "tasks": [
                    "Send launch announcement email",
                    "Publish launch day social posts",
                    "Activate paid ads",
                    "Monitor and respond to all comments",
                    "Reach out to podcast/newsletter partners",
                ],
            },
            "post_launch": {
                "days": "+1 to +7",
                "tasks": [
                    "Send case study / testimonial emails",
                    "Run urgency campaigns (limited time/spots)",
                    "Retarget page visitors",
                    "Close cart with final email",
                    "Send post-purchase onboarding sequence",
                ],
            },
        },
        "email_sequence_preview": email_result.get("emails", [])[:3],
        "social_preview": social_result.get("calendar", [])[:5],
        "kpis": [
            "Email open rate: target 35%+",
            "Email click rate: target 5%+",
            "Waitlist to buyer conversion: target 10%+",
            "Social reach vs engagement rate: target 3%+",
        ],
    }
    _SESSION.push_history("launch", None, f"Launch playbook for '{product}'")
    if save:
        result["saved_to"] = export_markdown(result, _SESSION.output_dir)
    _out(ctx, result)


# ---------------------------------------------------------------------------
# proposal
# ---------------------------------------------------------------------------

@cli.command()
@click.argument("client")
@click.option("--service", default="full marketing audit and strategy")
@click.option("--save", is_flag=True)
@click.pass_context
def proposal(ctx: click.Context, client: str, service: str, save: bool) -> None:
    """Generate a client marketing proposal."""
    result = {
        "command": "proposal",
        "client": client,
        "service": service,
        "status": "success",
        "executive_summary": f"This proposal outlines a comprehensive {service} engagement for {client}, designed to identify growth opportunities and deliver measurable ROI.",
        "scope": [
            "Full marketing audit (6-dimension scoring)",
            "Competitive analysis (3 key competitors)",
            "Copy optimization recommendations",
            "30-day content calendar",
            "Email sequence (welcome + nurture)",
            "PDF report with executive summary",
        ],
        "deliverables": [
            "MARKETING-AUDIT.md — full analysis report",
            "COMPETITOR-REPORT.md — competitive intelligence",
            "COPY-SUGGESTIONS.md — before/after headline examples",
            "SOCIAL-CALENDAR.md — 30-day ready-to-post calendar",
            "EMAIL-SEQUENCES.md — 11 ready-to-send emails",
            "MARKETING-REPORT.pdf — executive presentation",
        ],
        "investment_tiers": {
            "starter": {"price": "$497", "includes": "Audit + PDF report"},
            "growth": {"price": "$997", "includes": "Audit + copy + emails + social calendar"},
            "premium": {"price": "$1,997", "includes": "Everything + 30-day implementation support"},
        },
        "timeline": "5 business days from project kickoff",
        "next_steps": [
            f"1. Review proposal and select investment tier",
            f"2. Sign service agreement",
            f"3. Provide access to analytics (GA4, ad accounts if applicable)",
            f"4. Kickoff call to align on priorities",
        ],
    }
    _SESSION.push_history("proposal", None, f"Proposal for '{client}'")
    if save:
        result["saved_to"] = export_markdown(result, _SESSION.output_dir)
    _out(ctx, result)


# ---------------------------------------------------------------------------
# ads
# ---------------------------------------------------------------------------

@cli.command()
@click.argument("url")
@click.option("--platform", "ad_platform", default="Google",
              type=click.Choice(["Google", "Meta", "LinkedIn", "TikTok", "YouTube"], case_sensitive=False))
@click.option("--save", is_flag=True)
@click.pass_context
def ads(ctx: click.Context, url: str, ad_platform: str, save: bool) -> None:
    """Generate ad campaign copy and targeting strategy."""
    from cli_anything.aimarketing.utils.scraper import fetch_page_analysis
    raw = fetch_page_analysis(url)
    analysis = raw.get("analysis", {})
    seo = analysis.get("seo", {})
    title = seo.get("title", "Your Product")
    h1s = seo.get("headings", {}).get("h1", [])
    main_headline = h1s[0] if h1s else title

    ad_templates = {
        "Google": {
            "headlines": [
                f"{main_headline[:30]}",
                "Get Results in 30 Days",
                "Free Trial — No Credit Card",
            ],
            "descriptions": [
                f"Discover how {title[:20]} helps you achieve [goal]. Trusted by [X]+ customers.",
                "Start free today. No contracts. Cancel anytime. Join [X]+ happy customers.",
            ],
            "extensions": ["Sitelinks: Pricing | Features | Case Studies | Free Trial"],
        },
        "Meta": {
            "primary_text": f"Tired of [pain point]? {main_headline[:50]} might be the answer. Here's what [X] customers say...",
            "headline": f"{main_headline[:40]}",
            "description": "Learn more →",
            "audience_targeting": ["Interest: [niche]", "Lookalike: 1% of customers", "Retarget: site visitors"],
        },
        "LinkedIn": {
            "headline": f"{main_headline[:70]}",
            "intro_text": f"For [job title] who want [outcome]. {title} helps you [specific benefit]. [Social proof stat].",
            "cta": "Learn More",
            "targeting": ["Job title: [target role]", "Industry: [target industry]", "Company size: 11–200"],
        },
    }

    result = {
        "command": "ads",
        "url": url,
        "platform": ad_platform,
        "status": raw.get("status", "unknown"),
        "ad_copy": ad_templates.get(ad_platform, ad_templates["Google"]),
        "landing_page_alignment": {
            "message_match": "Ensure ad headline matches landing page H1",
            "offer_clarity": "Lead with same offer in ad and on landing page",
            "trust_signals": "Match social proof claims across ad and landing page",
        },
        "budget_guidance": {
            "test_budget": "$300–$500 to gather initial data",
            "scaling_signal": "Scale when Cost Per Acquisition < 30% of LTV",
            "optimize_at": "50+ conversions per ad set before scaling",
        },
        "errors": [raw["error"]] if "error" in raw else [],
    }
    _SESSION.current_url = url
    _SESSION.push_history("ads", url, f"{ad_platform} ads generated")
    if save:
        result["saved_to"] = export_markdown(result, _SESSION.output_dir)
    _out(ctx, result)


# ---------------------------------------------------------------------------
# funnel
# ---------------------------------------------------------------------------

@cli.command()
@click.argument("url")
@click.option("--save", is_flag=True)
@click.pass_context
def funnel(ctx: click.Context, url: str, save: bool) -> None:
    """Sales funnel analysis and conversion optimization."""
    from cli_anything.aimarketing.utils.scraper import fetch_page_analysis
    raw = fetch_page_analysis(url)
    analysis = raw.get("analysis", {})
    conversion = analysis.get("conversion", {})
    forms = conversion.get("forms", [])
    ctas = conversion.get("ctas", [])

    funnel_types = {
        bool(forms): "lead-gen",
        not bool(forms) and bool(ctas): "click-through",
    }
    detected_type = funnel_types.get(True, "content")

    result = {
        "command": "funnel",
        "url": url,
        "status": raw.get("status", "unknown"),
        "funnel_type": detected_type,
        "conversion_elements": {
            "ctas": ctas,
            "forms": forms,
            "buttons": conversion.get("buttons", []),
        },
        "friction_points": [
            "Multiple competing CTAs can confuse visitors — test single CTA pages",
            "Form fields > 3 typically reduce conversions by 30–50%",
            "No urgency or scarcity signals detected",
        ] if not forms else [
            "Form detected — ensure it loads fast and is mobile-friendly",
            "Test auto-fill compatibility",
            "Add trust seals near form submit button",
        ],
        "funnel_metrics_targets": {
            "visitor_to_lead": "2–5% (lead gen) / 1–3% (content)",
            "lead_to_mql": "20–40%",
            "mql_to_customer": "5–15%",
        },
        "recommendations": [
            "Map your full funnel: Awareness → Consideration → Decision",
            "Identify the biggest drop-off point and fix it first",
            "Add exit-intent popup to capture leaving visitors",
            "Implement retargeting pixel immediately",
        ],
        "errors": [raw["error"]] if "error" in raw else [],
    }
    _SESSION.current_url = url
    _SESSION.push_history("funnel", url, f"Funnel type: {detected_type}")
    if save:
        result["saved_to"] = export_markdown(result, _SESSION.output_dir)
    _out(ctx, result)


# ---------------------------------------------------------------------------
# session commands
# ---------------------------------------------------------------------------

@cli.group()
def session() -> None:
    """Manage CLI session state."""


@session.command("show")
@click.pass_context
def session_show(ctx: click.Context) -> None:
    """Show current session state."""
    data = _SESSION.to_dict()
    data["command"] = "session-show"
    data["status"] = "ok"
    _out(ctx, data)


@session.command("clear")
def session_clear() -> None:
    """Clear session state."""
    _SESSION.clear()
    click.echo("Session cleared.")


# ---------------------------------------------------------------------------
# REPL
# ---------------------------------------------------------------------------

class MarketingREPL(cmd.Cmd):
    intro = (
        "\n  cli-anything-aimarketing REPL\n"
        "  Type 'help' for commands. 'quit' to exit.\n"
    )
    prompt = "marketing> "

    def _run(self, args: str) -> None:
        if not args.strip():
            return
        parts = args.strip().split()
        argv = ["cli-anything-aimarketing"] + parts
        try:
            from click.testing import CliRunner
            runner = CliRunner(mix_stderr=False)
            result = runner.invoke(cli, parts, catch_exceptions=False)
            click.echo(result.output, nl=False)
        except Exception as exc:
            click.echo(f"Error: {exc}")

    def do_audit(self, args: str) -> None:
        """audit <url> [--save] — Full marketing audit"""
        self._run(f"audit {args}")

    def do_quick(self, args: str) -> None:
        """quick <url> — 60-second snapshot"""
        self._run(f"quick {args}")

    def do_copy(self, args: str) -> None:
        """copy <url> — Copy analysis"""
        self._run(f"copy {args}")

    def do_emails(self, args: str) -> None:
        """emails <topic> [--type welcome|nurture|launch|...] — Email sequence"""
        self._run(f"emails {args}")

    def do_social(self, args: str) -> None:
        """social <topic> [--platform LinkedIn] [--days 30] — Social calendar"""
        self._run(f"social {args}")

    def do_competitors(self, args: str) -> None:
        """competitors <url1> [url2 ...] — Competitor analysis"""
        self._run(f"competitors {args}")

    def do_seo(self, args: str) -> None:
        """seo <url> — SEO audit"""
        self._run(f"seo {args}")

    def do_brand(self, args: str) -> None:
        """brand <url> — Brand voice analysis"""
        self._run(f"brand {args}")

    def do_report(self, args: str) -> None:
        """report <url> — Save Markdown report"""
        self._run(f"report {args}")

    def do_session(self, args: str) -> None:
        """session show|clear — Manage session"""
        self._run(f"session {args}")

    def do_quit(self, _: str) -> bool:
        click.echo("Goodbye.")
        return True

    def do_exit(self, args: str) -> bool:
        return self.do_quit(args)

    def do_EOF(self, args: str) -> bool:  # noqa: N802
        click.echo("")
        return self.do_quit(args)


@cli.command()
def repl() -> None:
    """Start an interactive REPL session."""
    MarketingREPL().cmdloop()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    cli(obj={})


if __name__ == "__main__":
    main()
