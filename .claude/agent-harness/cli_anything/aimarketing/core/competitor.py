"""Competitor analysis — scan and compare competitor websites."""

from typing import Any, Dict, List, Optional

from cli_anything.aimarketing.utils.scraper import fetch_competitor_analysis, fetch_page_analysis


COMPETITOR_TIERS = ["direct", "indirect", "aspirational"]


def _swot(data: Dict) -> Dict[str, List[str]]:
    """Generate SWOT skeleton from scraped competitor data."""
    positioning = data.get("positioning", {})
    h1s = positioning.get("headline", "") if isinstance(positioning, dict) else ""
    h1s = [h1s] if h1s else data.get("h1", [])
    pricing_raw = data.get("pricing", {})
    if isinstance(pricing_raw, dict):
        pricing = pricing_raw.get("pricing_mentions", [])
    else:
        pricing = pricing_raw if isinstance(pricing_raw, list) else []
    trust_raw = data.get("trust", {})
    if isinstance(trust_raw, dict):
        social = trust_raw.get("social_platforms", [])
        testimonials = [1] if trust_raw.get("has_testimonials") else []
        trust = ["logos"] * trust_raw.get("estimated_logo_count", 0)
    else:
        social = data.get("social_links", [])
        trust = data.get("trust_signals", [])
        testimonials = data.get("testimonials", [])

    strengths = []
    weaknesses = []
    opportunities = []
    threats = []

    if h1s:
        strengths.append(f"Clear headline positioning: '{h1s[0][:60]}...' " if len(h1s[0]) > 60 else h1s[0])
    if trust:
        strengths.append(f"Trust signals present: {', '.join(trust[:3])}")
    if testimonials:
        strengths.append(f"{len(testimonials)} testimonial(s) detected")
    if pricing:
        threats.append(f"Pricing signals found: {', '.join(str(p) for p in pricing[:3])}")
    if social:
        opportunities.append("Active social presence — monitor for content angles")
    if not trust:
        weaknesses.append("Limited trust signals detected")
    if not testimonials:
        weaknesses.append("No social proof / testimonials detected")

    opportunities.append("Differentiate on [your unique angle] where they're weak")
    weaknesses = weaknesses or ["Insufficient data — manual review needed"]

    return {
        "strengths": strengths or ["Could not extract — review manually"],
        "weaknesses": weaknesses,
        "opportunities": opportunities,
        "threats": threats or ["Pricing competition possible"],
    }


def scan_competitor(url: str, tier: str = "direct") -> Dict[str, Any]:
    """Scan a single competitor URL and return structured intelligence."""
    raw = fetch_competitor_analysis(url)
    data = raw.get("data", {})
    swot = _swot(data)

    return {
        "url": url,
        "tier": tier if tier in COMPETITOR_TIERS else "direct",
        "status": raw.get("status", "unknown"),
        "positioning": {
            "primary_headline": (data.get("h1") or ["N/A"])[0],
            "sub_headlines": data.get("h2", [])[:5],
            "pricing_signals": data.get("pricing", []),
        },
        "trust_signals": data.get("trust_signals", []),
        "social_presence": data.get("social_links", []),
        "testimonials_count": len(data.get("testimonials", [])),
        "swot": swot,
        "steal_worthy": _steal_worthy(data),
        "errors": [raw["error"]] if "error" in raw else [],
    }


def _steal_worthy(data: Dict) -> List[str]:
    tactics = []
    if data.get("testimonials"):
        tactics.append("Strong social proof — add more testimonials to your site")
    if data.get("pricing"):
        tactics.append("Transparent pricing visible — consider adding/comparing pricing page")
    h2s = data.get("h2", [])
    if h2s:
        tactics.append(f"Content structure idea: section titled '{h2s[0]}'")
    if not tactics:
        tactics.append("Review their content strategy manually for differentiation ideas")
    return tactics


def scan_competitors(urls: List[str], main_url: Optional[str] = None) -> Dict[str, Any]:
    """Scan multiple competitor URLs and produce a comparison report."""
    competitors = []
    for i, url in enumerate(urls[:5]):  # max 5 competitors
        tier = COMPETITOR_TIERS[min(i, len(COMPETITOR_TIERS) - 1)]
        competitors.append(scan_competitor(url, tier))

    # Comparison matrix
    matrix = []
    for c in competitors:
        matrix.append({
            "url": c["url"],
            "tier": c["tier"],
            "headline": c["positioning"]["primary_headline"],
            "pricing_visible": bool(c["positioning"]["pricing_signals"]),
            "testimonials": c["testimonials_count"],
            "social_links": len(c["social_presence"]),
            "swot_strengths": len(c["swot"]["strengths"]),
        })

    return {
        "command": "competitors",
        "main_url": main_url,
        "competitors_scanned": len(competitors),
        "comparison_matrix": matrix,
        "competitors": competitors,
        "strategic_summary": {
            "differentiation_opportunities": _differentiation_opps(competitors),
            "common_weaknesses": _common_weaknesses(competitors),
        },
    }


def _differentiation_opps(competitors: List[Dict]) -> List[str]:
    opps = set()
    for c in competitors:
        for opp in c["swot"].get("opportunities", []):
            opps.add(opp)
    return list(opps)[:5] or ["Manual competitor analysis recommended"]


def _common_weaknesses(competitors: List[Dict]) -> List[str]:
    weak = {}
    for c in competitors:
        for w in c["swot"].get("weaknesses", []):
            weak[w] = weak.get(w, 0) + 1
    common = [w for w, count in sorted(weak.items(), key=lambda x: -x[1])]
    return common[:3] or ["No common weaknesses found with available data"]
