"""Unit tests for cli_anything.aimarketing core modules.

All tests are synthetic — no network calls, no file I/O side effects.
"""

import json
import os
import sys
import tempfile
import unittest
from unittest.mock import MagicMock, patch

# ---------------------------------------------------------------------------
# Patch scraper before importing core modules that use it
# ---------------------------------------------------------------------------

STUB_ANALYSIS = {
    "url": "https://example.com",
    "status": "stub",
    "analysis": {
        "seo": {
            "title": "Example Domain",
            "meta_description": "Example meta",
            "headings": {"h1": ["Example Heading"], "h2": ["Sub 1", "Sub 2"], "h3": []},
            "og_tags": {"og:title": "Example"},
            "canonical": "https://example.com",
            "viewport": "width=device-width",
        },
        "content": {"word_count": 450, "headings_count": 3},
        "conversion": {
            "ctas": ["Get Started", "Learn More"],
            "forms": [{"action": "/submit"}],
            "buttons": ["Submit", "Sign Up"],
        },
        "trust": {"social_links": ["https://twitter.com/example"], "social_link_count": 1},
        "tracking": {"tools_detected": ["Google Analytics"], "schema_types": ["WebPage"]},
        "technical": {"internal_links": 5, "external_links": 2, "scripts_count": 3},
        "scores": {"seo": 7, "cta": 6, "trust": 5, "tracking": 4},
    },
}

STUB_COMPETITOR = {
    "url": "https://competitor.com",
    "status": "stub",
    "data": {
        "h1": ["Competitor Main Headline"],
        "h2": ["Feature A", "Feature B"],
        "pricing": ["$49/mo", "$99/mo"],
        "social_links": ["https://twitter.com/comp"],
        "trust_signals": ["SOC2 Certified", "GDPR Compliant"],
        "testimonials": ["Great product!", "Highly recommend"],
    },
}


def _mock_fetch_page(url):
    return STUB_ANALYSIS


def _mock_fetch_competitor(url):
    return STUB_COMPETITOR


# ---------------------------------------------------------------------------
# Session tests
# ---------------------------------------------------------------------------

