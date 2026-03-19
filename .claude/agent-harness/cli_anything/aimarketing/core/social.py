"""Social media calendar generator — 30-day content calendar with hooks and hashtags."""

from typing import Any, Dict, List, Optional

PLATFORMS = ["LinkedIn", "Twitter/X", "Instagram", "TikTok", "YouTube"]

CONTENT_PILLARS = [
    {"name": "Educational", "weight": 0.40, "description": "Teach your audience something valuable"},
    {"name": "Behind-the-Scenes", "weight": 0.20, "description": "Show your process and people"},
    {"name": "Social Proof", "weight": 0.15, "description": "Testimonials, case studies, results"},
    {"name": "Engagement", "weight": 0.15, "description": "Questions, polls, conversations"},
    {"name": "Promotional", "weight": 0.10, "description": "Offers, products, services"},
]

HOOK_TEMPLATES = {
    "LinkedIn": [
        "I made a mistake that cost me [X]. Here's what I learned:",
        "Unpopular opinion: [contrarian view]",
        "[Number] things I wish I knew before [topic]:",
        "After [X years/time] in [industry], here's what actually works:",
        "Most [audience] get [topic] wrong. Here's why:",
    ],
    "Twitter/X": [
        "Hot take: [contrarian view]",
        "Thread: [number] lessons from [topic] 🧵",
        "Nobody talks about this, but [insight]",
        "PSA for [audience]:",
        "If you only do one thing for [topic], do this:",
    ],
    "Instagram": [
        "Save this if you want to [outcome] ↓",
        "The [topic] formula nobody shares:",
        "POV: You finally figured out [topic]",
        "Swipe to see the before/after →",
        "Stop doing this with [topic] 🚫",
    ],
    "TikTok": [
        "POV: You discover the [topic] hack",
        "Things [audience] don't tell you about [topic]",
        "Wait for it... [topic] revealed",
        "Day [X] of [challenge/journey]",
        "I tried [topic] for 30 days. Here's what happened:",
    ],
    "YouTube": [
        "I tested [topic] for [timeframe] — results shocked me",
        "The truth about [topic] (nobody tells you this)",
        "How I went from [before] to [after] with [topic]",
        "Step-by-step [topic] for beginners in [timeframe]",
        "[Number] [topic] mistakes to avoid in [year]",
    ],
}

HASHTAG_TIERS = {
    "niche": ["#[specifictopic]", "#[nicheaudience]", "#[industryterm]"],
    "medium": ["#marketing", "#business", "#entrepreneur", "#growthhacking"],
    "broad": ["#success", "#motivation", "#tips", "#howto"],
    "branded": ["#[yourbrand]", "#[yourproduct]"],
}


def _pillar_for_day(day: int) -> str:
    """Assign content pillar based on day number using weighted distribution."""
    # 30-day weighted distribution: 12 edu, 6 bts, 4-5 social proof, 4-5 engagement, 3-4 promo
    pillar_map = {
        1: "Educational", 2: "Educational", 3: "Behind-the-Scenes",
        4: "Social Proof", 5: "Educational", 6: "Engagement",
        7: "Educational", 8: "Educational", 9: "Promotional",
        10: "Behind-the-Scenes", 11: "Educational", 12: "Social Proof",
        13: "Engagement", 14: "Educational", 15: "Educational",
        16: "Behind-the-Scenes", 17: "Social Proof", 18: "Educational",
        19: "Engagement", 20: "Educational", 21: "Promotional",
        22: "Behind-the-Scenes", 23: "Educational", 24: "Social Proof",
        25: "Engagement", 26: "Educational", 27: "Educational",
        28: "Promotional", 29: "Behind-the-Scenes", 30: "Educational",
    }
    return pillar_map.get(day, "Educational")


def _post_for_day(day: int, topic: str, audience: str, platform: str) -> Dict[str, Any]:
    pillar = _pillar_for_day(day)
    hooks = HOOK_TEMPLATES.get(platform, HOOK_TEMPLATES["LinkedIn"])
    hook = hooks[(day - 1) % len(hooks)]
    hook = hook.replace("[topic]", topic).replace("[audience]", audience)

    caption_templates = {
        "Educational": f"Here's what every {audience} needs to know about {topic}. [3 key points] Save this for later.",
        "Behind-the-Scenes": f"A look inside how we approach {topic}. [Process detail] What questions do you have?",
        "Social Proof": f"[Client/customer name] achieved [result] using {topic}. Here's how: [brief story] DM for details.",
        "Engagement": f"What's your biggest challenge with {topic}? Reply below — I read every response.",
        "Promotional": f"If you're serious about {topic}, [product/service] is open. [Key benefit]. Link in bio / comments.",
    }

    return {
        "day": day,
        "pillar": pillar,
        "platform": platform,
        "hook": hook,
        "caption": caption_templates.get(pillar, caption_templates["Educational"]),
        "hashtags": {
            "niche": HASHTAG_TIERS["niche"],
            "medium": HASHTAG_TIERS["medium"][:2],
            "branded": HASHTAG_TIERS["branded"],
        },
        "visual_spec": _visual_spec(pillar, platform),
        "best_time": _best_time(platform, day),
    }


def _visual_spec(pillar: str, platform: str) -> str:
    specs = {
        "Educational": "Carousel (5–7 slides) or infographic — clean design, 1 idea per slide",
        "Behind-the-Scenes": "Authentic photo or short video — raw, real, unpolished is fine",
        "Social Proof": "Quote card with customer photo + result metric",
        "Engagement": "Bold question text on solid background, or selfie-style video",
        "Promotional": "Product/service screenshot or result visualization, clear CTA overlay",
    }
    return specs.get(pillar, "Image with caption overlay")


def _best_time(platform: str, day: int) -> str:
    times = {
        "LinkedIn": "Tue–Thu 8–10am or 5–6pm (local)",
        "Twitter/X": "Mon–Fri 9am or 12–1pm (local)",
        "Instagram": "Mon/Wed/Fri 11am–1pm or 7–9pm",
        "TikTok": "Tue/Thu/Fri 7–9pm (local)",
        "YouTube": "Sat–Sun 12–4pm (subscribers' local timezone)",
    }
    return times.get(platform, "Check your analytics for peak engagement time")


def generate_social_calendar(
    topic: str,
    audience: str = "entrepreneurs",
    platform: str = "LinkedIn",
    days: int = 30,
) -> Dict[str, Any]:
    """Generate a 30-day social media content calendar."""
    if platform not in PLATFORMS:
        platform = "LinkedIn"

    posts = [_post_for_day(d, topic, audience, platform) for d in range(1, days + 1)]

    pillar_counts = {}
    for p in posts:
        pillar_counts[p["pillar"]] = pillar_counts.get(p["pillar"], 0) + 1

    return {
        "command": "social",
        "topic": topic,
        "audience": audience,
        "platform": platform,
        "duration_days": days,
        "content_pillars": CONTENT_PILLARS,
        "pillar_distribution": pillar_counts,
        "calendar": posts,
        "repurposing_strategy": [
            f"LinkedIn carousel → Instagram slides (resize to 1:1)",
            f"Long-form LinkedIn post → Twitter thread",
            f"TikTok → YouTube Short → Instagram Reel (same video)",
            f"Blog post → 5 LinkedIn posts → 10 tweets",
        ],
        "engagement_playbook": [
            "Reply to every comment within 2 hours of posting",
            "Engage with 5 accounts in your niche before posting",
            "DM everyone who comments on promotional posts",
            "Repost best-performing content at 90 days",
        ],
    }
