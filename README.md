Vex Language 🔥

«A compiler-backed programming language with Hinglish-inspired syntax, custom lexer, parser, AST generation, bytecode compiler, virtual machine, Python transpilation backend, CLI tooling, and editor support.»

Vex is a programming language designed to make coding more approachable while exposing developers to real language-engineering concepts.

Vex supports two execution backends:

Vex Source → Lexer → Parser → AST → Python Backend → Python Runtime
Vex Source → Lexer → Parser → AST → Bytecode Compiler → Vex VM

This means Vex is no longer just a transpiler. It includes its own frontend pipeline, bytecode compiler, and virtual machine while still preserving compatibility with the Python ecosystem.

---

Why Vex?

Most beginners learn programming through languages they do not naturally think in.

Vex reduces that barrier by allowing developers to write code using Hinglish-inspired keywords while still learning serious programming language concepts such as:

- Lexical Analysis
- Parsing
- AST Generation
- Bytecode Compilation
- Virtual Machine Execution
- Python Transpilation
- CLI Tooling
- Testing Infrastructure
- Editor Integration

Vex is both an approachable programming language and a practical language-engineering project.

---

Features

Language Features

- Hinglish and English modes
- Variables
- Arithmetic expressions
- Operator precedence
- Parenthesized expressions
- Conditionals
- If statements
- Print statements
- Python ecosystem compatibility
- Auto f-string conversion

Compiler Pipeline

- Custom Lexer
- Custom Parser
- AST Generation
- Token Inspection
- AST Inspection
- Python Code Generation
- Bytecode Generation
- VM Execution

Tooling

- CLI Interface
- Project Initialization
- "vex.toml" configuration
- VS Code Extension
- Windsurf Support
- PyPI Distribution
- Automated Unit Tests

---

Architecture

Vex follows a compiler-inspired architecture.

Vex Source
     ↓
Lexer
     ↓
Tokens
     ↓
Parser
     ↓
AST
     ↓
 ┌───────────────┬──────────────────┐
 │ Python Backend│ Bytecode Compiler│
 │       ↓       │        ↓         │
 │ Python Runtime│      Vex VM      │
 └───────────────┴──────────────────┘

Vex currently supports both:

1. Python transpilation backend
2. Native Vex bytecode VM backend

---

Installation

pip install vex-lang

Python 3.8+ is required.

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

Run project:

cd my_app
vex run

Or execute directly:

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

Run using the Vex VM backend:

python -m vex.cli run vm_demo.vex --backend vm

Output:

Sohail
15
20
30

---

Bytecode Inspection

python -m vex.cli bytecode vm_demo.vex

Example output:

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

---

Modes

Declare the mode at the top of your file.

#mode hinglish

or

#mode english

---

Keyword Reference

Vex| Python
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
cheez| class
khud| self
aur| and
ya| or
nahi| not
chalne_de| pass
rok| break
aage| continue

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

Token Inspection

vex tokens hello.vex

Example:

KEYWORD('agar')
IDENTIFIER('age')
OPERATOR('>=')
NUMBER('18')
COLON(':')
EOF('')

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

Bytecode Compilation

python -m vex.cli bytecode hello.vex

Example:

0000  LOAD_CONST 18
0001  STORE_NAME 'age'
0002  LOAD_NAME 'age'
0003  LOAD_CONST 18
0004  COMPARE_GTE
0005  JUMP_IF_FALSE 8
0006  LOAD_CONST 'Adult'
0007  PRINT

---

CLI Commands

Command| Description
"vex run [file.vex]"| Execute a Vex file
"vex run [file.vex] --backend python"| Run using Python backend
"vex run [file.vex] --backend vm"| Run using Vex VM backend
"vex translate <file.vex>"| Generate Python source
"vex tokens <file.vex>"| Display lexer tokens
"vex ast <file.vex>"| Display generated AST
"vex bytecode <file.vex>"| Display generated bytecode
"vex init <project_name>"| Create a new project
"vex version"| Display installed version

---

VM Instructions

The Vex VM currently supports:

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

---

VS Code & Windsurf Extension

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

Vex consists of more than the language itself.

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
- Documentation
- Testing Infrastructure

---

Project Structure

vex/
├── cli.py
├── config.py
├── translator.py
├── lexer.py
├── parser.py
├── ast_nodes.py
├── tokens.py
├── bytecode.py
├── compiler.py
├── vm.py
├── modes.py
├── errors.py
├── runtime.py
├── transpiler.py
├── runner.py
└── keywords.py

tests/
├── test_translator.py
├── test_lexer.py
├── test_parser.py
├── test_ast.py
├── test_config.py
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

---

Roadmap

Completed

- [x] Custom Lexer
- [x] Custom Parser
- [x] AST Generation
- [x] Python Transpilation Backend
- [x] Bytecode Compiler
- [x] Vex Virtual Machine
- [x] Arithmetic Expression Parsing
- [x] Operator Precedence
- [x] VM Control Flow
- [x] CLI Tooling
- [x] Project Configuration
- [x] VS Code Extension
- [x] Windsurf Support
- [x] PyPI Distribution
- [x] Automated Testing

Planned

- [ ] Full "warna" else support in VM backend
- [ ] "warna_agar" elif support
- [ ] Function execution in VM backend
- [ ] Loop execution in VM backend
- [ ] Package system documentation
- [ ] ".vbc" bytecode file output
- [ ] Standard library expansion
- [ ] Language Server Protocol support
- [ ] Static type checking
- [ ] Optimizer passes

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

The goal of Vex is to build an approachable programming language that also teaches real language-engineering concepts such as lexical analysis, parsing, AST construction, transpilation, bytecode compilation, virtual machine execution, testing, tooling, and ecosystem development.

Vex aims to grow into a complete educational language ecosystem with multiple execution backends, package tooling, editor support, documentation, and developer-friendly learning resources.