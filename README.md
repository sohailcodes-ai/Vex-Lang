Vex Language 🔥

«A compiler-backed programming language featuring Hinglish-inspired syntax, a custom lexer, parser, AST generator, bytecode compiler, virtual machine, Python transpilation backend, CLI tooling, and editor integrations.»

Vex is a programming language designed to make programming more approachable while teaching real language-engineering concepts.

Unlike traditional educational languages, Vex supports multiple execution backends and includes its own compiler pipeline.

---

Why Vex?

Many beginners learn programming through a language they do not naturally think in.

Vex reduces that barrier by allowing developers to write code using Hinglish-inspired keywords while still learning serious compiler and language-design concepts.

Vex is designed to teach:

- Lexical Analysis
- Parsing
- Abstract Syntax Trees (AST)
- Bytecode Compilation
- Virtual Machines
- Transpilation
- CLI Tooling
- Testing Infrastructure
- Language Design

---

Features

Language Features

- Hinglish Mode
- English Mode
- Variables
- Arithmetic Expressions
- Operator Precedence
- Parenthesized Expressions
- Conditional Statements
- If / Else Support
- Python Ecosystem Compatibility

Compiler Infrastructure

- Custom Lexer
- Custom Parser
- AST Generation
- Bytecode Compiler
- Virtual Machine
- Python Code Generator
- Token Inspection
- AST Inspection
- Bytecode Inspection

Tooling

- CLI Interface
- Project Initialization
- TOML Configuration
- VS Code Extension
- Windsurf Support
- PyPI Distribution
- Automated Unit Tests

---

Architecture

Vex currently supports two execution backends.

Python Backend

.vex Source
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

VM Backend

.vex Source
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

Complete Architecture

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
     Python Backend           VM Backend
            │                         │
            ▼                         ▼
 Python Code Generator     Bytecode Compiler
            │                         │
            ▼                         ▼
      Python Code            Vex Bytecode
            │                         │
            ▼                         ▼
    CPython Runtime       Vex Virtual Machine

---

Current Capabilities

Language Frontend

✅ Custom Lexer

✅ Custom Parser

✅ AST Generation

✅ Arithmetic Expression Parsing

✅ Operator Precedence

✅ Conditional Parsing

Python Backend

✅ Python Code Generation

✅ Runtime Execution

VM Backend

✅ Bytecode Compilation

✅ Virtual Machine

✅ Arithmetic Execution

✅ Conditional Execution

Tooling

✅ CLI Commands

✅ Project Initialization

✅ VS Code Extension

✅ Windsurf Support

✅ PyPI Package

✅ Automated Testing

---

Philosophy

Vex is not intended to replace Python.

The goal of Vex is to provide an approachable programming language while exposing developers to real compiler and language-engineering concepts.

Rather than hiding how programming languages work internally, Vex encourages developers to explore:

- Tokenization
- Parsing
- AST Construction
- Code Generation
- Bytecode Compilation
- Virtual Machine Design
- Tooling Development
- Language Ecosystem Engineering

---

Roadmap

Completed

- Lexer
- Parser
- AST Generator
- Python Backend
- Bytecode Compiler
- Virtual Machine
- Arithmetic Expressions
- Operator Precedence
- Conditional Execution
- CLI Tooling
- VS Code Extension
- Windsurf Support
- PyPI Distribution
- Automated Testing

Planned

- Function Execution in VM
- Loop Execution in VM
- Package System
- Bytecode File Output (.vbc)
- Standard Library
- Language Server Protocol (LSP)
- Static Type Checking
- Optimizer Passes
- Additional Compiler Backends

---

License

MIT License

---

Built By

Sohail Ali

GitHub: https://github.com/sohailcodes-ai

---

Vision

Vex aims to grow into a complete educational programming language ecosystem featuring multiple execution backends, modern tooling, editor integrations, package management, and developer-focused learning resources.