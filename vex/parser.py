from vex.tokens import TokenType
from vex.ast_nodes import (
    Program,
    Identifier,
    NumberLiteral,
    StringLiteral,
    BinaryExpression,
    PrintStatement,
)


class ParserError(Exception):
    pass


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def current(self):
        if self.position >= len(self.tokens):
            return self.tokens[-1]
        return self.tokens[self.position]

    def advance(self):
        token = self.current()
        self.position += 1
        return token

    def match(self, token_type, value=None):
        token = self.current()

        if token.type != token_type:
            return False

        if value is not None and token.value != value:
            return False

        return True

    def consume(self, token_type, value=None):
        token = self.current()

        if not self.match(token_type, value):
            raise ParserError(
                f"Expected {token_type} but got {token.type}"
            )

        return self.advance()

    def parse(self):
        body = []

        while not self.match(TokenType.EOF):
            if self.match(TokenType.NEWLINE):
                self.advance()
                continue

            body.append(self.statement())

        return Program(body)

    def statement(self):
        token = self.current()

        if token.type == TokenType.KEYWORD and token.value in (
            "dikhao",
            "bolo",
        ):
            return self.print_statement()

        raise ParserError(
            f"Unexpected token: {token.value}"
        )

    def print_statement(self):
        self.advance()

        self.consume(TokenType.LEFT_PAREN)

        value = self.expression()

        self.consume(TokenType.RIGHT_PAREN)

        return PrintStatement(value)

    def expression(self):
        token = self.current()

        if token.type == TokenType.STRING:
            self.advance()
            return StringLiteral(token.value)

        if token.type == TokenType.NUMBER:
            self.advance()
            return NumberLiteral(token.value)

        if token.type == TokenType.IDENTIFIER:
            self.advance()
            return Identifier(token.value)

        raise ParserError(
            f"Invalid expression: {token.value}"
        )


def parse(tokens):
    return Parser(tokens).parse()