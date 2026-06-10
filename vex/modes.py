"""
modes.py
--------
Mode detection and keyword mappings for Hinglish/English Vex source.
"""

HINGLISH_TO_PYTHON = {
    "bolo": "print",
    "dikhao": "print",
    "agar": "if",
    "warna": "else",
    "warna_agar": "elif",
    "jabtak": "while",
    "har": "for",
    "mai": "in",
    "kaam": "def",
    "wapas": "return",
    "aao": "import",
    "jaise": "as",
    "pakdo": "try",
    "chodo": "except",
    "sahi": "True",
    "galat": "False",
    "kuch_nahi": "None",
    "cheez": "class",
    "khud": "self",
    "aur": "and",
    "ya": "or",
    "nahi": "not",
    "seedha": "lambda",
    #"hai": "is",
    "chalne_de": "pass",
    "rok": "break",
    "aage": "continue",
}

ENGLISH_KEYWORDS = {
    "print", "if", "else", "elif", "while",
    "for", "in", "def", "return", "import",
    "as", "try", "except", "True", "False",
    "None", "class", "self", "and", "or",
    "not", "lambda", "is", "pass", "break",
    "continue",
}


def detect_mode(source: str) -> str:
    """Detects #mode hinglish or #mode english from the first line."""
    lines = source.strip().splitlines()
    if not lines:
        return "english"

    first_line = lines[0].strip().lower()
    if first_line == "#mode hinglish":
        return "hinglish"
    return "english"
