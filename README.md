# Vex Language 🔥

A compiler-backed programming language featuring Hinglish-inspired syntax, a custom lexer, parser, AST generator, bytecode compiler, virtual machine, Python execution backend, CLI tooling, testing infrastructure, PyPI distribution, and editor integrations.

Vex is a programming language that combines familiar Hinglish-inspired syntax with a real language toolchain.

Vex is not only a syntax translator. It includes its own frontend pipeline, bytecode compiler, virtual machine, Python backend, command-line interface, project configuration system, tests, and editor support.

Vex currently supports two execution backends:

Python Backend:
Vex Source → Lexer → Parser → AST → Python Code → CPython Runtime

VM Backend:
Vex Source → Lexer → Parser → AST → Vex Bytecode → Vex Virtual Machine

---

Why Vex?

Most programming languages use English-based syntax by default.

Vex uses Hinglish-inspired keywords while still preserving access to Python-style programming concepts and tooling.

The goal is simple:

- Keep syntax familiar for Hinglish-speaking developers
- Provide a real compiler-style architecture
- Support Python backend execution
- Support VM backend execution
- Expose internal stages like tokens, AST, and bytecode
- Provide installable tooling through PyPI and editor integrations

---

Features

Language Features

- Hinglish and English modes
- Variables
- Arithmetic expressions
- Operator precedence
- Parenthesized expressions
- Conditional statements
- Print statements
- Python ecosystem compatibility
- Auto f-string conversion

Compiler and Runtime Features

- Custom Lexer
- Custom Parser
- AST Generation
- Python Code Generation
- Bytecode Compilation
- Virtual Machine Execution
- Token Inspection
- AST Inspection
- Bytecode Inspection
- Runtime Execution

Tooling

- CLI Interface
- Project Initialization
- "vex.toml" Configuration
- VS Code Extension
- Windsurf Support
- PyPI Distribution
- Automated Unit Tests

---

Architecture

Vex follows a dual-backend architecture.

                    Vex Source
                         │
                         ▼
                      Lexer
                         │
                         ▼
                      Tokens
                         │
                         ▼
                      Parser
                         │
                         ▼
                        AST
                         │
            ┌────────────┴────────────┐
            │                         │
            ▼                         ▼
     Python Backend             VM Backend
            │                         │
            ▼                         ▼
 Python Code Generator       Bytecode Compiler
            │                         │
            ▼                         ▼
      Python Code              Vex Bytecode
            │                         │
            ▼                         ▼
    CPython Runtime         Vex Virtual Machine

Python Backend Flow

.vex File
   ↓
Lexer
   ↓
Parser
   ↓
AST
   ↓
Python Code Generator
   ↓
Python Source
   ↓
CPython Runtime

VM Backend Flow

.vex File
   ↓
Lexer
   ↓
Parser
   ↓
AST
   ↓
Bytecode Compiler
   ↓
Vex Bytecode
   ↓
Vex Virtual Machine

---

Installation

pip install vex-lang

Python 3.8+ is recommended.

---

Quick Start

Create a new project:

vex init my_app

Generated structure:

my_app/
├── main.vex
└── vex.toml

Example configuration:

name = "my_app"
version = "0.1.0"
mode = "hinglish"
entry = "main.vex"

Run the project:

cd my_app
vex run

Or execute a file directly:

vex run my_app/main.vex

---

Your First Program

#mode hinglish

naam = "Sohail"

bolo("Yo {naam}!")

age = 18

agar age >= 18:
    bolo("Adult")

Run:

vex run hello.vex

Output:

Yo Sohail!
Adult

---

Running With Backends

Python Backend

vex run hello.vex --backend python

The Python backend transpiles Vex source code into Python and executes it using the Python runtime.

VM Backend

vex run hello.vex --backend vm

The VM backend compiles Vex source code into bytecode and executes it using the Vex Virtual Machine.

---

Modes

Declare the mode at the top of your file.

#mode hinglish

or

#mode english

---

Keyword Reference

Vex| Python Equivalent
bolo| print
dikhao| print
agar| if
warna| else
warna_agar| elif
jabtak| while
har| for
mai| in
kaam| def
wapas| return
aao| import
jaise| as
pakdo| try
chodo| except
sahi| True
galat| False
kuch_nahi| None
khali| None
cheez| class
khud| self
aur| and
ya| or
nahi| not
chalne_de| pass
rok| break
aage| continue

