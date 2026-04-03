"""
main.py
-------
Vex CLI entry point.
Usage: python main.py run <file.vex>
"""

import sys
from vex.transpiler import transpile
from vex.runner import run

#mode Hinglish

def main():
    if len(sys.argv) < 3:
        print("Vex Language v0.1.0")
        print("Usage: python main.py run <file.vex>")
        return

    command = sys.argv[1]
    filepath = sys.argv[2]

    if command == "run":
        with open(filepath, "r", encoding="utf-8") as f:
            source = f.read()

        python_code = transpile(source)
        run(python_code)
    else:
        print(f"[Vex] Unknown command: {command}")


if __name__ == "__main__":
    main()