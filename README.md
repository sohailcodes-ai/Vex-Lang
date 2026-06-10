# Vex 🔥

> A Python-powered programming language with Hinglish/English dual mode.

Vex is not a replacement for Python. It's a more comfortable way to write it.
Write code in Hinglish or English — Vex converts it to Python and runs it.
Every library, every feature — nothing changes under the hood.

## Why Vex?

Python is powerful — but for many Indian beginners, English syntax is a barrier.
Vex removes that barrier. Same Python power, just in a language that feels natural.

- Full Python ecosystem — NumPy, Pandas, everything works
- Hinglish or English keywords — your choice
- Auto f-strings — `{variable}` just works inside strings, no `f""` needed
- Readable error messages
- VSCode/Windsurf extension with syntax highlighting and run button

## Install

```bash
pip install vex-lang
```

Python must be installed first.

## Quick Start

Scaffold a new project:

```bash
vex init my_app
```

This creates:

```
my_app/
├── main.vex
└── vex.toml
```

`vex.toml` holds project settings:

```toml
name = "my_app"
version = "0.1.0"
mode = "hinglish"
entry = "main.vex"
```

Run it from the project folder:

```bash
cd my_app
vex run
```

Or pass a file directly:

```bash
vex run my_app/main.vex
vex run examples/hello.vex
```

## Your First File

Create a file called `hello.vex` and write:

```
#mode hinglish

naam = "Sohail"
bolo "Yo {naam}!"

agar True:
    bolo "Vex chal raha hai!"
```

Run it:

```bash
vex run hello.vex
```

To see the generated Python without running it:

```bash
vex translate examples/hello.vex
```

Output:
```
Yo Sohail!
Vex chal raha hai!
```
## Modes

Declare mode on the first line of your file:

```
#mode hinglish    ← Hinglish keywords
#mode english     ← English Python-like keywords
```
## Keyword Reference

| Vex (Hinglish) | Python |
|----------------|--------|
| `bolo` | `print` |
| `agar` | `if` |
| `warna` | `else` |
| `warna_agar` | `elif` |
| `jabtak` | `while` |
| `har` | `for` |
| `mai` | `in` |
| `kaam` | `def` |
| `wapas` | `return` |
| `aao` | `import` |
| `jaise` | `as` |
| `pakdo` | `try` |
| `chodo` | `except` |
| `sahi` | `True` |
| `galat` | `False` |
| `kuch_nahi` | `None` |
| `cheez` | `class` |
| `khud` | `self` |
| `aur` | `and` |
| `ya` | `or` |
| `nahi` | `not` |
| `rok` | `break` |
| `aage` | `continue` |
| `chalne_de` | `pass` |
## Real Example — With NumPy

```
#mode hinglish

aao numpy jaise np

numbers = [1, 2, 3, 4, 5]
bolo np.mean(numbers)
bolo np.sum(numbers)
```

Output:
```
3.0
15
```
## Functions

```
#mode hinglish

kaam greet(naam):
    wapas "Assalamualiykum Habibi" + naam

bolo greet("Sohail")
```

Output:
```
Assalamualiykum Habibi Sohail
```
## Loops

```
#mode hinglish

har i mai range(5):
    bolo i
```
Output:
```
0
1
2
3
4

## Error Handling

```
#mode hinglish

pakdo:
    bolo 10 / 0
chodo ZeroDivisionError:
    bolo "Zero se divide nahi kar sakte!"
```
## VSCode / Windsurf Extension

1. Search **"Vex Language"** in extensions
2. Install
3. Create a `.vex` file
4. Click **▶** or press `Ctrl+Shift+R` to run

Syntax highlighting, file icons, and run support included.

## Project Structure

```
vex/
├── cli.py           # CLI: vex run | translate | init | version
├── config.py        # vex.toml project configuration
├── translator.py    # Vex → Python transpilation
├── modes.py         # Hinglish/English mode + keywords
├── errors.py        # Error types and messages
├── runtime.py       # Execute transpiled code
├── transpiler.py    # Compatibility shim (legacy import path)
├── runner.py        # Compatibility shim (legacy import path)
└── keywords.py      # Compatibility shim (legacy import path)
tests/
└── test_translator.py
examples/
└── hello.vex
```

## CLI Commands

| Command | Description |
|---------|-------------|
| `vex run [file.vex]` | Run entry from `vex.toml`, or the given file |
| `vex translate <file.vex>` | Transpile a Vex file and print Python to stdout |
| `vex init <project_name>` | Create a new project with `main.vex` and `vex.toml` |
| `vex version` | Print installed Vex version |

## Development

```bash
git clone https://github.com/sohailcodes-ai/Vex-Lang
cd Vex-Lang
pip install -e ".[dev]"
python -m unittest discover -s tests
```

## Links

- PyPI: [pypi.org/project/vex-lang](https://pypi.org/project/vex-lang)
- VSCode Marketplace: [Vex Language](https://marketplace.visualstudio.com/items?itemName=sohailcodes-ai.vex-lang)
- GitHub: [github.com/sohailcodes-ai/Vex-Lang](https://github.com/sohailcodes-ai/Vex-Lang)

## Built by

Sohail Ali — [@sohailcodes-ai](https://github.com/sohailcodes-ai)