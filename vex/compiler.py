from __future__ import annotations

from typing import Any

from vex.bytecode import FunctionBytecode, Instruction, OpCode


class VexCompilerError(Exception):
    pass


class VexCompiler:
    def __init__(self) -> None:
        self.instructions: list[Instruction] = []
        self.loop_start_stack: list[int] = []
        self.loop_break_stack: list[list[int]] = []

    def emit(self, op: str, arg: Any = None) -> int:
        self.instructions.append(Instruction(op, arg))
        return len(self.instructions) - 1

    def patch(self, index: int, arg: Any) -> None:
        self.instructions[index].arg = arg

    def compile(self, ast: Any) -> list[Instruction]:
        self.instructions = []
        self.loop_start_stack = []
        self.loop_break_stack = []
        self.compile_node(ast)
        return self.instructions

    def compile_node(self, node: Any) -> None:
        name = node.__class__.__name__

        if name == "Program":
            for statement in node.body:
                self.compile_node(statement)

        elif name == "FunctionDefinition":
            function_compiler = VexCompiler()

            for statement in node.body:
                function_compiler.compile_node(statement)

            if (
                not function_compiler.instructions
                or function_compiler.instructions[-1].op != OpCode.RETURN_VALUE
            ):
                function_compiler.emit(OpCode.LOAD_CONST, None)
                function_compiler.emit(OpCode.RETURN_VALUE)

            function = FunctionBytecode(
                name=node.name.name,
                params=[param.name for param in node.params],
                instructions=function_compiler.instructions,
            )

            self.emit(OpCode.LOAD_CONST, function)
            self.emit(OpCode.STORE_NAME, node.name.name)

        elif name == "ReturnStatement":
            if node.value is not None:
                self.compile_node(node.value)
            else:
                self.emit(OpCode.LOAD_CONST, None)
            self.emit(OpCode.RETURN_VALUE)

        elif name == "AssignmentStatement":
            self.compile_node(node.value)
            self.emit(OpCode.STORE_NAME, node.target.name)

        elif name == "PrintStatement":
            self.compile_node(node.value)
            self.emit(OpCode.PRINT)

        elif name == "IfStatement":
            self.compile_node(node.condition)
            jump_if_false_index = self.emit(OpCode.JUMP_IF_FALSE, None)

            for statement in node.body:
                self.compile_node(statement)

            if node.else_body:
                jump_over_else_index = self.emit(OpCode.JUMP, None)

                else_start = len(self.instructions)
                self.patch(jump_if_false_index, else_start)

                for statement in node.else_body:
                    self.compile_node(statement)

                after_else = len(self.instructions)
                self.patch(jump_over_else_index, after_else)
            else:
                after_if = len(self.instructions)
                self.patch(jump_if_false_index, after_if)

        elif name == "WhileStatement":
            loop_start = len(self.instructions)

            self.loop_start_stack.append(loop_start)
            self.loop_break_stack.append([])

            self.compile_node(node.condition)
            jump_if_false_index = self.emit(OpCode.JUMP_IF_FALSE, None)

            for statement in node.body:
                self.compile_node(statement)

            self.emit(OpCode.JUMP, loop_start)

            loop_end = len(self.instructions)
            self.patch(jump_if_false_index, loop_end)

            break_jumps = self.loop_break_stack.pop()
            self.loop_start_stack.pop()

            for break_index in break_jumps:
                self.patch(break_index, loop_end)

        elif name == "BreakStatement":
            if not self.loop_break_stack:
                raise VexCompilerError("'rok' can only be used inside a loop")

            break_jump_index = self.emit(OpCode.JUMP, None)
            self.loop_break_stack[-1].append(break_jump_index)

        elif name == "ContinueStatement":
            if not self.loop_start_stack:
                raise VexCompilerError("'aage' can only be used inside a loop")

            self.emit(OpCode.JUMP, self.loop_start_stack[-1])

        elif name == "LogicalExpression":
            self.compile_node(node.left)
            self.compile_node(node.right)

            if node.operator == "aur":
                self.emit(OpCode.LOGICAL_AND)
            elif node.operator == "ya":
                self.emit(OpCode.LOGICAL_OR)
            else:
                raise VexCompilerError(
                    f"Unsupported logical operator for VM: {node.operator}"
                )

        elif name == "UnaryExpression":
            self.compile_node(node.operand)

            if node.operator == "nahi":
                self.emit(OpCode.LOGICAL_NOT)
            else:
                raise VexCompilerError(
                    f"Unsupported unary operator for VM: {node.operator}"
                )

        elif name == "ListLiteral":
            for element in node.elements:
                self.compile_node(element)

            self.emit(OpCode.BUILD_LIST, len(node.elements))

        elif name == "IndexExpression":
            self.compile_node(node.collection)
            self.compile_node(node.index)
            self.emit(OpCode.GET_INDEX)

        elif name == "CallExpression":
            for argument in node.arguments:
                self.compile_node(argument)

            self.emit(
                OpCode.CALL_FUNCTION,
                {
                    "name": node.callee.name,
                    "argc": len(node.arguments),
                },
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
            elif node.operator == "==":
                self.emit(OpCode.COMPARE_EQ)
            elif node.operator == "!=":
                self.emit(OpCode.COMPARE_NE)
            elif node.operator == "<":
                self.emit(OpCode.COMPARE_LT)
            elif node.operator == "<=":
                self.emit(OpCode.COMPARE_LTE)
            elif node.operator == ">":
                self.emit(OpCode.COMPARE_GT)
            elif node.operator == ">=":
                self.emit(OpCode.COMPARE_GTE)
            else:
                raise VexCompilerError(
                    f"Unsupported binary operator for VM: {node.operator}"
                )

        else:
            raise VexCompilerError(f"Unsupported AST node for VM: {name}")


def compile_to_bytecode(ast: Any) -> list[Instruction]:
    compiler = VexCompiler()
    return compiler.compile(ast)