# Test Plan — cli-anything-aimarketing

## Test Strategy

| Layer | File | Scope |
|-------|------|-------|
| Unit | `test_core.py` | All core modules with synthetic data, no network |
| E2E | `test_full_e2e.py` | Full pipeline with real URLs |
| Subprocess | `TestCLISubprocess` in `test_full_e2e.py` | Installed CLI via PATH |

---

## Unit Tests (`test_core.py`)

### `TestSession`
- `test_defaults` — Session initializes with correct defaults
- `test_set_url` — `current_url` setter persists to disk and reloads
- `test_set_output_dir` — `output_dir` setter persists
- `test_push_history` — history capped at MAX_HISTORY (10)
- `test_clear` — clear removes session file and resets state
- `test_to_dict` — serializes all fields

### `TestAudit`
- `test_run_audit_structure` — result has keys: command, url, status, scores, recommendations, revenue_impact
- `test_scores_dimensions` — all 6 dimension scores present
- `test_overall_score_range` — overall score is 0–100
- `test_grade_mapping` — grade matches score threshold
- `test_run_quick_structure` — quick result has top_3_actions
- `test_recommendations_generated` — at least 1 recommendation produced
- `test_revenue_impact_fields` — impact has monthly_visitors, lift_pct, revenue_usd

### `TestContent`
- `test_analyze_copy_structure` — result has copy_score, headlines_analyzed, cta_issues
- `test_evaluate_headline_empty` — empty headline scores 0
- `test_evaluate_headline_good` — headline with number scores > 60
- `test_evaluate_headline_jargon` — jargon-heavy headline penalized
- `test_generate_copy_structure` — returns headline_templates, cta_templates, email_subject_lines
- `test_generate_copy_frameworks` — PAS, AIDA, Before-After-Bridge, 4U all return results

### `TestEmailGen`
- `test_welcome_sequence` — 5 emails, correct duration
- `test_nurture_sequence` — 6 emails
- `test_launch_sequence` — 8 emails
- `test_cold_outreach_sequence` — 5 emails
- `test_onboarding_sequence` — 6 emails
- `test_email_fields` — each email has: number, send_day, subject, goal, body_structure
- `test_ab_test_ideas` — ab_test_ideas list present
- `test_compliance_checklist` — compliance_checklist has 4 items
- `test_invalid_type_defaults_to_welcome` — unknown type falls back

### `TestSocial`
- `test_30_day_calendar_length` — calendar has 30 entries
- `test_pillar_distribution` — all 5 pillars represented
- `test_post_fields` — each post has: day, pillar, platform, hook, caption, best_time
- `test_platform_choice` — LinkedIn, Twitter/X, Instagram, TikTok all work
- `test_custom_days` — `days=7` returns 7-day calendar
- `test_engagement_playbook` — engagement_playbook list present
- `test_repurposing_strategy` — repurposing_strategy list present

### `TestCompetitor`
- `test_scan_competitor_structure` — result has url, tier, swot, positioning
- `test_swot_fields` — SWOT has strengths, weaknesses, opportunities, threats
- `test_scan_competitors_matrix` — comparison_matrix has one entry per URL
- `test_steal_worthy` — steal_worthy list present
- `test_tier_validation` — invalid tier defaults to 'direct'

### `TestExport`
- `test_export_markdown_creates_file` — file exists after export
- `test_export_markdown_content` — file contains URL and score
- `test_export_json_creates_file` — JSON file is valid
- `test_export_json_roundtrip` — exported JSON parses back correctly
- `test_export_pdf_requires_reportlab` — raises RuntimeError without reportlab (mocked)

---

## E2E Tests (`test_full_e2e.py`)

### `TestAuditE2E`
- `test_audit_live_url` — audit of `https://example.com` returns valid scores
- `test_audit_saves_markdown` — `--save` flag creates `.md` file
- `test_quick_live_url` — quick command completes successfully

### `TestCopyE2E`
- `test_copy_live_url` — copy analysis of `https://example.com` returns copy_score

### `TestEmailE2E`
- `test_emails_all_types` — all SEQUENCE_TYPES generate without error
- `test_emails_save_markdown` — saved file contains email subject lines

### `TestSocialE2E`
- `test_social_all_platforms` — all PLATFORMS generate without error
- `test_social_calendar_30_days` — 30-day calendar fully generated

### `TestCompetitorE2E`
- `test_competitors_live_scan` — scans `https://example.com` without crash
- `test_competitors_multi_url` — handles 2 URLs

### `TestExportE2E`
- `test_full_pipeline_to_markdown` — audit → export_markdown → file readable
- `test_full_pipeline_to_json` — audit → export_json → valid JSON

### `TestCLISubprocess`
- `test_cli_available_in_path` — `cli-anything-aimarketing --help` exits 0
- `test_audit_json_output` — `--json audit https://example.com` produces valid JSON
- `test_quick_json_output` — `--json quick https://example.com` produces valid JSON
- `test_emails_json_output` — `--json emails "SaaS onboarding"` produces valid JSON
- `test_social_json_output` — `--json social "productivity"` produces valid JSON
- `test_session_show_json` — `--json session show` produces valid JSON
- `test_session_clear` — `session clear` exits 0
- `test_repl_exits_cleanly` — `repl` with EOF input exits 0

---

## Test Results

