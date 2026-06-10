"""
translator.py
-------------
Core of Vex — converts Vex source code into Python code.
"""

import re

from vex.modes import HINGLISH_TO_PYTHON, detect_mode


def fix_strings(line: str) -> str:
    """
    Auto converts {var} inside strings to f-strings.
    bolo "Hello {naam}" → print(f"Hello {naam}")
    """
    if re.search(r'"[^"]*\{[^}]+\}[^"]*"', line):
        line = re.sub(r'"([^"]*\{[^}]+\}[^"]*)"', r'f"\1"', line)
    return line


def replace_hinglish_keywords(line: str) -> str:
    """
    Replaces Hinglish keywords even when attached to symbols.

    Example:
    dikhao("Adult") -> print("Adult")
    agar age >= 18: -> if age >= 18:
    """
    for vex_keyword, python_keyword in HINGLISH_TO_PYTHON.items():
        line = re.sub(
            rf"\b{re.escape(vex_keyword)}\b",
            python_keyword,
            line,
        )
    return line


def normalize_print_syntax(line: str) -> str:
    """
    Supports:
    print "Hello"     -> print("Hello")
    print f"Hello"   -> print(f"Hello")
    print variable   -> print(variable)
    print func(x)    -> print(func(x))
    print(x)         -> print(x)
    """
    stripped = line.lstrip()
    indent = line[: len(line) - len(stripped)]

    if not stripped.startswith("print "):
        return line

    value = stripped[len("print ") :].strip()

    if value.startswith("("):
        return line

    return f"{indent}print({value})"


def transpile(source: str) -> str:
    """Takes Vex source and returns equivalent Python source."""
    lines = source.splitlines()
    mode = detect_mode(source)
    output = []

    for line in lines:
        if line.strip().startswith("#mode"):
            continue

        line = fix_strings(line)

        if mode == "hinglish":
            line = replace_hinglish_keywords(line)

        line = normalize_print_syntax(line)

        output.append(line)

    return "\n".join(output)