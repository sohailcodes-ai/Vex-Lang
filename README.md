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

## Links

- PyPI: [pypi.org/project/vex-lang](https://pypi.org/project/vex-lang)
- VSCode Marketplace: [Vex Language](https://marketplace.visualstudio.com/items?itemName=sohailcodes-ai.vex-lang)
- GitHub: [github.com/sohailcodes-ai/Vex-Lang](https://github.com/sohailcodes-ai/Vex-Lang)

## Built by

Sohail Ali — [@sohailcodes-ai](https://github.com/sohailcodes-ai)