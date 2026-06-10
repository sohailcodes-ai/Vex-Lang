import unittest

from vex.lexer import tokenize
from vex.tokens import TokenType


class TestLexer(unittest.TestCase):
    def test_tokenizes_if_statement(self):
        tokens = tokenize("agar age >= 18:")
        values = [token.value for token in tokens]

        self.assertEqual(values[:-1], ["agar", "age", ">=", "18", ":"])
        self.assertEqual(tokens[0].type, TokenType.KEYWORD)
        self.assertEqual(tokens[1].type, TokenType.IDENTIFIER)
        self.assertEqual(tokens[2].type, TokenType.OPERATOR)
        self.assertEqual(tokens[3].type, TokenType.NUMBER)
        self.assertEqual(tokens[4].type, TokenType.COLON)

    def test_tokenizes_print_statement(self):
        tokens = tokenize('dikhao("Adult")')
        types = [token.type for token in tokens]

        self.assertEqual(
            types[:-1],
            [
                TokenType.KEYWORD,
                TokenType.LEFT_PAREN,
                TokenType.STRING,
                TokenType.RIGHT_PAREN,
            ],
        )

    def test_ignores_mode_directive(self):
        tokens = tokenize("#mode hinglish\nagar x > 5:")
        values = [token.value for token in tokens]

        self.assertIn("agar", values)
        self.assertNotIn("#mode hinglish", values)


if __name__ == "__main__":
    unittest.main()