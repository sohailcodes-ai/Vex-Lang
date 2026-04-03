"""
parser.py
---------
Vex Parser — takes tokens from Lexer and builds an AST.
AST (Abstract Syntax Tree) represents the structure of the program.
Example:
    [Token(KEYWORD, 'bolo'), Token(STRING, 'Hello')]
    → PrintNode(value='Hello')
"""


class Parser:
    """
    Converts token list into an Abstract Syntax Tree (AST).
    """

    def __init__(self, tokens: list):
        self.tokens = tokens

    def parse(self):
        """
        Main method — converts tokens into AST.
        To be implemented.
        """
        pass