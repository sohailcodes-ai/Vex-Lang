import unittest

from vex.lexer import tokenize
from vex.tokens import TokenType


class TestLexer(unittest.TestCase):
    def test_tokenizes_if_statement(self):
        tokens = tokenize("agar age >= 18:")
        values = [token.value for token in tokens]

        self.assertEqual(values[:-2], ["agar", "age", ">=", "18", ":"])
        self.assertEqual(tokens[-2].type, TokenType.NEWLINE)
        self.assertEqual(tokens[-1].type, TokenType.EOF)

        self.assertEqual(tokens[0].type, TokenType.KEYWORD)
        self.assertEqual(tokens[1].type, TokenType.IDENTIFIER)
        self.assertEqual(tokens[2].type, TokenType.OPERATOR)
        self.assertEqual(tokens[3].type, TokenType.NUMBER)
        self.assertEqual(tokens[4].type, TokenType.COLON)

    def test_tokenizes_print_statement(self):
        tokens = tokenize('dikhao("Adult")')
        types = [token.type for token in tokens]

        self.assertEqual(
            types[:-2],
            [
                TokenType.KEYWORD,
                TokenType.LEFT_PAREN,
                TokenType.STRING,
                TokenType.RIGHT_PAREN,
            ],
        )

        self.assertEqual(tokens[-2].type, TokenType.NEWLINE)
        self.assertEqual(tokens[-1].type, TokenType.EOF)

    def test_ignores_mode_directive(self):
        tokens = tokenize("#mode hinglish\nagar x > 5:")
        values = [token.value for token in tokens]

        self.assertIn("agar", values)
        self.assertNotIn("#mode hinglish", values)

    def test_emits_indent_and_dedent(self):
        tokens = tokenize(
            """agar age >= 18:
    dikhao("Adult")
"""
        )

        types = [token.type for token in tokens]

        self.assertIn(TokenType.INDENT, types)
        self.assertIn(TokenType.DEDENT, types)

    def test_nested_block_tokens(self):
        tokens = tokenize(
            """jabtak x < 3:
    x = x + 1
"""
        )

        types = [token.type for token in tokens]

        self.assertEqual(types.count(TokenType.INDENT), 1)
        self.assertEqual(types.count(TokenType.DEDENT), 1)


if __name__ == "__main__":
    unittest.main()