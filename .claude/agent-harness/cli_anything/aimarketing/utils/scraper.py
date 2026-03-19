"""Web scraping utilities — thin wrappers around the project's analyze_page.py and
competitor_scanner.py scripts located at ../../scripts/ relative to this file."""

import importlib.util
import os
import sys
from typing import Any, Dict

# Resolve the scripts directory relative to this file
_HERE = os.path.dirname(os.path.abspath(__file__))
_SCRIPTS_DIR = os.path.normpath(
    os.path.join(_HERE, "..", "..", "..", "..", "scripts")
)


def _load_module(name: str, filename: str):
    """Dynamically load a script from the scripts directory."""
    path = os.path.join(_SCRIPTS_DIR, filename)
    if not os.path.exists(path):
        return None
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
    except Exception:
        return None
    return mod


def fetch_page_analysis(url: str) -> Dict[str, Any]:
    """Fetch and parse a webpage using MarketingPageParser from analyze_page.py.

    Returns a dict with keys: url, status, analysis (seo/content/conversion/trust/tracking/technical/scores).
    Falls back to a minimal stub if the script is unavailable.
    """
    mod = _load_module("analyze_page", "analyze_page.py")
    if mod is None:
        return _stub_analysis(url)

    try:
        result = mod.analyze(url)
        if isinstance(result, dict):
            return result
    except Exception:
        pass

    # Try calling directly via the parser class
    try:
        import urllib.request
        import ssl

        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        req = urllib.request.Request(
            url, headers={"User-Agent": "cli-anything-aimarketing/0.1"}
        )
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            html = resp.read().decode("utf-8", errors="replace")

        parser = mod.MarketingPageParser()
        parser.feed(html)
        return {
            "url": url,
            "status": "success",
            "analysis": parser.get_results(),
        }
    except Exception as exc:
        return {"url": url, "status": "error", "error": str(exc), "analysis": {}}


def fetch_competitor_analysis(url: str) -> Dict[str, Any]:
    """Scan a competitor page using CompetitorPageParser from competitor_scanner.py."""
    mod = _load_module("competitor_scanner", "competitor_scanner.py")
    if mod is None:
        return _stub_competitor(url)

    try:
        import urllib.request
        import ssl

        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        req = urllib.request.Request(
            url, headers={"User-Agent": "cli-anything-aimarketing/0.1"}
        )
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            html = resp.read().decode("utf-8", errors="replace")

        parser = mod.CompetitorPageParser()
        parser.feed(html)
        return {"url": url, "status": "success", "data": parser.get_results()}
    except Exception as exc:
        return {"url": url, "status": "error", "error": str(exc), "data": {}}


# ------------------------------------------------------------------
# Stubs (used when scripts are not importable, e.g., in unit tests)
# ------------------------------------------------------------------

def _stub_analysis(url: str) -> Dict[str, Any]:
    return {
        "url": url,
        "status": "stub",
        "analysis": {
            "seo": {
                "title": "",
                "meta_description": "",
                "headings": {"h1": [], "h2": [], "h3": []},
                "og_tags": {},
            },
            "content": {"word_count": 0, "headings_count": 0},
            "conversion": {"ctas": [], "forms": [], "buttons": []},
            "trust": {"social_links": [], "social_link_count": 0},
            "tracking": {"tools_detected": [], "schema_types": []},
            "technical": {"internal_links": 0, "external_links": 0, "scripts_count": 0},
            "scores": {"seo": 0, "cta": 0, "trust": 0, "tracking": 0},
        },
    }


def _stub_competitor(url: str) -> Dict[str, Any]:
    return {
        "url": url,
        "status": "stub",
        "data": {
            "h1": [],
            "h2": [],
            "pricing": [],
            "social_links": [],
            "trust_signals": [],
            "testimonials": [],
        },
    }
