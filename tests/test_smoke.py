"""Offline smoke checks; not news-analysis quality tests."""
import json
from pathlib import Path
import sys
import unittest

from news_crosscheck.config import load_config

ROOT = Path(__file__).resolve().parents[1]


class HarnessSmokeTests(unittest.TestCase):
    def test_declared_python_version(self):
        self.assertEqual(sys.version_info[:2], (3, 11), "Project requires Python 3.11")

    def test_project_config_loads(self):
        config = load_config(ROOT / "config.toml")
        self.assertEqual(config["name"], "news-crosscheck")
        self.assertEqual(config["article_language"], "en")
        self.assertEqual(config["report_language"], "ko")

    def test_offline_json_configuration(self):
        config = load_config(ROOT / "config.toml")
        self.assertIs(config["api_enabled"], False)
        self.assertEqual(config["storage_format"], "json")

    def test_configured_fixture_is_readable_and_synthetic(self):
        config = load_config(ROOT / "config.toml")
        path = (ROOT / config["fixture_path"]).resolve()
        self.assertTrue(path.is_relative_to(ROOT / "data" / "fixtures"))
        data = json.loads(path.read_text(encoding="utf-8"))
        self.assertIs(data["synthetic"], True)
        self.assertGreater(len(data["articles"]), 0)
        for article in data["articles"]:
            self.assertEqual(article["language"], "en")
            for field in ("id", "title", "body", "publisher", "country", "published_at"):
                self.assertTrue(article[field])
            self.assertTrue(article["url"].startswith("https://example.invalid/"))


if __name__ == "__main__":
    unittest.main()