---

Variables

#mode hinglish

naam = "Sohail"
age = 18

bolo(naam)
bolo(age)

Output:

Sohail
18

---

Arithmetic Expressions

#mode hinglish

x = 10 + 5
y = 10 + 5 * 2
z = (10 + 5) * 2

bolo(x)
bolo(y)
bolo(z)

Output:

15
20
30

Vex supports operator precedence and parenthesized expressions.

---

Conditionals

#mode hinglish

age = 18

agar age >= 18:
    bolo("Adult")

Output:

Adult

---

Functions

#mode hinglish

kaam greet(naam):
    wapas "Assalamualiykum Habibi " + naam

bolo(greet("Sohail"))

Output:

Assalamualiykum Habibi Sohail

---

Loops

#mode hinglish

har i mai range(5):
    bolo(i)

Output:

0
1
2
3
4

---

Error Handling

#mode hinglish

pakdo:
    bolo(10 / 0)

chodo ZeroDivisionError:
    bolo("Zero se divide nahi kar sakte!")

---

NumPy Example

#mode hinglish

aao numpy jaise np

numbers = [1, 2, 3, 4, 5]

bolo(np.mean(numbers))
bolo(np.sum(numbers))

Output:

3.0
15

---

Language Internals

Vex exposes internal compiler stages directly through the CLI.

This makes it possible to inspect tokens, AST output, generated Python, and generated bytecode.

---

Token Inspection

vex tokens hello.vex

Example output:

KEYWORD('agar') line=5, col=1
IDENTIFIER('age') line=5, col=6
OPERATOR('>=') line=5, col=10
NUMBER('18') line=5, col=13
COLON(':') line=5, col=15
EOF('') line=7, col=1

---

AST Inspection

vex ast hello.vex

Input:

#mode hinglish

age = 18

agar age >= 18:
    bolo("Adult")

Output:

Program
  AssignmentStatement
    Identifier(age)
    NumberLiteral(18)
  IfStatement
    BinaryExpression(>=)
      Identifier(age)
      NumberLiteral(18)
    Body
      PrintStatement
        StringLiteral('Adult')

---

Python Translation

vex translate hello.vex

Output:

age = 18

if age >= 18:
    print("Adult")

---

Bytecode Inspection

vex bytecode hello.vex

Example output:

0000  LOAD_CONST 18
0001  STORE_NAME 'age'
0002  LOAD_NAME 'age'
0003  LOAD_CONST 18
0004  COMPARE_GTE
0005  JUMP_IF_FALSE 8
0006  LOAD_CONST 'Adult'
0007  PRINT

---

VM Backend Example

#mode hinglish

naam = "Sohail"
bolo(naam)

x = 10 + 5
bolo(x)

y = 10 + 5 * 2
bolo(y)

z = (10 + 5) * 2
bolo(z)

Run using the VM backend:

vex run vm_demo.vex --backend vm

Output:

Sohail
15
20
30

Inspect bytecode:

vex bytecode vm_demo.vex

Example bytecode:

0000  LOAD_CONST 'Sohail'
0001  STORE_NAME 'naam'
0002  LOAD_NAME 'naam'
0003  PRINT
0004  LOAD_CONST 10
0005  LOAD_CONST 5
0006  BINARY_ADD
0007  STORE_NAME 'x'
0008  LOAD_NAME 'x'
0009  PRINT
0010  LOAD_CONST 10
0011  LOAD_CONST 5
0012  LOAD_CONST 2
0013  BINARY_MUL
0014  BINARY_ADD
0015  STORE_NAME 'y'
0016  LOAD_NAME 'y'
0017  PRINT
0018  LOAD_CONST 10
0019  LOAD_CONST 5
0020  BINARY_ADD
0021  LOAD_CONST 2
0022  BINARY_MUL
0023  STORE_NAME 'z'
0024  LOAD_NAME 'z'
0025  PRINT

---

CLI Commands

Command| Description
"vex run [file.vex]"| Execute a Vex file
"vex run [file.vex] --backend python"| Execute using the Python backend
"vex run [file.vex] --backend vm"| Execute using the Vex VM backend
"vex translate <file.vex>"| Generate Python source
"vex tokens <file.vex>"| Display lexer tokens
"vex ast <file.vex>"| Display generated AST
"vex bytecode <file.vex>"| Display generated bytecode
"vex init <project_name>"| Create a new Vex project
"vex version"| Display installed version

