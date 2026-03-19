"""Email sequence generator — produces multi-email sequences for common marketing scenarios."""

from typing import Any, Dict, List, Optional

SEQUENCE_TYPES = [
    "welcome", "nurture", "launch", "cart-abandonment",
    "cold-outreach", "onboarding", "re-engagement",
]

_SEQUENCE_CONFIGS = {
    "welcome": {
        "emails": 5,
        "duration_days": 8,
        "goal": "Onboard new subscribers and deliver a quick win",
        "open_rate_benchmark": "45–60%",
        "schedule": [0, 2, 4, 6, 8],
        "subjects": [
            "Welcome! Here's your first quick win",
            "The #1 mistake [audience] make (and how to fix it)",
            "[First name], here's what's working right now",
            "A quick story about [transformation]",
            "Your next step — what do you need most?",
        ],
        "email_goals": [
            "Deliver quick win / lead magnet",
            "Educate on core problem",
            "Show social proof + what's possible",
            "Handle top objection via story",
            "Soft pitch + segment by interest",
        ],
    },
    "nurture": {
        "emails": 6,
        "duration_days": 14,
        "goal": "Move leads from awareness to consideration",
        "open_rate_benchmark": "25–40%",
        "schedule": [0, 2, 4, 7, 10, 14],
        "subjects": [
            "How [customer name] achieved [result]",
            "The framework behind [topic]",
            "Why [common approach] fails (and what to do instead)",
            "[Topic]: The data might surprise you",
            "Ready for the next level with [topic]?",
            "Last chance to [action] before [deadline]",
        ],
        "email_goals": [
            "Case study — build credibility",
            "Educational framework — position as authority",
            "Myth-busting — overcome objections",
            "Data/research — establish thought leadership",
            "Transition to offer",
            "Urgency close",
        ],
    },
    "launch": {
        "emails": 8,
        "duration_days": 10,
        "goal": "Drive maximum sales during product launch window",
        "open_rate_benchmark": "30–50%",
        "schedule": [-7, -5, -3, -1, 0, 1, 3, 0],
        "subjects": [
            "Something exciting is coming...",
            "Sneak peek inside [product]",
            "[First name], doors open in 48 hours",
            "Last chance to join the waitlist",
            "🚀 We're LIVE — [product] is now available",
            "Have you seen what's inside [product]?",
            "Only [X] spots remaining",
            "Final hours — [product] closes tonight",
        ],
        "email_goals": [
            "Tease announcement",
            "Show transformation / behind-the-scenes",
            "Build urgency — 48h countdown",
            "Waitlist / early bird close",
            "Cart open announcement",
            "Feature deep-dive + testimonials",
            "Scarcity push",
            "Cart close",
        ],
    },
    "cold-outreach": {
        "emails": 5,
        "duration_days": 14,
        "goal": "Book discovery calls or demo requests",
        "open_rate_benchmark": "15–25%",
        "schedule": [0, 3, 7, 10, 14],
        "subjects": [
            "Quick question about [company]",
            "Idea for [company] → [specific benefit]",
            "Did you get a chance to see this?",
            "[Mutual connection / shared interest] — worth a chat?",
            "Closing the loop on [topic]",
        ],
        "email_goals": [
            "Permission-based cold open",
            "Value proposition with specific angle",
            "Follow-up with social proof",
            "Referral / shared context angle",
            "Breakup email — reverse psychology",
        ],
    },
    "onboarding": {
        "emails": 6,
        "duration_days": 14,
        "goal": "Activate new customers and drive first value moment",
        "open_rate_benchmark": "50–70%",
        "schedule": [0, 1, 3, 5, 7, 14],
        "subjects": [
            "You're in! Here's how to get started",
            "Your account is ready — first step",
            "Day 3 check-in: How's it going?",
            "Pro tip: [specific feature/action]",
            "Success story: How [customer] got results in week 1",
            "Your 2-week check-in + next steps",
        ],
        "email_goals": [
            "Activate account + set expectations",
            "Drive first key action",
            "Check engagement + offer support",
            "Teach power feature",
            "Social proof to reinforce decision",
            "Upsell / referral + expansion",
        ],
    },
}


def _build_email(
    sequence_type: str,
    email_index: int,
    config: Dict,
    topic: str,
    audience: str,
) -> Dict[str, Any]:
    subjects = config.get("subjects", [])
    goals = config.get("email_goals", [])
    schedule = config.get("schedule", [])

    subject = subjects[email_index] if email_index < len(subjects) else f"Email {email_index + 1}"
    goal = goals[email_index] if email_index < len(goals) else "Engage and convert"
    day = schedule[email_index] if email_index < len(schedule) else email_index * 2

    return {
        "number": email_index + 1,
        "send_day": f"Day {day}" if day >= 0 else f"Day {day} (pre-launch)",
        "subject": subject.replace("[topic]", topic).replace("[audience]", audience),
        "goal": goal,
        "body_structure": _body_structure(sequence_type, email_index, topic, audience),
        "ps_line": f"P.S. — If you have questions about {topic}, just reply to this email.",
        "estimated_length_words": 200 if sequence_type == "cold-outreach" else 400,
    }


def _body_structure(seq_type: str, idx: int, topic: str, audience: str) -> List[str]:
    structures = {
        "welcome": [
            ["Hook with their problem", f"Deliver quick win about {topic}", "Set expectations for sequence", "CTA: Download / action"],
            [f"The #1 mistake {audience} make", "Why it happens", "The fix", "CTA: Reply / engage"],
            ["Social proof story", "Key lesson", f"How {topic} bridges the gap", "Soft CTA"],
            ["Personal story about transformation", "Lesson learned", "Bridge to reader's situation", "CTA: Next step"],
            ["Gratitude + recap", "Segment question", "Offer teaser", "Reply CTA"],
        ],
        "launch": [
            ["Tease — something is coming", "Build curiosity", "No details yet", "Waitlist CTA"],
            ["Behind-the-scenes look", "Problem statement", "Solution preview", "Early access CTA"],
        ],
    }
    default = [
        [f"Open with {topic} hook", "Educate / entertain", "Make offer or ask", "CTA"],
    ]
    seq_structs = structures.get(seq_type, default)
    if idx < len(seq_structs):
        return seq_structs[idx]
    return default[0]


def generate_email_sequence(
    topic: str,
    sequence_type: str = "welcome",
    audience: str = "business owners",
    num_emails: Optional[int] = None,
) -> Dict[str, Any]:
    """Generate a complete email sequence for the given topic."""
    if sequence_type not in _SEQUENCE_CONFIGS:
        sequence_type = "welcome"

    config = _SEQUENCE_CONFIGS[sequence_type]
    n = num_emails or config["emails"]

    emails = [
        _build_email(sequence_type, i, config, topic, audience)
        for i in range(min(n, len(config.get("subjects", [""] * n))))
    ]

    return {
        "command": "emails",
        "topic": topic,
        "sequence_type": sequence_type,
        "audience": audience,
        "overview": {
            "goal": config["goal"],
            "total_emails": len(emails),
            "duration_days": config["duration_days"],
            "open_rate_benchmark": config["open_rate_benchmark"],
        },
        "emails": emails,
        "ab_test_ideas": [
            f"Test plain-text vs HTML for email 1",
            f"Test question subject line vs statement for email 2",
            f"Test emoji vs no emoji in subject lines",
        ],
        "compliance_checklist": [
            "Unsubscribe link in every email",
            "Physical address in footer",
            "Sender name matches expected from address",
            "CAN-SPAM / GDPR compliant opt-in confirmed",
        ],
    }
