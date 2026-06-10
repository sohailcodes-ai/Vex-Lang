from vex.tokens import Token, TokenType


KEYWORDS = {
    "agar",
    "warna",
    "warna_agar",
    "dikhao",
    "bolo",
    "jabtak",
    "har",
    "ke_liye",
    "mai",
    "kaam",
    "wapas",
    "sahi",
    "galat",
    "khali",
}


OPERATORS = {
    "==",
    "!=",
    ">=",
    "<=",
    "+",
    "-",
    "*",
    "/",
    "%",
    "=",
    ">",
    "<",
}


class LexerError(Exception):
    pass


class Lexer:
    def __init__(self, source: str):
        self.source = source
        self.position = 0
        self.line = 1
        self.column = 1
        self.tokens = []

    def current_char(self):
        if self.position >= len(self.source):
            return None
        return self.source[self.position]

    def peek_char(self):
        next_position = self.position + 1
        if next_position >= len(self.source):
            return None
        return self.source[next_position]

    def advance(self):
        char = self.current_char()
        self.position += 1

        if char == "\n":
            self.line += 1
            self.column = 1
        else:
            self.column += 1

        return char

    def add_token(self, token_type, value, line=None, column=None):
        self.tokens.append(
            Token(
                token_type,
                value,
                line if line is not None else self.line,
                column if column is not None else self.column,
            )
        )

    def tokenize(self):
        while self.current_char() is not None:
            char = self.current_char()

            if char in " \t\r":
                self.advance()
                continue

            if char == "\n":
                self.add_token(TokenType.NEWLINE, "\\n")
                self.advance()
                continue

            if char == "#":
                self.skip_comment_or_directive()
                continue

            if char.isalpha() or char == "_":
                self.tokenize_identifier_or_keyword()
                continue

            if char.isdigit():
                self.tokenize_number()
                continue

            if char in ('"', "'"):
                self.tokenize_string()
                continue

            if char == ":":
                self.add_token(TokenType.COLON, char)
                self.advance()
                continue

            if char == ",":
                self.add_token(TokenType.COMMA, char)
                self.advance()
                continue

            if char == "(":
                self.add_token(TokenType.LEFT_PAREN, char)
                self.advance()
                continue

            if char == ")":
                self.add_token(TokenType.RIGHT_PAREN, char)
                self.advance()
                continue

            if self.is_operator_start(char):
                self.tokenize_operator()
                continue

            raise LexerError(
                f"Unexpected character {char!r} at line {self.line}, column {self.column}"
            )

        self.add_token(TokenType.EOF, "")
        return self.tokens

    def skip_comment_or_directive(self):
        while self.current_char() is not None and self.current_char() != "\n":
            self.advance()

    def tokenize_identifier_or_keyword(self):
        start_line = self.line
        start_column = self.column
        value = ""

        while self.current_char() is not None and (
            self.current_char().isalnum() or self.current_char() == "_"
        ):
            value += self.advance()

        token_type = TokenType.KEYWORD if value in KEYWORDS else TokenType.IDENTIFIER
        self.add_token(token_type, value, start_line, start_column)

    def tokenize_number(self):
        start_line = self.line
        start_column = self.column
        value = ""

        while self.current_char() is not None and self.current_char().isdigit():
            value += self.advance()

        if self.current_char() == ".":
            value += self.advance()
            while self.current_char() is not None and self.current_char().isdigit():
                value += self.advance()

        self.add_token(TokenType.NUMBER, value, start_line, start_column)

    def tokenize_string(self):
        start_line = self.line
        start_column = self.column
        quote = self.advance()
        value = ""

        while self.current_char() is not None and self.current_char() != quote:
            if self.current_char() == "\n":
                raise LexerError(
                    f"Unterminated string at line {start_line}, column {start_column}"
                )
            value += self.advance()

        if self.current_char() != quote:
            raise LexerError(
                f"Unterminated string at line {start_line}, column {start_column}"
            )

        self.advance()
        self.add_token(TokenType.STRING, value, start_line, start_column)

    def is_operator_start(self, char):
        return any(op.startswith(char) for op in OPERATORS)

    def tokenize_operator(self):
        start_line = self.line
        start_column = self.column

        two_char = (self.current_char() or "") + (self.peek_char() or "")
        if two_char in OPERATORS:
            self.advance()
            self.advance()
            self.add_token(TokenType.OPERATOR, two_char, start_line, start_column)
            return

        one_char = self.current_char()
        if one_char in OPERATORS:
            self.advance()
            self.add_token(TokenType.OPERATOR, one_char, start_line, start_column)
            return

        raise LexerError(
            f"Invalid operator at line {self.line}, column {self.column}"
        )


def tokenize(source: str):
    return Lexer(source).tokenize()