from __future__ import annotations

from typing import Any

from vex.bytecode import FunctionBytecode, Instruction, OpCode


class VexVMError(Exception):
    pass


class VexVM:
    def __init__(self) -> None:
        self.stack: list[Any] = []
        self.globals: dict[str, Any] = {}
        self.frames: list[dict[str, Any]] = []
        self.output: list[str] = []

    def push(self, value: Any) -> None:
        self.stack.append(value)

    def pop(self) -> Any:
        if not self.stack:
            raise VexVMError("Stack underflow")
        return self.stack.pop()

    def current_locals(self) -> dict[str, Any] | None:
        if not self.frames:
            return None
        return self.frames[-1]

    def load_name(self, name: str) -> Any:
        locals_ = self.current_locals()

        if locals_ is not None and name in locals_:
            return locals_[name]

        if name in self.globals:
            return self.globals[name]

        raise VexVMError(f"Undefined variable: {name}")

    def store_name(self, name: str, value: Any) -> None:
        locals_ = self.current_locals()

        if locals_ is not None:
            locals_[name] = value
        else:
            self.globals[name] = value

    def run(self, instructions: list[Instruction]) -> Any:
        return self.execute(instructions)

    def execute(self, instructions: list[Instruction]) -> Any:
        ip = 0

        while ip < len(instructions):
            instruction = instructions[ip]
            op = instruction.op
            arg = instruction.arg

            if op == OpCode.LOAD_CONST:
                self.push(arg)

            elif op == OpCode.LOAD_NAME:
                self.push(self.load_name(arg))

            elif op == OpCode.STORE_NAME:
                value = self.pop()
                self.store_name(arg, value)

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

            elif op == OpCode.CALL_FUNCTION:
                function_name = arg["name"]
                argc = arg["argc"]

                function = self.load_name(function_name)

                if not isinstance(function, FunctionBytecode):
                    raise VexVMError(f"{function_name} is not callable")

                if argc != len(function.params):
                    raise VexVMError(
                        f"{function_name} expected {len(function.params)} args but got {argc}"
                    )

                args = [self.pop() for _ in range(argc)]
                args.reverse()

                frame = dict(zip(function.params, args))
                self.frames.append(frame)

                result = self.execute(function.instructions)

                self.frames.pop()
                self.push(result)

            elif op == OpCode.RETURN_VALUE:
                return self.pop()

            else:
                raise VexVMError(f"Unknown opcode: {op}")

            ip += 1

        return None