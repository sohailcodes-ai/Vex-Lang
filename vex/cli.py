"""
cli.py
------
Vex CLI — registers the 'vex' command globally after pip install.
Usage:
    vex run <file.vex>
    vex version
"""

import sys
from vex.transpiler import transpile
from vex.runner import run


def main():
    if len(sys.argv) < 2:
        print("Vex Language v0.1.0")
        print("Usage:")
        print("  vex run <file.vex>")
        print("  vex version")
        return

    command = sys.argv[1]

    if command == "version":
        print("Vex v0.1.0")
        return

    if command == "run":
        if len(sys.argv) < 3:
            print("[Vex] Error: file path do")
            print("Usage: vex run <file.vex>")
            return

        filepath = sys.argv[2]

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                source = f.read()
        except FileNotFoundError:
            print(f"[Vex Error] File nahi mila: {filepath}")
            return

        python_code = transpile(source)
        run(python_code)

    else:
        print(f"[Vex] Unknown command: {command}")
        print("Usage: vex run <file.vex>")


if __name__ == "__main__":
    main()