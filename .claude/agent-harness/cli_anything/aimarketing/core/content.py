"""Content & copy analysis — headline audit, copy frameworks, suggestions."""

from typing import Any, Dict, List, Optional

from cli_anything.aimarketing.utils.scraper import fetch_page_analysis

# Copywriting frameworks
FRAMEWORKS = ["PAS", "AIDA", "Before-After-Bridge", "4U"]

# Common weak words that dilute copy
WEAK_WORDS = {
    "solutions", "leverage", "synergy", "holistic", "innovative",
    "cutting-edge", "world-class", "best-in-class", "seamlessly",
    "robust", "scalable", "empower", "utilize", "paradigm",
}


def _evaluate_headline(headline: str) -> Dict[str, Any]:
    """Score a single headline on clarity, specificity, and impact."""
    if not headline:
        return {"headline": "", "score": 0, "issues": ["Missing headline"]}

    words = headline.lower().split()
    score = 50  # baseline
    issues = []
    strengths = []

    if len(words) < 4:
        issues.append("Too short — add more specificity")
        score -= 10
    elif len(words) > 12:
        issues.append("Too long — trim to 6–12 words for impact")
        score -= 5

    weak = [w for w in words if w in WEAK_WORDS]
    if weak:
        issues.append(f"Weak jargon detected: {', '.join(weak)}")
        score -= 10 * len(weak)
    else:
        strengths.append("No jargon detected")
        score += 10

    # Numbers boost specificity
    has_number = any(c.isdigit() for c in headline)
    if has_number:
        strengths.append("Contains specific number — good for credibility")
        score += 15

    # Question hooks
    if headline.strip().endswith("?"):
        strengths.append("Question format engages curiosity")
        score += 10

    # Power words (sample)
    power = {"free", "proven", "guaranteed", "instant", "secret", "new", "exclusive", "limited"}
    found_power = [w for w in words if w in power]
    if found_power:
        strengths.append(f"Power words: {', '.join(found_power)}")
        score += 5 * len(found_power)

    return {
        "headline": headline,
        "score": min(100, max(0, score)),
        "word_count": len(words),
        "issues": issues,
        "strengths": strengths,
    }


def _generate_rewrites(headline: str, framework: str) -> str:
    """Return a rewrite instruction for the given framework."""
    templates = {
        "PAS": f"[Problem] Does your [audience] struggle with X? [Agitate] Without [solution], you'll keep [pain]. [Solve] → {headline!r} rewritten as: 'Stop [pain]. [Benefit] in [timeframe].'",
        "AIDA": f"[A] Attention hook | [I] Establish problem | [D] Present {headline!r} as the desire | [A] CTA",
        "Before-After-Bridge": f"Before: [pain state] → After: [desired state] → Bridge: how {headline!r} gets them there",
        "4U": f"Make {headline!r} Useful, Ultra-specific, Unique, and Urgent — e.g., 'Get [specific result] in [timeframe] — [limited offer]'",
    }
    return templates.get(framework, f"Rewrite '{headline}' using {framework}")


def analyze_copy(url: str) -> Dict[str, Any]:
    """Fetch page, audit headlines and CTAs, return copy analysis."""
    raw = fetch_page_analysis(url)
    analysis = raw.get("analysis", {})
    seo = analysis.get("seo", {})
    conversion = analysis.get("conversion", {})

    headlines = []
    title = seo.get("title", "")
    if title:
        headlines.append(title)
    for h in seo.get("headings", {}).get("h1", []):
        headlines.append(h)
    for h in seo.get("headings", {}).get("h2", [])[:3]:
        headlines.append(h)

    evaluated = [_evaluate_headline(h) for h in headlines if h]
    avg_score = (
        sum(e["score"] for e in evaluated) / len(evaluated)
        if evaluated else 0.0
    )

    suggestions = []
    for fw in FRAMEWORKS:
        if evaluated:
            suggestions.append({
                "framework": fw,
                "rewrite_guide": _generate_rewrites(evaluated[0]["headline"], fw),
            })

    ctas = conversion.get("ctas", [])
    cta_issues = []
    if not ctas:
        cta_issues.append("No clear CTAs detected — add action-oriented buttons")
    elif len(ctas) < 2:
        cta_issues.append("Only 1 CTA found — add a secondary CTA below the fold")

    return {
        "command": "copy",
        "url": url,
        "status": raw.get("status", "unknown"),
        "copy_score": round(avg_score, 1),
        "headlines_analyzed": evaluated,
        "ctas_found": ctas,
        "cta_issues": cta_issues,
        "rewrite_frameworks": suggestions,
        "quick_wins": [
            "Test a number in your headline (e.g., '3 ways to...' or '47% faster')",
            "Replace 'solutions' with a specific benefit",
            "Add urgency word to primary CTA (e.g., 'Get started free — today only')",
        ],
        "errors": [raw["error"]] if "error" in raw else [],
    }


def generate_copy(topic: str, framework: str = "PAS", audience: str = "business owners") -> Dict[str, Any]:
    """Generate copy elements for a given topic without fetching a URL."""
    headline_templates = {
        "PAS": [
            f"Are You Losing Revenue Because of [X]?",
            f"Stop [Problem]. Start [Solution] — {topic}",
            f"The {topic} Fix That [Target] Have Been Waiting For",
        ],
        "AIDA": [
            f"Introducing {topic}: The [Benefit] You Didn't Know You Needed",
            f"[Attention-grabbing stat] — Here's How {topic} Changes Everything",
        ],
        "Before-After-Bridge": [
            f"Before {topic}: [Pain]. After: [Transformation].",
            f"What if {topic} could [desired outcome] in [timeframe]?",
        ],
        "4U": [
            f"Get [Specific Result] with {topic} — Guaranteed in 30 Days",
            f"The Proven {topic} System Used by [Social Proof Number] {audience}",
        ],
    }
    return {
        "command": "generate-copy",
        "topic": topic,
        "framework": framework,
        "audience": audience,
        "headline_templates": headline_templates.get(framework, headline_templates["PAS"]),
        "cta_templates": [
            f"Start {topic} Free →",
            f"Get My [Benefit] Now",
            f"Yes, I Want [Result] →",
            f"Claim Your Free [Offer] →",
        ],
        "email_subject_lines": [
            f"You're missing out on {topic}...",
            f"[First name], here's your {topic} plan",
            f"The {topic} secret top {audience} use",
        ],
    }