**Run date:** 2026-03-17
**Python:** 3.12.8 | **pytest:** 9.0.2 | **Platform:** win32

```
============================= test session starts =============================
collected 66 items

test_core.py::TestSession::test_clear                            PASSED
test_core.py::TestSession::test_defaults                         PASSED
test_core.py::TestSession::test_push_history                     PASSED
test_core.py::TestSession::test_set_output_dir                   PASSED
test_core.py::TestSession::test_set_url                          PASSED
test_core.py::TestSession::test_to_dict                          PASSED
test_core.py::TestAudit::test_grade_mapping                      PASSED
test_core.py::TestAudit::test_overall_score_range                PASSED
test_core.py::TestAudit::test_recommendations_generated          PASSED
test_core.py::TestAudit::test_revenue_impact_fields              PASSED
test_core.py::TestAudit::test_run_audit_structure                PASSED
test_core.py::TestAudit::test_run_quick_structure                PASSED
test_core.py::TestAudit::test_scores_dimensions                  PASSED
test_core.py::TestContent::test_analyze_copy_structure           PASSED
test_core.py::TestContent::test_evaluate_headline_empty          PASSED
test_core.py::TestContent::test_evaluate_headline_good           PASSED
test_core.py::TestContent::test_evaluate_headline_jargon         PASSED
test_core.py::TestContent::test_generate_copy_frameworks         PASSED
test_core.py::TestContent::test_generate_copy_structure          PASSED
test_core.py::TestEmailGen::test_ab_test_ideas                   PASSED
test_core.py::TestEmailGen::test_cold_outreach_sequence          PASSED
test_core.py::TestEmailGen::test_compliance_checklist            PASSED
test_core.py::TestEmailGen::test_email_fields                    PASSED
test_core.py::TestEmailGen::test_invalid_type_defaults_to_welcome PASSED
test_core.py::TestEmailGen::test_launch_sequence                 PASSED
test_core.py::TestEmailGen::test_nurture_sequence                PASSED
test_core.py::TestEmailGen::test_onboarding_sequence             PASSED
test_core.py::TestEmailGen::test_welcome_sequence                PASSED
test_core.py::TestSocial::test_30_day_calendar_length            PASSED
test_core.py::TestSocial::test_custom_days                       PASSED
test_core.py::TestSocial::test_engagement_playbook               PASSED
test_core.py::TestSocial::test_pillar_distribution               PASSED
test_core.py::TestSocial::test_platform_choice                   PASSED
test_core.py::TestSocial::test_post_fields                       PASSED
test_core.py::TestSocial::test_repurposing_strategy              PASSED
test_core.py::TestCompetitor::test_scan_competitor_structure     PASSED
test_core.py::TestCompetitor::test_scan_competitors_matrix       PASSED
test_core.py::TestCompetitor::test_steal_worthy                  PASSED
test_core.py::TestCompetitor::test_swot_fields                   PASSED
test_core.py::TestCompetitor::test_tier_validation               PASSED
test_core.py::TestExport::test_export_json_creates_file          PASSED
test_core.py::TestExport::test_export_json_roundtrip             PASSED
test_core.py::TestExport::test_export_markdown_content           PASSED
test_core.py::TestExport::test_export_markdown_creates_file      PASSED
test_core.py::TestExport::test_export_pdf_requires_reportlab     PASSED
test_full_e2e.py::TestAuditE2E::test_audit_live_url              PASSED
test_full_e2e.py::TestAuditE2E::test_audit_saves_markdown        PASSED
test_full_e2e.py::TestAuditE2E::test_quick_live_url              PASSED
test_full_e2e.py::TestCopyE2E::test_copy_live_url                PASSED
test_full_e2e.py::TestCopyE2E::test_generate_copy_all_frameworks PASSED
test_full_e2e.py::TestEmailE2E::test_emails_all_types            PASSED
test_full_e2e.py::TestEmailE2E::test_emails_save_markdown        PASSED
test_full_e2e.py::TestSocialE2E::test_social_all_platforms       PASSED
test_full_e2e.py::TestSocialE2E::test_social_calendar_30_days    PASSED
test_full_e2e.py::TestCompetitorE2E::test_competitors_live_scan  PASSED
test_full_e2e.py::TestCompetitorE2E::test_competitors_multi_url  PASSED
test_full_e2e.py::TestExportE2E::test_full_pipeline_to_json      PASSED
test_full_e2e.py::TestExportE2E::test_full_pipeline_to_markdown  PASSED
test_full_e2e.py::TestCLISubprocess::test_audit_json_output      PASSED
test_full_e2e.py::TestCLISubprocess::test_cli_available_in_path  PASSED
test_full_e2e.py::TestCLISubprocess::test_emails_json_output     PASSED
test_full_e2e.py::TestCLISubprocess::test_quick_json_output      PASSED
test_full_e2e.py::TestCLISubprocess::test_repl_exits_cleanly     PASSED
test_full_e2e.py::TestCLISubprocess::test_session_clear          PASSED
test_full_e2e.py::TestCLISubprocess::test_session_show_json      PASSED
test_full_e2e.py::TestCLISubprocess::test_social_json_output     PASSED

======================= 66 passed in 0.77s =======================
```

**Coverage:** 66/66 tests pass (100%)
**Gaps:** None — all planned test cases implemented and passing.
