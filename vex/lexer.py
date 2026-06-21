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
    "rok",
    "aage",
    "aur",
    "ya",
    "nahi",
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
        self.lines = source.splitlines()
        self.tokens = []
        self.indent_stack = [0]

    def add_token(self, token_type, value, line, column):
        self.tokens.append(Token(token_type, value, line, column))

    def tokenize(self):
        for line_number, raw_line in enumerate(self.lines, start=1):
            if not raw_line.strip():
                continue

            stripped = raw_line.lstrip(" ")
            indent = len(raw_line) - len(stripped)

            if stripped.startswith("#"):
                continue

            self.handle_indent(indent, line_number)
            self.tokenize_line(stripped, line_number, indent + 1)
            self.add_token(TokenType.NEWLINE, "\\n", line_number, len(raw_line) + 1)

        while len(self.indent_stack) > 1:
            self.indent_stack.pop()
            self.add_token(TokenType.DEDENT, "", len(self.lines), 1)

        self.add_token(TokenType.EOF, "", len(self.lines) + 1, 1)
        return self.tokens

    def handle_indent(self, indent, line_number):
        current_indent = self.indent_stack[-1]

        if indent > current_indent:
            self.indent_stack.append(indent)
            self.add_token(TokenType.INDENT, "", line_number, 1)
            return

        while indent < self.indent_stack[-1]:
            self.indent_stack.pop()
            self.add_token(TokenType.DEDENT, "", line_number, 1)

        if indent != self.indent_stack[-1]:
            raise LexerError(f"Invalid indentation at line {line_number}")

    def tokenize_line(self, line, line_number, base_column):
        position = 0

        while position < len(line):
            char = line[position]
            column = base_column + position

            if char in " \t\r":
                position += 1
                continue

            if char == "#":
                break

            if char.isalpha() or char == "_":
                position = self.tokenize_identifier_or_keyword(
                    line,
                    position,
                    line_number,
                    column,
                )
                continue

            if char.isdigit():
                position = self.tokenize_number(line, position, line_number, column)
                continue

            if char in ('"', "'"):
                position = self.tokenize_string(line, position, line_number, column)
                continue

            if char == ":":
                self.add_token(TokenType.COLON, char, line_number, column)
                position += 1
                continue

            if char == ",":
                self.add_token(TokenType.COMMA, char, line_number, column)
                position += 1
                continue

            if char == "(":
                self.add_token(TokenType.LEFT_PAREN, char, line_number, column)
                position += 1
                continue

            if char == ")":
                self.add_token(TokenType.RIGHT_PAREN, char, line_number, column)
                position += 1
                continue

            if char == "[":
                self.add_token(TokenType.LEFT_BRACKET, char, line_number, column)
                position += 1
                continue

            if char == "]":
                self.add_token(TokenType.RIGHT_BRACKET, char, line_number, column)
                position += 1
                continue

            if char == ".":
                self.add_token(TokenType.DOT, char, line_number, column)
                position += 1
                continue

            if self.is_operator_start(char):
                position = self.tokenize_operator(line, position, line_number, column)
                continue

            raise LexerError(
                f"Unexpected character {char!r} at line {line_number}, column {column}"
            )

    def tokenize_identifier_or_keyword(self, line, position, line_number, column):
        start = position

        while position < len(line) and (
            line[position].isalnum() or line[position] == "_"
        ):
            position += 1

        value = line[start:position]
        token_type = TokenType.KEYWORD if value in KEYWORDS else TokenType.IDENTIFIER
        self.add_token(token_type, value, line_number, column)
        return position

    def tokenize_number(self, line, position, line_number, column):
        start = position

        while position < len(line) and line[position].isdigit():
            position += 1

        if position < len(line) and line[position] == ".":
            position += 1

            while position < len(line) and line[position].isdigit():
                position += 1

        self.add_token(TokenType.NUMBER, line[start:position], line_number, column)
        return position

    def tokenize_string(self, line, position, line_number, column):
        quote = line[position]
        position += 1
        value = ""

        while position < len(line) and line[position] != quote:
            value += line[position]
            position += 1

        if position >= len(line) or line[position] != quote:
            raise LexerError(f"Unterminated string at line {line_number}, column {column}")

        position += 1
        self.add_token(TokenType.STRING, value, line_number, column)
        return position

    def is_operator_start(self, char):
        return any(op.startswith(char) for op in OPERATORS)

    def tokenize_operator(self, line, position, line_number, column):
        two_char = line[position:position + 2]

        if two_char in OPERATORS:
            self.add_token(TokenType.OPERATOR, two_char, line_number, column)
            return position + 2

        one_char = line[position]

        if one_char in OPERATORS:
            self.add_token(TokenType.OPERATOR, one_char, line_number, column)
            return position + 1

        raise LexerError(f"Invalid operator at line {line_number}, column {column}")


def tokenize(source: str):
    return Lexer(source).tokenize()