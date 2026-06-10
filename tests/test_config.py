"""Tests for vex.toml project configuration."""

import tempfile
import unittest
from pathlib import Path

from vex.config import (
    CONFIG_FILENAME,
    VexConfig,
    find_config_file,
    format_config,
    load_config,
    load_project_config,
    parse_config,
    resolve_entry_file,
)
from vex.errors import VexConfigError


class TestConfigParsing(unittest.TestCase):
    def test_parse_valid_config(self):
        content = format_config(name="my_app")
        config = parse_config(content)

        self.assertEqual(config.name, "my_app")
        self.assertEqual(config.version, "0.1.0")
        self.assertEqual(config.mode, "hinglish")
        self.assertEqual(config.entry, "main.vex")

    def test_parse_missing_field_raises(self):
        content = 'name = "my_app"\nversion = "0.1.0"\n'
        with self.assertRaises(VexConfigError):
            parse_config(content)


class TestProjectConfig(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.project_dir = Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_find_and_load_config(self):
        config_content = format_config(name="demo")
        (self.project_dir / CONFIG_FILENAME).write_text(
            config_content,
            encoding="utf-8",
        )

        config_path = find_config_file(self.project_dir)
        self.assertIsNotNone(config_path)

        config = load_config(config_path)
        self.assertIsInstance(config, VexConfig)
        self.assertEqual(config.name, "demo")

    def test_load_project_config_returns_config_and_dir(self):
        (self.project_dir / CONFIG_FILENAME).write_text(
            format_config(name="demo"),
            encoding="utf-8",
        )

        loaded = load_project_config(self.project_dir)
        self.assertIsNotNone(loaded)

        config, project_dir = loaded
        self.assertEqual(config.name, "demo")
        self.assertEqual(project_dir, self.project_dir.resolve())

    def test_resolve_entry_file(self):
        (self.project_dir / CONFIG_FILENAME).write_text(
            format_config(name="demo", entry="main.vex"),
            encoding="utf-8",
        )
        (self.project_dir / "main.vex").write_text(
            '#mode hinglish\n\nbolo "hi"',
            encoding="utf-8",
        )

        entry_file = resolve_entry_file(self.project_dir)
        self.assertEqual(entry_file, self.project_dir / "main.vex")

    def test_resolve_entry_file_without_config_returns_none(self):
        self.assertIsNone(resolve_entry_file(self.project_dir))


if __name__ == "__main__":
    unittest.main()
