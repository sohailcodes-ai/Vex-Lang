"""Tests for Vex Hinglish mode translation."""

import unittest
from pathlib import Path

from vex.modes import detect_mode
from vex.translator import transpile

EXAMPLES_DIR = Path(__file__).resolve().parent.parent / "examples"


class TestModeDetection(unittest.TestCase):
    def test_hinglish_mode_from_first_line(self):
        source = "#mode hinglish\n\nbolo \"hi\""
        self.assertEqual(detect_mode(source), "hinglish")

    def test_english_mode_by_default(self):
        source = 'print("hi")'
        self.assertEqual(detect_mode(source), "english")

    def test_hinglish_mode_case_insensitive(self):
        source = "#mode Hinglish\n\nbolo \"hi\""
        self.assertEqual(detect_mode(source), "hinglish")


class TestHinglishTranslation(unittest.TestCase):
    def test_keyword_replacement(self):
        source = "#mode hinglish\n\nbolo \"Hello\""
        result = transpile(source)
        self.assertIn('print("Hello")', result)
        self.assertNotIn("bolo", result)

    def test_if_and_print_keywords(self):
        source = "#mode hinglish\n\nagar x:\n    bolo \"yes\""
        result = transpile(source)
        self.assertIn("if x:", result)
        self.assertIn('print("yes")', result)

    def test_f_string_auto_conversion(self):
        source = '#mode hinglish\n\nnaam = "Sohail"\nbolo "Yo {naam}!"'
        result = transpile(source)
        self.assertIn('naam = "Sohail"', result)
        self.assertIn('print(f"Yo {naam}!")', result)

    def test_mode_directive_stripped(self):
        source = "#mode hinglish\n\nbolo \"hi\""
        result = transpile(source)
        self.assertNotIn("#mode", result)

    def test_english_mode_leaves_keywords_unchanged(self):
        source = '#mode english\n\nprint("hi")'
        result = transpile(source)
        self.assertIn('print("hi")', result)


class TestTranslateOutput(unittest.TestCase):
    """Translator-level tests for vex translate command output."""

    def test_hello_vex_transpiles_to_python(self):
        source = (EXAMPLES_DIR / "hello.vex").read_text(encoding="utf-8")
        result = transpile(source)

        self.assertIn('naam = "Sohail"', result)
        self.assertIn('print ("Yo Duniya!")', result)
        self.assertIn('print (f"Mera naam {naam} hai")', result)
        self.assertNotIn("bolo", result)
        self.assertNotIn("#mode", result)


if __name__ == "__main__":
    unittest.main()
