# AIMARKETING — CLI Harness SOP

## Software Overview

`ai-marketing-claude` is a multi-skill marketing analysis and content generation system. It audits websites, generates copy, email sequences, social calendars, competitor reports, and produces client-ready PDF reports.

## CLI Command

```bash
cli-anything-aimarketing [OPTIONS] COMMAND [ARGS]
```

## Command Reference

| Command | Input | Output | Description |
|---------|-------|--------|-------------|
| `audit <url>` | URL | Score + recommendations | Full 6-dimension marketing audit |
| `quick <url>` | URL | Snapshot scores | 60-second marketing snapshot |
| `copy <url>` | URL | Copy suggestions | Headline and copy optimization |
| `emails <topic>` | Topic/URL | Email sequence | Multi-email sequence generator |
| `social <topic>` | Topic/URL | 30-day calendar | Social media content calendar |
| `ads <url>` | URL | Ad campaigns | Multi-platform ad generation |
| `funnel <url>` | URL | Funnel analysis | Sales funnel evaluation |
| `competitors <url>` | URL | Competitor report | Competitive intelligence |
| `landing <url>` | URL | CRO analysis | Landing page optimization |
| `launch <product>` | Product name | Launch playbook | Product launch plan |
| `proposal <client>` | Client name | Proposal | Client proposal generator |
| `report <url>` | URL | Markdown report | Full markdown marketing report |
| `pdf <url>` | URL | PDF file | Professional PDF report |
| `seo <url>` | URL | SEO audit | Technical SEO analysis |
| `brand <url>` | URL | Brand guide | Brand voice analysis |
| `repl` | — | Interactive | REPL session |
| `session show` | — | Session state | Show current session |
| `session clear` | — | — | Clear session state |

## JSON Output Mode

Add `--json` flag to any command for machine-readable JSON output:

```bash
cli-anything-aimarketing --json audit https://example.com
```

JSON schema:
```json
{
  "command": "audit",
  "url": "https://example.com",
  "status": "success",
  "data": { ... },
  "scores": {
    "overall": 72,
    "content": 75,
    "conversion": 68,
    "seo": 71,
    "competitive": 65,
    "brand": 80,
    "growth": 73
  },
  "recommendations": [],
  "errors": []
}
```

## Scoring System

| Dimension | Weight | Description |
|-----------|--------|-------------|
| Content & Messaging | 25% | Headline clarity, value proposition, copy persuasion |
| Conversion Optimization | 20% | CTAs, social proof, friction, trust signals |
| SEO & Discoverability | 20% | Title, meta, headers, mobile, schema markup |
| Competitive Positioning | 15% | Differentiation, market positioning |
| Brand & Trust | 10% | Consistency, authority signals |
| Growth & Strategy | 10% | Acquisition channels, pricing strategy |

| Score | Grade | Interpretation |
|-------|-------|----------------|
| 85–100 | A | Excellent — optimize and scale |
| 70–84 | B | Good — targeted improvements needed |
| 55–69 | C | Average — significant gaps exist |
| 40–54 | D | Below average — rebuild key areas |
| 0–39 | F | Critical — requires urgent overhaul |

## Session State

The harness maintains a session in `~/.cli_anything_aimarketing_session.json`:
- Current URL under analysis
- Cached audit results
- Output directory (default: `./marketing-output/`)
- Analysis history (last 10 analyses)

## Typical Agent Workflow

```bash
# 1. Full audit
cli-anything-aimarketing --json audit https://example.com

# 2. Deep copy analysis
cli-anything-aimarketing --json copy https://example.com

# 3. Generate email sequence from audit context
cli-anything-aimarketing --json emails "SaaS onboarding"

# 4. Generate social calendar
cli-anything-aimarketing --json social "productivity software"

# 5. Export full PDF report
cli-anything-aimarketing --json pdf https://example.com

# 6. Check session
cli-anything-aimarketing session show
```

## Architecture Notes

- All Python scripts in `../../scripts/` are reused: `analyze_page.py`, `competitor_scanner.py`, `social_calendar.py`, `generate_pdf_report.py`
- Core modules wrap script logic with clean APIs
- No external API dependencies — uses `urllib` + `html.parser` + `reportlab`
- REPL uses `cmd.Cmd` for interactive sessions
- JSON mode outputs to stdout, human mode outputs formatted terminal text
