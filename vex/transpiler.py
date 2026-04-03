"""
transpiler.py
-------------
Core of Vex — converts Vex source code into Python code.
"""

import re
from vex.keywords import HINGLISH_TO_PYTHON
def detect_mode(source: str) -> str:
    """Detects #mode hinglish or #mode english from first line."""
    first_line = source.strip().splitlines()[0]
    if first_line.strip() == "#mode hinglish":
        return "hinglish"
    return "english"
def fix_strings(line: str) -> str:
    """
    Auto converts {var} inside strings to f-strings.
    bolo "Hello {naam}" → print(f"Hello {naam}")
    """
    if re.search(r'"[^"]*\{[^}]+\}[^"]*"', line):
        line = re.sub(r'"([^"]*\{[^}]+\}[^"]*)"', r'f"\1"', line)
    return line
def transpile(source: str) -> str:
    """
    Main function — takes Vex source, returns Python source.
    """
    lines = source.splitlines()
    mode = detect_mode(source)
    output = []
    for line in lines:
        if line.strip().startswith("#mode"):
            continue
        line = fix_strings(line)
        if mode == "hinglish":
            words = line.split(" ")
            new_words = []
            for word in words:
                stripped = word.strip()
                if stripped in HINGLISH_TO_PYTHON:
                    word = word.replace(stripped, HINGLISH_TO_PYTHON[stripped])
                new_words.append(word)
            line = " ".join(new_words)
        line = re.sub(
            r'\bprint\s+"([^"]*)"',
            r'print("\1")',
            line
        )
        line = re.sub(
            r"\bprint\s+'([^']*)'",
            r"print('\1')",
            line
        )

        output.append(line)

    return "\n".join(output)