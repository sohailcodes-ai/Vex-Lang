from __future__ import annotations

from typing import Any

from vex.bytecode import Instruction, OpCode


class VexVMError(Exception):
    pass


class VexVM:
    def __init__(self) -> None:
        self.stack: list[Any] = []
        self.globals: dict[str, Any] = {}
        self.output: list[str] = []

    def push(self, value: Any) -> None:
        self.stack.append(value)

    def pop(self) -> Any:
        if not self.stack:
            raise VexVMError("Stack underflow")
        return self.stack.pop()

    def run(self, instructions: list[Instruction]) -> Any:
        ip = 0

        while ip < len(instructions):
            instruction = instructions[ip]
            op = instruction.op
            arg = instruction.arg

            if op == OpCode.LOAD_CONST:
                self.push(arg)

            elif op == OpCode.LOAD_NAME:
                if arg not in self.globals:
                    raise VexVMError(f"Undefined variable: {arg}")
                self.push(self.globals[arg])

            elif op == OpCode.STORE_NAME:
                value = self.pop()
                self.globals[arg] = value

            elif op == OpCode.PRINT:
                value = self.pop()
                text = str(value)
                self.output.append(text)
                print(text)

            elif op == OpCode.POP_TOP:
                self.pop()

            elif op == OpCode.BINARY_ADD:
                right = self.pop()
                left = self.pop()
                self.push(left + right)

            elif op == OpCode.BINARY_SUB:
                right = self.pop()
                left = self.pop()
                self.push(left - right)

            elif op == OpCode.BINARY_MUL:
                right = self.pop()
                left = self.pop()
                self.push(left * right)

            elif op == OpCode.BINARY_DIV:
                right = self.pop()
                left = self.pop()
                self.push(left / right)

            elif op == OpCode.COMPARE_EQ:
                right = self.pop()
                left = self.pop()
                self.push(left == right)

            elif op == OpCode.COMPARE_NE:
                right = self.pop()
                left = self.pop()
                self.push(left != right)

            elif op == OpCode.COMPARE_LT:
                right = self.pop()
                left = self.pop()
                self.push(left < right)

            elif op == OpCode.COMPARE_LTE:
                right = self.pop()
                left = self.pop()
                self.push(left <= right)

            elif op == OpCode.COMPARE_GT:
                right = self.pop()
                left = self.pop()
                self.push(left > right)

            elif op == OpCode.COMPARE_GTE:
                right = self.pop()
                left = self.pop()
                self.push(left >= right)

            elif op == OpCode.JUMP:
                ip = arg
                continue

            elif op == OpCode.JUMP_IF_FALSE:
                condition = self.pop()
                if not condition:
                    ip = arg
                    continue

            elif op == OpCode.RETURN_VALUE:
                return self.pop()

            else:
                raise VexVMError(f"Unknown opcode: {op}")

            ip += 1

        return None