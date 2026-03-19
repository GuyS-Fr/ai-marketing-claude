"""Marketing audit — 6-dimension scored analysis of a webpage."""

from typing import Any, Dict, List, Optional

from cli_anything.aimarketing.utils.scraper import fetch_page_analysis

# Dimension weights (must sum to 1.0)
WEIGHTS = {
    "content": 0.25,
    "conversion": 0.20,
    "seo": 0.20,
    "competitive": 0.15,
    "brand": 0.10,
    "growth": 0.10,
}

GRADE_THRESHOLDS = [(85, "A"), (70, "B"), (55, "C"), (40, "D"), (0, "F")]


def _grade(score: float) -> str:
    for threshold, grade in GRADE_THRESHOLDS:
        if score >= threshold:
            return grade
    return "F"


def _score_seo(analysis: Dict) -> float:
    seo = analysis.get("seo", {})
    scores = analysis.get("scores", {})
    base = scores.get("seo", 0) * 10  # raw score 0-10 → 0-100
    title = 10 if seo.get("title") else 0
    meta = 10 if seo.get("meta_description") else 0
    h1 = 10 if seo.get("headings", {}).get("h1") else 0
    og = 5 if seo.get("og_tags") else 0
    if base > 0:
        return min(100, base)
    return min(100, title + meta + h1 + og + 30)


def _score_content(analysis: Dict) -> float:
    content = analysis.get("content", {})
    seo = analysis.get("seo", {})
    word_count = content.get("word_count", 0)
    headings = content.get("headings_count", 0)
    h1_count = len(seo.get("headings", {}).get("h1", []))
    score = 0
    score += min(30, word_count // 20)
    score += min(20, headings * 2)
    score += 20 if h1_count == 1 else 0
    score += 10 if seo.get("title") else 0
    score += 10 if seo.get("meta_description") else 0
    return min(100, score + 20)


def _score_conversion(analysis: Dict) -> float:
    conversion = analysis.get("conversion", {})
    scores = analysis.get("scores", {})
    cta_raw = scores.get("cta", 0) * 10
    ctas = len(conversion.get("ctas", []))
    forms = len(conversion.get("forms", []))
    buttons = len(conversion.get("buttons", []))
    if cta_raw > 0:
        return min(100, cta_raw)
    score = 0
    score += min(40, ctas * 10)
    score += min(20, forms * 10)
    score += min(20, buttons * 5)
    score += 20  # baseline
    return min(100, score)


def _score_trust(analysis: Dict) -> float:
    trust = analysis.get("trust", {})
    tracking = analysis.get("tracking", {})
    scores = analysis.get("scores", {})
    trust_raw = scores.get("trust", 0) * 10
    if trust_raw > 0:
        return min(100, trust_raw)
    social_count = trust.get("social_link_count", 0)
    tracking_count = len(tracking.get("tools_detected", []))
    schema = len(tracking.get("schema_types", []))
    score = min(40, social_count * 8) + min(30, tracking_count * 10) + min(20, schema * 10) + 20
    return min(100, score)


def _estimate_revenue_impact(scores: Dict[str, float], traffic: int = 5000) -> Dict[str, Any]:
    """Rough revenue impact estimate based on scoring gaps."""
    avg = sum(scores.values()) / len(scores)
    gap = max(0, 85 - avg)
    conversion_lift = gap * 0.003  # 0.3% lift per 10 score points
    aov = 97  # assumed average order value
    monthly_impact = traffic * conversion_lift * aov
    return {
        "assumed_monthly_visitors": traffic,
        "estimated_conversion_lift_pct": round(conversion_lift * 100, 2),
        "estimated_monthly_revenue_impact_usd": round(monthly_impact, 0),
        "confidence": "medium" if avg > 40 else "low",
    }


def _generate_recommendations(analysis: Dict, scores: Dict[str, float]) -> List[str]:
    recs = []
    seo = analysis.get("seo", {})
    content = analysis.get("content", {})
    conversion = analysis.get("conversion", {})
    tracking = analysis.get("tracking", {})

    if scores.get("seo", 100) < 70:
        if not seo.get("meta_description"):
            recs.append("Add a compelling meta description (150–160 chars) to improve CTR from search.")
        if not seo.get("headings", {}).get("h1"):
            recs.append("Add a clear H1 tag that includes your primary keyword.")
        if not seo.get("og_tags"):
            recs.append("Add Open Graph tags to improve social sharing appearance.")

    if scores.get("content", 100) < 70:
        wc = content.get("word_count", 0)
        if wc < 300:
            recs.append(f"Increase page content (currently ~{wc} words). Aim for 500+ for landing pages.")
        if not seo.get("title"):
            recs.append("Add a descriptive <title> tag that matches user intent.")

    if scores.get("conversion", 100) < 70:
        ctas = conversion.get("ctas", [])
        if len(ctas) < 2:
            recs.append("Add at least 2 clear CTAs above and below the fold.")
        if not conversion.get("forms"):
            recs.append("Consider adding a lead capture form to convert traffic.")

    if scores.get("brand", 100) < 70:
        if not tracking.get("tools_detected"):
            recs.append("Install analytics (Google Analytics or equivalent) to measure performance.")

    if not recs:
        recs.append("Marketing fundamentals look solid — focus on A/B testing headlines and CTAs.")

    return recs[:8]


def run_audit(url: str) -> Dict[str, Any]:
    """Full marketing audit of a URL. Returns structured result dict."""
    raw = fetch_page_analysis(url)
    analysis = raw.get("analysis", {})

    dim_scores = {
        "seo": _score_seo(analysis),
        "content": _score_content(analysis),
        "conversion": _score_conversion(analysis),
        "brand": _score_trust(analysis),
        "competitive": 50.0,  # requires separate competitor scan
        "growth": 50.0,       # requires separate growth analysis
    }

    overall = sum(dim_scores[k] * WEIGHTS[k] for k in WEIGHTS)
    overall = round(overall, 1)

    recommendations = _generate_recommendations(analysis, dim_scores)
    revenue_impact = _estimate_revenue_impact(dim_scores)

    return {
        "command": "audit",
        "url": url,
        "status": raw.get("status", "unknown"),
        "scores": {
            "overall": overall,
            "grade": _grade(overall),
            **{k: round(v, 1) for k, v in dim_scores.items()},
        },
        "analysis": analysis,
        "recommendations": recommendations,
        "revenue_impact": revenue_impact,
        "errors": [raw["error"]] if "error" in raw else [],
    }


def run_quick(url: str) -> Dict[str, Any]:
    """60-second snapshot — lighter version of full audit."""
    result = run_audit(url)
    return {
        "command": "quick",
        "url": url,
        "status": result["status"],
        "scores": result["scores"],
        "top_3_actions": result["recommendations"][:3],
        "errors": result["errors"],
    }
