import unittest

from vex.bytecode import Instruction, OpCode
from vex.vm import VexVM


class TestVexVM(unittest.TestCase):
    def test_print_constant(self):
        vm = VexVM()

        instructions = [
            Instruction(OpCode.LOAD_CONST, "Hello Vex VM"),
            Instruction(OpCode.PRINT),
        ]

        vm.run(instructions)

        self.assertEqual(vm.output, ["Hello Vex VM"])

    def test_variable_assignment(self):
        vm = VexVM()

        instructions = [
            Instruction(OpCode.LOAD_CONST, 18),
            Instruction(OpCode.STORE_NAME, "age"),
        ]

        vm.run(instructions)

        self.assertEqual(vm.globals["age"], 18)

    def test_load_variable_and_print(self):
        vm = VexVM()

        instructions = [
            Instruction(OpCode.LOAD_CONST, "Sohail"),
            Instruction(OpCode.STORE_NAME, "naam"),
            Instruction(OpCode.LOAD_NAME, "naam"),
            Instruction(OpCode.PRINT),
        ]

        vm.run(instructions)

        self.assertEqual(vm.output, ["Sohail"])

    def test_binary_addition(self):
        vm = VexVM()

        instructions = [
            Instruction(OpCode.LOAD_CONST, 10),
            Instruction(OpCode.LOAD_CONST, 5),
            Instruction(OpCode.BINARY_ADD),
            Instruction(OpCode.PRINT),
        ]

        vm.run(instructions)

        self.assertEqual(vm.output, ["15"])

    def test_arithmetic_precedence_bytecode_order(self):
        vm = VexVM()

        instructions = [
            Instruction(OpCode.LOAD_CONST, 10),
            Instruction(OpCode.LOAD_CONST, 5),
            Instruction(OpCode.LOAD_CONST, 2),
            Instruction(OpCode.BINARY_MUL),
            Instruction(OpCode.BINARY_ADD),
            Instruction(OpCode.PRINT),
        ]

        vm.run(instructions)

        self.assertEqual(vm.output, ["20"])

    def test_parenthesized_arithmetic_bytecode_order(self):
        vm = VexVM()

        instructions = [
            Instruction(OpCode.LOAD_CONST, 10),
            Instruction(OpCode.LOAD_CONST, 5),
            Instruction(OpCode.BINARY_ADD),
            Instruction(OpCode.LOAD_CONST, 2),
            Instruction(OpCode.BINARY_MUL),
            Instruction(OpCode.PRINT),
        ]

        vm.run(instructions)

        self.assertEqual(vm.output, ["30"])

    def test_compare_gte(self):
        vm = VexVM()

        instructions = [
            Instruction(OpCode.LOAD_CONST, 18),
            Instruction(OpCode.LOAD_CONST, 18),
            Instruction(OpCode.COMPARE_GTE),
        ]

        vm.run(instructions)

        self.assertEqual(vm.stack[-1], True)

    def test_compare_lt(self):
        vm = VexVM()

        instructions = [
            Instruction(OpCode.LOAD_CONST, 10),
            Instruction(OpCode.LOAD_CONST, 18),
            Instruction(OpCode.COMPARE_LT),
        ]

        vm.run(instructions)

        self.assertEqual(vm.stack[-1], True)

    def test_jump_if_false_skips_if_body(self):
        vm = VexVM()

        instructions = [
            Instruction(OpCode.LOAD_CONST, False),
            Instruction(OpCode.JUMP_IF_FALSE, 4),
            Instruction(OpCode.LOAD_CONST, "wrong"),
            Instruction(OpCode.PRINT),
            Instruction(OpCode.LOAD_CONST, "correct"),
            Instruction(OpCode.PRINT),
        ]

        vm.run(instructions)

        self.assertEqual(vm.output, ["correct"])

    def test_unconditional_jump(self):
        vm = VexVM()

        instructions = [
            Instruction(OpCode.JUMP, 3),
            Instruction(OpCode.LOAD_CONST, "wrong"),
            Instruction(OpCode.PRINT),
            Instruction(OpCode.LOAD_CONST, "correct"),
            Instruction(OpCode.PRINT),
        ]

        vm.run(instructions)

        self.assertEqual(vm.output, ["correct"])


if __name__ == "__main__":
    unittest.main()