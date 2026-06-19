import unittest

from vex.lexer import tokenize
from vex.parser import parse
from vex.compiler import compile_to_bytecode
from vex.vm import VexVM


class TestCompilerPipeline(unittest.TestCase):
    def run_source(self, source: str):
        tokens = tokenize(source)
        ast = parse(tokens)
        bytecode = compile_to_bytecode(ast)

        vm = VexVM()
        vm.run(bytecode)

        return vm

    def test_assignment_and_print(self):
        vm = self.run_source("""
naam = "Sohail"
bolo(naam)
""")

        self.assertEqual(vm.output, ["Sohail"])

    def test_arithmetic(self):
        vm = self.run_source("""
x = 10 + 5
bolo(x)
""")

        self.assertEqual(vm.output, ["15"])

    def test_if_true(self):
        vm = self.run_source("""
age = 18

agar age >= 18:
    bolo("Adult")
""")

        self.assertEqual(vm.output, ["Adult"])

    def test_if_else(self):
        vm = self.run_source("""
age = 16

agar age >= 18:
    bolo("Adult")
warna:
    bolo("Minor")
""")

        self.assertEqual(vm.output, ["Minor"])


if __name__ == "__main__":
    unittest.main()