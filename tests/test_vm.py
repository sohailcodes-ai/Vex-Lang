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


if __name__ == "__main__":
    unittest.main()