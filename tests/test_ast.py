import unittest

from vex.ast_nodes import (
    Program,
    Identifier,
    NumberLiteral,
    StringLiteral,
    BinaryExpression,
    PrintStatement,
    IfStatement,
)


class TestASTNodes(unittest.TestCase):
    def test_program_pretty_print(self):
        program = Program(
            body=[
                PrintStatement(StringLiteral("Hello")),
            ]
        )

        output = program.pretty()

        self.assertIn("Program", output)
        self.assertIn("PrintStatement", output)
        self.assertIn("StringLiteral('Hello')", output)

    def test_if_statement_pretty_print(self):
        condition = BinaryExpression(
            left=Identifier("age"),
            operator=">=",
            right=NumberLiteral("18"),
        )

        node = IfStatement(
            condition=condition,
            body=[PrintStatement(StringLiteral("Adult"))],
        )

        output = node.pretty()

        self.assertIn("IfStatement", output)
        self.assertIn("BinaryExpression(>=)", output)
        self.assertIn("Identifier(age)", output)
        self.assertIn("NumberLiteral(18)", output)
        self.assertIn("PrintStatement", output)


if __name__ == "__main__":
    unittest.main()