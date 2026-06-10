# Vex Repository Audit

## Summary

Vex is a lightweight Python transpiler: `.vex` source with optional Hinglish keywords is converted to Python and executed via `exec`. The package ships on PyPI as `vex-lang` with entry point `vex = vex.cli:main`.

## Pre-refactor layout

| File | Role |
|------|------|
| `vex/transpiler.py` | Mode detection, keyword swap, f-string fixups |
| `vex/keywords.py` | Hinglish → Python keyword map |
| `vex/runner.py` | Execute transpiled code, print errors |
| `vex/cli.py` | `vex run`, `vex version` |
| `vex/lexer.py` | Stub (not used) |
| `vex/parser.py` | Stub (not used) |
| `main.py` | Duplicate local CLI entry |

## Issues found

1. **Scattered responsibilities** — transpilation, mode logic, and errors lived in ad-hoc modules.
2. **Duplicate CLI** — `main.py` and `vex/cli.py` duplicated run logic.
3. **No tests** — translation behavior was undocumented and unverified.
4. **No project scaffolding** — no way to bootstrap a new Vex project from the CLI.
5. **Unused stubs** — `lexer.py` and `parser.py` are placeholders for a future AST pipeline.

## Refactored layout

```
vex/
├── __init__.py      # Public API: transpile, run, __version__
├── cli.py           # vex run | init | version
├── translator.py    # Vex → Python transpilation
├── modes.py         # Mode detection + keyword maps
├── errors.py        # Error types and message formatting
├── runtime.py       # Execute transpiled Python
├── transpiler.py    # Shim → translator (PyPI compat)
├── runner.py        # Shim → runtime (PyPI compat)
├── keywords.py      # Shim → modes (PyPI compat)
├── lexer.py         # Future: tokenization
└── parser.py        # Future: AST
tests/
└── test_translator.py
examples/
└── hello.vex
```

## Preserved behavior

- `pip install vex-lang` → `vex` command unchanged
- `from vex.transpiler import transpile` still works
- `from vex.runner import run` still works
- Hinglish keyword mapping and f-string auto-conversion unchanged

## New behavior

- `vex init <project_name>` — creates `<project_name>/main.vex` with a starter template
