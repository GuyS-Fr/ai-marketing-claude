# cli-anything-aimarketing

CLI harness for [ai-marketing-claude](https://github.com/zubair-trabzada/ai-marketing-claude) — AI-powered marketing analysis, copy generation, and content automation.

## Installation

```bash
cd ai-marketing-claude/agent-harness
pip install -e .
```

Verify:
```bash
cli-anything-aimarketing --help
which cli-anything-aimarketing
```

PDF report support (optional):
```bash
pip install reportlab
```

## Commands

### Marketing Audit
```bash
# Full 6-dimension audit
cli-anything-aimarketing audit https://example.com

# 60-second snapshot
cli-anything-aimarketing quick https://example.com

# Save report to file
cli-anything-aimarketing audit https://example.com --save
```

### Copy & Content
```bash
# Analyze and optimize page copy
cli-anything-aimarketing copy https://example.com

# SEO technical audit
cli-anything-aimarketing seo https://example.com

# Landing page CRO analysis
cli-anything-aimarketing landing https://example.com

# Brand voice analysis
cli-anything-aimarketing brand https://example.com
```

### Email Sequences
```bash
# Welcome sequence (default)
cli-anything-aimarketing emails "SaaS onboarding"

# Specific sequence types
cli-anything-aimarketing emails "product launch" --type launch
cli-anything-aimarketing emails "lead nurture" --type nurture --audience "marketing managers"

# Available types: welcome, nurture, launch, cart-abandonment, cold-outreach, onboarding, re-engagement
```

### Social Calendar
```bash
# 30-day LinkedIn calendar (default)
cli-anything-aimarketing social "productivity software"

# Platform-specific
cli-anything-aimarketing social "AI tools" --platform Instagram --days 14
cli-anything-aimarketing social "B2B SaaS" --platform "Twitter/X" --audience "startup founders"
```

### Competitor Analysis
```bash
cli-anything-aimarketing competitors https://competitor1.com https://competitor2.com
cli-anything-aimarketing competitors https://comp.com --main-url https://yoursite.com
```

### Ad Campaigns
```bash
cli-anything-aimarketing ads https://example.com
cli-anything-aimarketing ads https://example.com --platform Meta
```

### Funnel Analysis
```bash
cli-anything-aimarketing funnel https://example.com
```

### Launch & Proposals
```bash
cli-anything-aimarketing launch "My SaaS Product" --audience "freelancers"
cli-anything-aimarketing proposal "Acme Corp" --service "full marketing audit"
```

### Reports
```bash
# Markdown report (saved to ./marketing-output/)
cli-anything-aimarketing report https://example.com

# Professional PDF
cli-anything-aimarketing pdf https://example.com
```

## JSON Output Mode

Add `--json` to any command for machine-readable output:

```bash
cli-anything-aimarketing --json audit https://example.com
cli-anything-aimarketing --json emails "SaaS" --type welcome
cli-anything-aimarketing --json social "marketing" | jq '.scores'
```

## REPL Mode

```bash
cli-anything-aimarketing repl

marketing> audit https://example.com
marketing> emails "product launch" --type launch
marketing> session show
marketing> quit
```

## Session Management

```bash
cli-anything-aimarketing session show
cli-anything-aimarketing session clear
cli-anything-aimarketing --output-dir ./reports audit https://example.com
```

## Output Files

All `--save` commands and `report`/`pdf` commands write to `./marketing-output/` (configurable with `--output-dir`):

| File Pattern | Command |
|-------------|---------|
| `MARKETING-AUDIT-*.md` | audit --save, report |
| `MARKETING-EMAILS-*.md` | emails --save |
| `MARKETING-SOCIAL-*.md` | social --save |
| `MARKETING-COMPETITORS-*.md` | competitors --save |
| `MARKETING-REPORT-*.pdf` | pdf |
| `marketing-*.json` | export_json() |

## Architecture

```
cli_anything/aimarketing/
├── aimarketing_cli.py      # Click CLI entry point + REPL
├── core/
│   ├── session.py          # Persistent session state
│   ├── audit.py            # 6-dimension marketing audit
│   ├── content.py          # Copy analysis and generation
│   ├── email_gen.py        # Email sequence generator
│   ├── social.py           # Social calendar generator
│   ├── competitor.py       # Competitor intelligence
│   └── export.py           # Markdown / PDF / JSON export
└── utils/
    └── scraper.py          # Web scraping (wraps analyze_page.py + competitor_scanner.py)
```

## Running Tests

```bash
cd agent-harness

# Unit tests (no network required)
pytest cli_anything/aimarketing/tests/test_core.py -v

# E2E tests (requires network)
pytest cli_anything/aimarketing/tests/test_full_e2e.py -v

# Subprocess tests (requires installed CLI)
CLI_ANYTHING_FORCE_INSTALLED=1 pytest cli_anything/aimarketing/tests/test_full_e2e.py -v -k "Subprocess"

# All tests
pytest cli_anything/aimarketing/tests/ -v --tb=short
```

## Scoring System

| Score | Grade | Action |
|-------|-------|--------|
| 85–100 | A | Optimize and scale |
| 70–84 | B | Targeted improvements |
| 55–69 | C | Significant gaps |
| 40–54 | D | Rebuild key areas |
| 0–39 | F | Urgent overhaul |
