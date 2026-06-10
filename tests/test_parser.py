import unittest

from vex.lexer import tokenize
from vex.parser import parse


class TestParser(unittest.TestCase):

    def test_parse_print_statement(self):
        tokens = tokenize('dikhao("Hello")')

        ast = parse(tokens)

        output = ast.pretty()

        self.assertIn("Program", output)
        self.assertIn("PrintStatement", output)
        self.assertIn("StringLiteral('Hello')", output)

    def test_parse_bolo_statement(self):
        tokens = tokenize('bolo("Hi")')

        ast = parse(tokens)

        output = ast.pretty()

        self.assertIn("PrintStatement", output)

    def test_parse_if_statement(self):
        code = """
agar age >= 18:
    dikhao("Adult")
"""

        tokens = tokenize(code)

        ast = parse(tokens)

        output = ast.pretty()

        self.assertIn("IfStatement", output)
        self.assertIn("BinaryExpression(>=)", output)
        self.assertIn("Identifier(age)", output)
        self.assertIn("NumberLiteral(18)", output)
        self.assertIn("PrintStatement", output)


if __name__ == "__main__":
    unittest.main()