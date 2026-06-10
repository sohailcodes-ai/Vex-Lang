# Vex Language 🔥

> A transpiler-based programming language with Hinglish syntax, custom lexer, parser, AST generation, editor tooling, and Python code generation.

Vex is a programming language designed to make coding more approachable for Hinglish-speaking developers while preserving the power of Python.

Vex source code is transpiled into Python and executed using the Python runtime. Alongside transpilation, Vex includes its own lexer, parser, AST generation pipeline, CLI tooling, testing infrastructure, and editor integrations.

---

## Why Vex?

Python is powerful, but many beginners are introduced to programming through a language they do not naturally think in.

Vex reduces that barrier.

Write code using Hinglish keywords while retaining access to the entire Python ecosystem.

### Features

* Hinglish and English modes
* Python ecosystem compatibility
* Custom Lexer
* Custom Parser
* AST Generation
* Token Inspection
* AST Inspection
* Python Code Generation
* Runtime Execution
* VS Code Extension
* Windsurf Support
* PyPI Distribution
* Automated Unit Tests
* Auto f-string conversion

---

## Architecture

Vex follows a compiler-inspired architecture.

```text
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
Python Code Generation
     ↓
Python Runtime
```

Although Vex currently transpiles to Python, it includes its own frontend language pipeline consisting of lexical analysis, parsing, and abstract syntax tree generation.

---

## Installation

```bash
pip install vex-lang
```

Python must be installed beforehand.

---

## Quick Start

Create a new project:

```bash
vex init my_app
```

Generated structure:

```text
my_app/
├── main.vex
└── vex.toml
```

Example configuration:

```toml
name = "my_app"
version = "0.1.0"
mode = "hinglish"
entry = "main.vex"
```

Run project:

```bash
cd my_app
vex run
```

Or execute directly:

```bash
vex run my_app/main.vex
```

---

## Your First Program

```vex
#mode hinglish

naam = "Sohail"

bolo "Yo {naam}!"

agar True:
    bolo "Vex chal raha hai!"
```

Run:

```bash
vex run hello.vex
```

Output:

```text
Yo Sohail!
Vex chal raha hai!
```

---

## Modes

Declare the mode at the top of your file.

```vex
#mode hinglish
```

or

```vex
#mode english
```

---

## Keyword Reference

| Vex        | Python   |
| ---------- | -------- |
| bolo       | print    |
| dikhao     | print    |
| agar       | if       |
| warna      | else     |
| warna_agar | elif     |
| jabtak     | while    |
| har        | for      |
| mai        | in       |
| kaam       | def      |
| wapas      | return   |
| aao        | import   |
| jaise      | as       |
| pakdo      | try      |
| chodo      | except   |
| sahi       | True     |
| galat      | False    |
| kuch_nahi  | None     |
| cheez      | class    |
| khud       | self     |
| aur        | and      |
| ya         | or       |
| nahi       | not      |
| chalne_de  | pass     |
| rok        | break    |
| aage       | continue |

---

## Functions

```vex
#mode hinglish

kaam greet(naam):
    wapas "Assalamualiykum Habibi " + naam

bolo greet("Sohail")
```

Output:

```text
Assalamualiykum Habibi Sohail
```

---

## Loops

```vex
#mode hinglish

har i mai range(5):
    bolo i
```

Output:

```text
0
1
2
3
4
```

---

## Error Handling

```vex
#mode hinglish

pakdo:
    bolo 10 / 0

chodo ZeroDivisionError:
    bolo "Zero se divide nahi kar sakte!"
```

---

## NumPy Example

```vex
#mode hinglish

aao numpy jaise np

numbers = [1, 2, 3, 4, 5]

bolo np.mean(numbers)
bolo np.sum(numbers)
```

Output:

```text
3.0
15
```

---

## Language Internals

### Token Inspection

```bash
vex tokens hello.vex
```

Example:

```text
KEYWORD('agar')
IDENTIFIER('age')
OPERATOR('>=')
NUMBER('18')
COLON(':')
EOF('')
```

---

### AST Inspection

```bash
vex ast hello.vex
```

Input:

```vex
#mode hinglish

age = 18

agar age >= 18:
    dikhao("Adult")
```

Output:

```text
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
```

---

### Python Translation

```bash
vex translate hello.vex
```

Output:

```python
age = 18

if age >= 18:
    print("Adult")
```

---

### Execution

```bash
vex run hello.vex
```

Output:

```text
Adult
```

---

## CLI Commands

| Command                  | Description               |
| ------------------------ | ------------------------- |
| vex run [file.vex]       | Execute a Vex file        |
| vex translate <file.vex> | Generate Python source    |
| vex tokens <file.vex>    | Display lexer tokens      |
| vex ast <file.vex>       | Display generated AST     |
| vex init <project_name>  | Create a new project      |
| vex version              | Display installed version |

---

## VS Code & Windsurf Extension

Features:

* Syntax Highlighting
* File Icons
* Run Button
* Vex File Recognition
* Hinglish Keyword Support

Installation:

1. Open Extensions
2. Search for **Vex Language**
3. Install
4. Create a `.vex` file
5. Start coding

---

## Ecosystem

Vex consists of more than the language itself.

* Vex Language
* PyPI Package
* VS Code Extension
* Windsurf Support
* Lexer
* Parser
* AST Generator
* CLI Tooling
* Documentation
* Testing Infrastructure

---

## Project Structure

```text
vex/
├── cli.py
├── config.py
├── translator.py
├── lexer.py
├── parser.py
├── ast_nodes.py
├── tokens.py
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

examples/
└── hello.vex
```

---

## Testing

Run all tests:

```bash
python -m unittest discover -s tests
```

Current test suite:

```text
23+ passing tests
```

---

## Development Setup

```bash
git clone https://github.com/sohailcodes-ai/Vex-Lang

cd Vex-Lang

pip install -e ".[dev]"

python -m unittest discover -s tests
```

---

## Links

GitHub:
https://github.com/sohailcodes-ai/Vex-Lang

PyPI:
https://pypi.org/project/vex-lang

VS Code Marketplace:
https://marketplace.visualstudio.com/items?itemName=sohailcodes-ai.vex-lang

---

## Built By

**Sohail Ali**

GitHub:
https://github.com/sohailcodes-ai

---

### Vision

Vex aims to make programming more accessible while exposing learners to real language-engineering concepts such as lexical analysis, parsing, AST generation, transpilation, testing, tooling, and ecosystem development.
