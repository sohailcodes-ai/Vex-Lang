"""
lexer.py
--------
Vex Lexer — takes raw Vex source code and converts it into tokens.
Example:
    bolo "Hello World"
    → [Token(KEYWORD, 'bolo'), Token(STRING, 'Hello World')]
"""


class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {repr(self.value)})"


class Lexer:
    """
    Tokenizes Vex source code into a list of Token objects.
    Handles both hinglish and english mode.
    """

    def __init__(self, source: str):
        self.source = source
        self.tokens = []

    def tokenize(self) -> list:
        """
        Main method — converts source string into token list.
        To be implemented.
        """
        pass