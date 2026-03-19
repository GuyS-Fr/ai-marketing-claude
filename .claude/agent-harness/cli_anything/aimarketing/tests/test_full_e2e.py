"""E2E tests for cli-anything-aimarketing.

Tests run against real URLs (example.com) and the installed CLI command.
Set CLI_ANYTHING_FORCE_INSTALLED=1 to run subprocess tests using the installed command.
"""

import json
import os
import subprocess
import sys
import tempfile
import unittest

# Subprocess tests require the installed CLI
_FORCE_INSTALLED = os.environ.get("CLI_ANYTHING_FORCE_INSTALLED") == "1"


def _resolve_cli(name: str) -> str:
    """Find the CLI binary in PATH or raise RuntimeError."""
    import shutil
    path = shutil.which(name)
    if path:
        return path
    raise RuntimeError(
        f"'{name}' not found in PATH. "
        f"Install with: pip install -e agent-harness/ "
        f"then set CLI_ANYTHING_FORCE_INSTALLED=1"
    )


# ---------------------------------------------------------------------------
# E2E: Audit
# ---------------------------------------------------------------------------

class TestAuditE2E(unittest.TestCase):
    def test_audit_live_url(self):
        from cli_anything.aimarketing.core.audit import run_audit
        r = run_audit("https://example.com")
        self.assertIn("scores", r)
        self.assertGreaterEqual(r["scores"]["overall"], 0)
        self.assertLessEqual(r["scores"]["overall"], 100)

    def test_audit_saves_markdown(self):
        from cli_anything.aimarketing.core.audit import run_audit
        from cli_anything.aimarketing.core.export import export_markdown
        with tempfile.TemporaryDirectory() as tmpdir:
            r = run_audit("https://example.com")
            path = export_markdown(r, tmpdir)
            self.assertTrue(os.path.exists(path))
            self.assertGreater(os.path.getsize(path), 100)

    def test_quick_live_url(self):
        from cli_anything.aimarketing.core.audit import run_quick
        r = run_quick("https://example.com")
        self.assertIn("top_3_actions", r)
        self.assertEqual(r["command"], "quick")


# ---------------------------------------------------------------------------
# E2E: Copy
# ---------------------------------------------------------------------------

class TestCopyE2E(unittest.TestCase):
    def test_copy_live_url(self):
        from cli_anything.aimarketing.core.content import analyze_copy
        r = analyze_copy("https://example.com")
        self.assertIn("copy_score", r)
        self.assertIsInstance(r["copy_score"], float)

    def test_generate_copy_all_frameworks(self):
        from cli_anything.aimarketing.core.content import generate_copy
        for fw in ["PAS", "AIDA", "Before-After-Bridge", "4U"]:
            r = generate_copy("email marketing automation", framework=fw)
            self.assertGreater(len(r["headline_templates"]), 0)


# ---------------------------------------------------------------------------
# E2E: Emails
# ---------------------------------------------------------------------------

class TestEmailE2E(unittest.TestCase):
    def test_emails_all_types(self):
        from cli_anything.aimarketing.core.email_gen import generate_email_sequence, SEQUENCE_TYPES
        for seq_type in SEQUENCE_TYPES:
            r = generate_email_sequence("marketing automation", seq_type)
            self.assertIn("emails", r)
            self.assertGreater(len(r["emails"]), 0, f"No emails for type {seq_type}")

    def test_emails_save_markdown(self):
        from cli_anything.aimarketing.core.email_gen import generate_email_sequence
        from cli_anything.aimarketing.core.export import export_markdown
        with tempfile.TemporaryDirectory() as tmpdir:
            r = generate_email_sequence("SaaS onboarding", "welcome")
            path = export_markdown(r, tmpdir)
            with open(path, "r", encoding="utf-8") as fh:
                content = fh.read()
            # File should contain email subjects
            self.assertIn("Email", content)


# ---------------------------------------------------------------------------
# E2E: Social
# ---------------------------------------------------------------------------

class TestSocialE2E(unittest.TestCase):
    def test_social_all_platforms(self):
        from cli_anything.aimarketing.core.social import generate_social_calendar, PLATFORMS
        for platform in PLATFORMS:
            r = generate_social_calendar("productivity software", platform=platform)
            self.assertEqual(r["platform"], platform)
            self.assertGreater(len(r["calendar"]), 0)

    def test_social_calendar_30_days(self):
        from cli_anything.aimarketing.core.social import generate_social_calendar
        r = generate_social_calendar("AI tools for marketers", days=30)
        self.assertEqual(len(r["calendar"]), 30)
        for post in r["calendar"]:
            self.assertIsNotNone(post["hook"])
            self.assertIsNotNone(post["caption"])


