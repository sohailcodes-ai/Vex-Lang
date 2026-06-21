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


@dataclass
class FunctionBytecode:
    name: str
    params: list[str]
    instructions: list[Instruction]

    def __repr__(self) -> str:
        return f"<function {self.name}({', '.join(self.params)})>"


class OpCode:
    LOAD_CONST = "LOAD_CONST"
    LOAD_NAME = "LOAD_NAME"
    STORE_NAME = "STORE_NAME"

    PRINT = "PRINT"
    POP_TOP = "POP_TOP"
    RETURN_VALUE = "RETURN_VALUE"

    BINARY_ADD = "BINARY_ADD"
    BINARY_SUB = "BINARY_SUB"
    BINARY_MUL = "BINARY_MUL"
    BINARY_DIV = "BINARY_DIV"

    COMPARE_EQ = "COMPARE_EQ"
    COMPARE_NE = "COMPARE_NE"
    COMPARE_LT = "COMPARE_LT"
    COMPARE_LTE = "COMPARE_LTE"
    COMPARE_GT = "COMPARE_GT"
    COMPARE_GTE = "COMPARE_GTE"

    LOGICAL_AND = "LOGICAL_AND"
    LOGICAL_OR = "LOGICAL_OR"
    LOGICAL_NOT = "LOGICAL_NOT"

    BUILD_LIST = "BUILD_LIST"
    GET_INDEX = "GET_INDEX"

    JUMP = "JUMP"
    JUMP_IF_FALSE = "JUMP_IF_FALSE"

    CALL_FUNCTION = "CALL_FUNCTION"