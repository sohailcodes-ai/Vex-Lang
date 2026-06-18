from vex.tokens import TokenType
from vex.ast_nodes import (
    Program,
    Identifier,
    NumberLiteral,
    StringLiteral,
    BinaryExpression,
    PrintStatement,
    IfStatement,
    AssignmentStatement,
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
            expected = token_type.value
            if value is not None:
                expected += f"({value})"

            raise ParserError(
                f"Expected {expected} but got {token.type.value}({token.value!r}) "
                f"at line {token.line}, column {token.column}"
            )

        return self.advance()

    def skip_newlines(self):
        while self.match(TokenType.NEWLINE):
            self.advance()

    def parse(self):
        body = []

        self.skip_newlines()

        while not self.match(TokenType.EOF):
            body.append(self.statement())
            self.skip_newlines()

        return Program(body)

    def statement(self):
        token = self.current()

        if token.type == TokenType.KEYWORD and token.value in ("dikhao", "bolo"):
            return self.print_statement()

        if token.type == TokenType.KEYWORD and token.value == "agar":
            return self.if_statement()

        if token.type == TokenType.IDENTIFIER:
            return self.assignment_statement()

        raise ParserError(
            f"Unexpected token {token.type.value}({token.value!r}) "
            f"at line {token.line}, column {token.column}"
        )

    def print_statement(self):
        self.advance()

        self.consume(TokenType.LEFT_PAREN)
        value = self.expression()
        self.consume(TokenType.RIGHT_PAREN)

        return PrintStatement(value)

    def assignment_statement(self):
        target_token = self.consume(TokenType.IDENTIFIER)
        self.consume(TokenType.OPERATOR, "=")
        value = self.expression()

        return AssignmentStatement(
            target=Identifier(target_token.value),
            value=value,
        )

    def if_statement(self):
        self.consume(TokenType.KEYWORD, "agar")

        left = self.expression()
        operator = self.consume(TokenType.OPERATOR)
        right = self.expression()

        condition = BinaryExpression(
            left=left,
            operator=operator.value,
            right=right,
        )

        self.consume(TokenType.COLON)
        self.skip_newlines()

        body = []

        if self.match(TokenType.KEYWORD, "dikhao") or self.match(TokenType.KEYWORD, "bolo"):
            body.append(self.print_statement())
        else:
            token = self.current()
            raise ParserError(
                f"Expected statement inside if body but got {token.type.value}({token.value!r}) "
                f"at line {token.line}, column {token.column}"
            )

        return IfStatement(condition=condition, body=body)

    def expression(self):
        return self.additive()

    def additive(self):
        node = self.multiplicative()

        while self.match(TokenType.OPERATOR, "+") or self.match(TokenType.OPERATOR, "-"):
            operator = self.advance()
            right = self.multiplicative()
            node = BinaryExpression(
                left=node,
                operator=operator.value,
                right=right,
            )

        return node

    def multiplicative(self):
        node = self.primary()

        while self.match(TokenType.OPERATOR, "*") or self.match(TokenType.OPERATOR, "/"):
            operator = self.advance()
            right = self.primary()
            node = BinaryExpression(
                left=node,
                operator=operator.value,
                right=right,
            )

        return node

    def primary(self):
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

        if token.type == TokenType.LEFT_PAREN:
            self.advance()
            expr = self.expression()
            self.consume(TokenType.RIGHT_PAREN)
            return expr

        raise ParserError(
            f"Invalid expression {token.type.value}({token.value!r}) "
            f"at line {token.line}, column {token.column}"
        )


def parse(tokens):
    return Parser(tokens).parse()