class TestSession(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()
        self.session_file = os.path.join(self.tmpdir, "test_session.json")
        from cli_anything.aimarketing.core.session import Session
        self.Session = Session
        self.session = Session(session_file=self.session_file)

    def test_defaults(self):
        self.assertIsNone(self.session.current_url)
        self.assertIsNotNone(self.session.output_dir)
        self.assertEqual(self.session.history, [])

    def test_set_url(self):
        self.session.current_url = "https://example.com"
        self.assertEqual(self.session.current_url, "https://example.com")
        # Reload from disk
        s2 = self.Session(session_file=self.session_file)
        self.assertEqual(s2.current_url, "https://example.com")

    def test_set_output_dir(self):
        self.session.output_dir = "/tmp/output"
        s2 = self.Session(session_file=self.session_file)
        self.assertEqual(s2.output_dir, "/tmp/output")

    def test_push_history(self):
        for i in range(15):
            self.session.push_history("audit", f"https://example{i}.com", f"summary {i}")
        self.assertEqual(len(self.session.history), 10)

    def test_clear(self):
        self.session.current_url = "https://example.com"
        self.session.clear()
        self.assertIsNone(self.session.current_url)
        self.assertFalse(os.path.exists(self.session_file))

    def test_to_dict(self):
        d = self.session.to_dict()
        self.assertIsInstance(d, dict)
        self.assertIn("current_url", d)
        self.assertIn("output_dir", d)
        self.assertIn("history", d)


# ---------------------------------------------------------------------------
# Audit tests
# ---------------------------------------------------------------------------

class TestAudit(unittest.TestCase):
    def setUp(self):
        patcher = patch(
            "cli_anything.aimarketing.utils.scraper.fetch_page_analysis",
            side_effect=_mock_fetch_page,
        )
        self.addCleanup(patcher.stop)
        patcher.start()
        # Also patch inside audit module
        patcher2 = patch(
            "cli_anything.aimarketing.core.audit.fetch_page_analysis",
            side_effect=_mock_fetch_page,
        )
        self.addCleanup(patcher2.stop)
        patcher2.start()

    def test_run_audit_structure(self):
        from cli_anything.aimarketing.core.audit import run_audit
        r = run_audit("https://example.com")
        for key in ("command", "url", "status", "scores", "recommendations", "revenue_impact"):
            self.assertIn(key, r, f"Missing key: {key}")

    def test_scores_dimensions(self):
        from cli_anything.aimarketing.core.audit import run_audit
        r = run_audit("https://example.com")
        for dim in ("overall", "seo", "content", "conversion", "brand", "competitive", "growth"):
            self.assertIn(dim, r["scores"], f"Missing dimension: {dim}")

    def test_overall_score_range(self):
        from cli_anything.aimarketing.core.audit import run_audit
        r = run_audit("https://example.com")
        self.assertGreaterEqual(r["scores"]["overall"], 0)
        self.assertLessEqual(r["scores"]["overall"], 100)

    def test_grade_mapping(self):
        from cli_anything.aimarketing.core.audit import _grade
        self.assertEqual(_grade(90), "A")
        self.assertEqual(_grade(75), "B")
        self.assertEqual(_grade(60), "C")
        self.assertEqual(_grade(45), "D")
        self.assertEqual(_grade(30), "F")

    def test_run_quick_structure(self):
        from cli_anything.aimarketing.core.audit import run_quick
        r = run_quick("https://example.com")
        self.assertIn("top_3_actions", r)
        self.assertLessEqual(len(r["top_3_actions"]), 3)

    def test_recommendations_generated(self):
        from cli_anything.aimarketing.core.audit import run_audit
        r = run_audit("https://example.com")
        self.assertGreater(len(r["recommendations"]), 0)

    def test_revenue_impact_fields(self):
        from cli_anything.aimarketing.core.audit import run_audit
        r = run_audit("https://example.com")
        impact = r["revenue_impact"]
        self.assertIn("assumed_monthly_visitors", impact)
        self.assertIn("estimated_conversion_lift_pct", impact)
        self.assertIn("estimated_monthly_revenue_impact_usd", impact)


# ---------------------------------------------------------------------------
# Content tests
# ---------------------------------------------------------------------------

class TestContent(unittest.TestCase):
    def setUp(self):
        patcher = patch(
            "cli_anything.aimarketing.core.content.fetch_page_analysis",
            side_effect=_mock_fetch_page,
        )
        self.addCleanup(patcher.stop)
        patcher.start()

    def test_analyze_copy_structure(self):
        from cli_anything.aimarketing.core.content import analyze_copy
        r = analyze_copy("https://example.com")
        for k in ("copy_score", "headlines_analyzed", "cta_issues", "rewrite_frameworks"):
            self.assertIn(k, r)

    def test_evaluate_headline_empty(self):
        from cli_anything.aimarketing.core.content import _evaluate_headline
        r = _evaluate_headline("")
        self.assertEqual(r["score"], 0)

    def test_evaluate_headline_good(self):
        from cli_anything.aimarketing.core.content import _evaluate_headline
        r = _evaluate_headline("5 Proven Ways to Double Your Revenue in 90 Days")
        self.assertGreater(r["score"], 60)

    def test_evaluate_headline_jargon(self):
        from cli_anything.aimarketing.core.content import _evaluate_headline
        r = _evaluate_headline("Leverage our innovative synergy solutions")
        jargon_result = _evaluate_headline("Clear simple headline with number 5")
        self.assertLess(r["score"], jargon_result["score"])

    def test_generate_copy_structure(self):
        from cli_anything.aimarketing.core.content import generate_copy
        r = generate_copy("email marketing")
        self.assertIn("headline_templates", r)
        self.assertIn("cta_templates", r)
        self.assertIn("email_subject_lines", r)

    def test_generate_copy_frameworks(self):
        from cli_anything.aimarketing.core.content import generate_copy
        for fw in ["PAS", "AIDA", "Before-After-Bridge", "4U"]:
            r = generate_copy("SaaS tool", framework=fw)
            self.assertIsInstance(r["headline_templates"], list)
            self.assertGreater(len(r["headline_templates"]), 0)


# ---------------------------------------------------------------------------
# Email gen tests
# ---------------------------------------------------------------------------

class TestEmailGen(unittest.TestCase):
    def _gen(self, seq_type):
        from cli_anything.aimarketing.core.email_gen import generate_email_sequence
        return generate_email_sequence("test topic", seq_type)

    def test_welcome_sequence(self):
        r = self._gen("welcome")
        self.assertEqual(r["overview"]["total_emails"], 5)

    def test_nurture_sequence(self):
        r = self._gen("nurture")
        self.assertEqual(r["overview"]["total_emails"], 6)

    def test_launch_sequence(self):
        r = self._gen("launch")
        self.assertEqual(r["overview"]["total_emails"], 8)

    def test_cold_outreach_sequence(self):
        r = self._gen("cold-outreach")
        self.assertEqual(r["overview"]["total_emails"], 5)

    def test_onboarding_sequence(self):
        r = self._gen("onboarding")
        self.assertEqual(r["overview"]["total_emails"], 6)

    def test_email_fields(self):
        r = self._gen("welcome")
        for email in r["emails"]:
            for field in ("number", "send_day", "subject", "goal", "body_structure"):
                self.assertIn(field, email, f"Missing field {field} in email {email.get('number')}")

    def test_ab_test_ideas(self):
        r = self._gen("welcome")
        self.assertIn("ab_test_ideas", r)
        self.assertGreater(len(r["ab_test_ideas"]), 0)

    def test_compliance_checklist(self):
        r = self._gen("welcome")
        self.assertIn("compliance_checklist", r)
        self.assertGreaterEqual(len(r["compliance_checklist"]), 4)

    def test_invalid_type_defaults_to_welcome(self):
        from cli_anything.aimarketing.core.email_gen import generate_email_sequence
        r = generate_email_sequence("topic", "nonexistent-type")
        self.assertEqual(r["sequence_type"], "welcome")


# ---------------------------------------------------------------------------
# Social tests
# ---------------------------------------------------------------------------

class TestSocial(unittest.TestCase):
    def test_30_day_calendar_length(self):
        from cli_anything.aimarketing.core.social import generate_social_calendar
        r = generate_social_calendar("SaaS marketing")
        self.assertEqual(len(r["calendar"]), 30)

    def test_pillar_distribution(self):
        from cli_anything.aimarketing.core.social import generate_social_calendar
        r = generate_social_calendar("marketing")
        pillars = {post["pillar"] for post in r["calendar"]}
        expected = {"Educational", "Behind-the-Scenes", "Social Proof", "Engagement", "Promotional"}
        self.assertEqual(pillars, expected)

    def test_post_fields(self):
        from cli_anything.aimarketing.core.social import generate_social_calendar
        r = generate_social_calendar("topic")
        for post in r["calendar"]:
            for f in ("day", "pillar", "platform", "hook", "caption", "best_time"):
                self.assertIn(f, post)

    def test_platform_choice(self):
        from cli_anything.aimarketing.core.social import generate_social_calendar, PLATFORMS
        for platform in PLATFORMS:
            r = generate_social_calendar("topic", platform=platform)
            self.assertEqual(r["platform"], platform)

    def test_custom_days(self):
        from cli_anything.aimarketing.core.social import generate_social_calendar
        r = generate_social_calendar("topic", days=7)
        self.assertEqual(len(r["calendar"]), 7)

    def test_engagement_playbook(self):
        from cli_anything.aimarketing.core.social import generate_social_calendar
        r = generate_social_calendar("topic")
        self.assertIn("engagement_playbook", r)
        self.assertGreater(len(r["engagement_playbook"]), 0)

    def test_repurposing_strategy(self):
        from cli_anything.aimarketing.core.social import generate_social_calendar
        r = generate_social_calendar("topic")
        self.assertIn("repurposing_strategy", r)


# ---------------------------------------------------------------------------
# Competitor tests
# ---------------------------------------------------------------------------

class TestCompetitor(unittest.TestCase):
    def setUp(self):
        patcher = patch(
            "cli_anything.aimarketing.core.competitor.fetch_competitor_analysis",
            side_effect=_mock_fetch_competitor,
        )
        self.addCleanup(patcher.stop)
        patcher.start()
        patcher2 = patch(
            "cli_anything.aimarketing.core.competitor.fetch_page_analysis",
            side_effect=_mock_fetch_page,
        )
        self.addCleanup(patcher2.stop)
        patcher2.start()

    def test_scan_competitor_structure(self):
        from cli_anything.aimarketing.core.competitor import scan_competitor
        r = scan_competitor("https://competitor.com")
        for k in ("url", "tier", "swot", "positioning", "steal_worthy"):
            self.assertIn(k, r)

    def test_swot_fields(self):
        from cli_anything.aimarketing.core.competitor import scan_competitor
        r = scan_competitor("https://competitor.com")
        for key in ("strengths", "weaknesses", "opportunities", "threats"):
            self.assertIn(key, r["swot"])

    def test_scan_competitors_matrix(self):
        from cli_anything.aimarketing.core.competitor import scan_competitors
        r = scan_competitors(["https://c1.com", "https://c2.com"])
        self.assertEqual(len(r["comparison_matrix"]), 2)

    def test_steal_worthy(self):
        from cli_anything.aimarketing.core.competitor import scan_competitor
        r = scan_competitor("https://competitor.com")
        self.assertIsInstance(r["steal_worthy"], list)
        self.assertGreater(len(r["steal_worthy"]), 0)

    def test_tier_validation(self):
        from cli_anything.aimarketing.core.competitor import scan_competitor
        r = scan_competitor("https://competitor.com", tier="invalid-tier")
        self.assertEqual(r["tier"], "direct")


# ---------------------------------------------------------------------------
# Export tests
# ---------------------------------------------------------------------------

class TestExport(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()
        self.sample_data = {
            "command": "audit",
            "url": "https://example.com",
            "status": "success",
            "scores": {"overall": 72, "grade": "B", "seo": 70, "content": 75},
            "recommendations": ["Fix meta description", "Add H1 tag"],
            "revenue_impact": {
                "assumed_monthly_visitors": 5000,
                "estimated_conversion_lift_pct": 0.5,
                "estimated_monthly_revenue_impact_usd": 2400,
                "confidence": "medium",
            },
        }

    def test_export_markdown_creates_file(self):
        from cli_anything.aimarketing.core.export import export_markdown
        path = export_markdown(self.sample_data, self.tmpdir)
        self.assertTrue(os.path.exists(path))

    def test_export_markdown_content(self):
        from cli_anything.aimarketing.core.export import export_markdown
        path = export_markdown(self.sample_data, self.tmpdir)
        with open(path, "r", encoding="utf-8") as fh:
            content = fh.read()
        self.assertIn("example.com", content)
        self.assertIn("72", content)

    def test_export_json_creates_file(self):
        from cli_anything.aimarketing.core.export import export_json
        path = export_json(self.sample_data, self.tmpdir)
        self.assertTrue(os.path.exists(path))

    def test_export_json_roundtrip(self):
        from cli_anything.aimarketing.core.export import export_json
        path = export_json(self.sample_data, self.tmpdir)
        with open(path, "r", encoding="utf-8") as fh:
            loaded = json.load(fh)
        self.assertEqual(loaded["url"], self.sample_data["url"])
        self.assertEqual(loaded["scores"]["overall"], 72)

    def test_export_pdf_requires_reportlab(self):
        from cli_anything.aimarketing.core.export import export_pdf
        import importlib
        import sys
        # Patch reportlab as unavailable
        with patch.dict(sys.modules, {"reportlab": None, "reportlab.lib": None,
                                      "reportlab.lib.pagesizes": None,
                                      "reportlab.pdfgen": None,
                                      "reportlab.pdfgen.canvas": None}):
            # Also make the pdf script unavailable
            with patch("os.path.exists", return_value=False):
                with self.assertRaises(RuntimeError):
                    export_pdf(self.sample_data, self.tmpdir)


if __name__ == "__main__":
    unittest.main(verbosity=2)
