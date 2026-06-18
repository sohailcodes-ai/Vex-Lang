from __future__ import annotations

from typing import Any

from vex.bytecode import Instruction, OpCode


class VexCompilerError(Exception):
    pass


class VexCompiler:
    def __init__(self) -> None:
        self.instructions: list[Instruction] = []

    def emit(self, op: str, arg: Any = None) -> None:
        self.instructions.append(Instruction(op, arg))

    def compile(self, ast: Any) -> list[Instruction]:
        self.instructions = []
        self.compile_node(ast)
        return self.instructions

    def compile_node(self, node: Any) -> None:
        name = node.__class__.__name__

        if name == "Program":
            for statement in node.body:
                self.compile_node(statement)

        elif name == "AssignmentStatement":
            self.compile_node(node.value)
            self.emit(OpCode.STORE_NAME, node.target.name)

        elif name == "PrintStatement":
            self.compile_node(node.value)
            self.emit(OpCode.PRINT)

        elif name == "IfStatement":
            raise VexCompilerError(
                "IfStatement VM support not implemented yet. Coming next."
            )

        elif name == "NumberLiteral":
            value = node.value
            if isinstance(value, str) and "." in value:
                value = float(value)
            elif isinstance(value, str):
                value = int(value)
            self.emit(OpCode.LOAD_CONST, value)

        elif name == "StringLiteral":
            self.emit(OpCode.LOAD_CONST, node.value)

        elif name == "BooleanLiteral":
            self.emit(OpCode.LOAD_CONST, node.value)

        elif name == "NullLiteral":
            self.emit(OpCode.LOAD_CONST, None)

        elif name == "Identifier":
            self.emit(OpCode.LOAD_NAME, node.name)

        elif name == "BinaryExpression":
            self.compile_node(node.left)
            self.compile_node(node.right)

            if node.operator == "+":
                self.emit(OpCode.BINARY_ADD)
            elif node.operator == "-":
                self.emit(OpCode.BINARY_SUB)
            elif node.operator == "*":
                self.emit(OpCode.BINARY_MUL)
            elif node.operator == "/":
                self.emit(OpCode.BINARY_DIV)
            else:
                raise VexCompilerError(
                    f"Unsupported binary operator for VM: {node.operator}"
                )

        else:
            raise VexCompilerError(f"Unsupported AST node for VM: {name}")


def compile_to_bytecode(ast: Any) -> list[Instruction]:
    compiler = VexCompiler()
    return compiler.compile(ast)