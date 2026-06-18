from dataclasses import dataclass
from typing import Any


@dataclass
class Instruction:
    op: str
    arg: Any = None

    def __repr__(self) -> str:
        if self.arg is None:
            return self.op
        return f"{self.op} {self.arg!r}"


class OpCode:
    LOAD_CONST = "LOAD_CONST"
    LOAD_NAME = "LOAD_NAME"
    STORE_NAME = "STORE_NAME"
    PRINT = "PRINT"
    POP_TOP = "POP_TOP"
    BINARY_ADD = "BINARY_ADD"
    BINARY_SUB = "BINARY_SUB"
    BINARY_MUL = "BINARY_MUL"
    BINARY_DIV = "BINARY_DIV"
    RETURN_VALUE = "RETURN_VALUE"