# ---------------------------------------------------------------------------
# E2E: Competitors
# ---------------------------------------------------------------------------

class TestCompetitorE2E(unittest.TestCase):
    def test_competitors_live_scan(self):
        from cli_anything.aimarketing.core.competitor import scan_competitor
        r = scan_competitor("https://example.com")
        # Should not raise; may be stub if scripts unavailable
        self.assertIn("swot", r)

    def test_competitors_multi_url(self):
        from cli_anything.aimarketing.core.competitor import scan_competitors
        r = scan_competitors(["https://example.com", "https://iana.org"])
        self.assertEqual(r["competitors_scanned"], 2)
        self.assertEqual(len(r["comparison_matrix"]), 2)


# ---------------------------------------------------------------------------
# E2E: Export pipeline
# ---------------------------------------------------------------------------

class TestExportE2E(unittest.TestCase):
    def test_full_pipeline_to_markdown(self):
        from cli_anything.aimarketing.core.audit import run_audit
        from cli_anything.aimarketing.core.export import export_markdown
        with tempfile.TemporaryDirectory() as tmpdir:
            r = run_audit("https://example.com")
            path = export_markdown(r, tmpdir)
            self.assertTrue(os.path.exists(path))
            with open(path, "r", encoding="utf-8") as fh:
                content = fh.read()
            self.assertIn("example.com", content)
            self.assertIn("Score", content)

    def test_full_pipeline_to_json(self):
        from cli_anything.aimarketing.core.audit import run_audit
        from cli_anything.aimarketing.core.export import export_json
        with tempfile.TemporaryDirectory() as tmpdir:
            r = run_audit("https://example.com")
            path = export_json(r, tmpdir)
            self.assertTrue(os.path.exists(path))
            with open(path, "r", encoding="utf-8") as fh:
                loaded = json.load(fh)
            self.assertIn("scores", loaded)
            self.assertEqual(loaded["url"], "https://example.com")


# ---------------------------------------------------------------------------
# Subprocess tests — require installed CLI
# ---------------------------------------------------------------------------

@unittest.skipUnless(_FORCE_INSTALLED, "Set CLI_ANYTHING_FORCE_INSTALLED=1 to run subprocess tests")
class TestCLISubprocess(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cli = _resolve_cli("cli-anything-aimarketing")

    def _run(self, *args, input_data=None, timeout=60):
        result = subprocess.run(
            [self.cli] + list(args),
            capture_output=True,
            text=True,
            timeout=timeout,
            input=input_data,
        )
        return result

    def test_cli_available_in_path(self):
        r = self._run("--help")
        self.assertEqual(r.returncode, 0)
        self.assertIn("marketing", r.stdout.lower())

    def test_audit_json_output(self):
        r = self._run("--json", "audit", "https://example.com")
        self.assertEqual(r.returncode, 0)
        data = json.loads(r.stdout)
        self.assertIn("scores", data)
        self.assertIn("overall", data["scores"])

    def test_quick_json_output(self):
        r = self._run("--json", "quick", "https://example.com")
        self.assertEqual(r.returncode, 0)
        data = json.loads(r.stdout)
        self.assertIn("scores", data)
        self.assertIn("top_3_actions", data)

    def test_emails_json_output(self):
        r = self._run("--json", "emails", "SaaS onboarding")
        self.assertEqual(r.returncode, 0)
        data = json.loads(r.stdout)
        self.assertIn("emails", data)
        self.assertGreater(len(data["emails"]), 0)

    def test_social_json_output(self):
        r = self._run("--json", "social", "productivity software")
        self.assertEqual(r.returncode, 0)
        data = json.loads(r.stdout)
        self.assertIn("calendar", data)
        self.assertGreater(len(data["calendar"]), 0)

    def test_session_show_json(self):
        r = self._run("--json", "session", "show")
        self.assertEqual(r.returncode, 0)
        data = json.loads(r.stdout)
        self.assertIn("output_dir", data)

    def test_session_clear(self):
        r = self._run("session", "clear")
        self.assertEqual(r.returncode, 0)

    def test_repl_exits_cleanly(self):
        r = self._run("repl", input_data="quit\n", timeout=10)
        self.assertEqual(r.returncode, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