---

Vex VM Instructions

The Vex Virtual Machine currently supports bytecode instructions such as:

LOAD_CONST
LOAD_NAME
STORE_NAME
PRINT
POP_TOP
RETURN_VALUE

BINARY_ADD
BINARY_SUB
BINARY_MUL
BINARY_DIV

COMPARE_EQ
COMPARE_NE
COMPARE_LT
COMPARE_LTE
COMPARE_GT
COMPARE_GTE

JUMP
JUMP_IF_FALSE

These instructions allow the VM backend to execute variables, arithmetic, comparisons, print statements, and conditional control flow.

---

VS Code & Windsurf Extension

Vex includes editor tooling support.

Features:

- Syntax Highlighting
- File Icons
- Run Button
- Vex File Recognition
- Hinglish Keyword Support

Installation:

1. Open Extensions
2. Search for Vex Language
3. Install
4. Create a ".vex" file
5. Start coding

---

Ecosystem

Vex consists of more than the language syntax.

- Vex Language
- Python Backend
- Bytecode Compiler
- Vex Virtual Machine
- PyPI Package
- VS Code Extension
- Windsurf Support
- Lexer
- Parser
- AST Generator
- CLI Tooling
- Project Configuration
- Documentation
- Testing Infrastructure

---

Project Structure

vex/
├── __init__.py
├── ast_nodes.py
├── bytecode.py
├── cli.py
├── compiler.py
├── config.py
├── errors.py
├── keywords.py
├── lexer.py
├── modes.py
├── parser.py
├── runner.py
├── runtime.py
├── tokens.py
├── translator.py
├── transpiler.py
└── vm.py

tests/
├── __init__.py
├── test_ast.py
├── test_config.py
├── test_lexer.py
├── test_parser.py
├── test_translator.py
└── test_vm.py

examples/
└── hello.vex

---

Testing

Run all tests:

python -m unittest discover -s tests

Current test suite:

26+ passing tests

---

Development Setup

git clone https://github.com/sohailcodes-ai/Vex-Lang

cd Vex-Lang

pip install -e ".[dev]"

python -m unittest discover -s tests

Run CLI locally:

python -m vex.cli version
python -m vex.cli run examples/hello.vex
python -m vex.cli bytecode examples/hello.vex

---

Roadmap

Completed

- [x] Custom Lexer
- [x] Custom Parser
- [x] AST Generation
- [x] Python Backend
- [x] Bytecode Compiler
- [x] Virtual Machine
- [x] Token Inspection
- [x] AST Inspection
- [x] Bytecode Inspection
- [x] CLI Tooling
- [x] Project Initialization
- [x] VS Code Extension
- [x] Windsurf Support
- [x] PyPI Distribution
- [x] Automated Testing

Planned

- [ ] Expanded VM language support
- [ ] Function execution in VM backend
- [ ] Loop execution in VM backend
- [ ] Package system documentation
- [ ] ".vbc" bytecode file output
- [ ] Standard library expansion
- [ ] Static type checking
- [ ] Optimizer passes
- [ ] Language Server Protocol support
- [ ] Additional compiler backends

---

Project Status

Vex is under active development.

The project currently supports:

- Source-to-Python execution
- Source-to-bytecode execution
- VM-based execution
- CLI inspection tools
- Editor tooling
- PyPI installation
- Unit testing

The VM backend is still evolving and may not support every feature available through the Python backend yet.

---

Links

GitHub:
https://github.com/sohailcodes-ai/Vex-Lang

PyPI:
https://pypi.org/project/vex-lang

VS Code Marketplace:
https://marketplace.visualstudio.com/items?itemName=sohailcodes-ai.vex-lang

---

License

Vex is released under the MIT License.

---

Built By

Sohail Ali

GitHub:
https://github.com/sohailcodes-ai

---

Vision

Vex is not just a Hinglish syntax layer over Python.

The goal of Vex is to grow into a complete programming language ecosystem with multiple execution backends, compiler infrastructure, VM execution, developer tooling, package support, editor integrations, and strong documentation.

Vex exists to make programming syntax feel familiar while still building on real language engineering foundations.