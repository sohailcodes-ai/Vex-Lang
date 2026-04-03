"""
main.py
-------
Vex CLI entry point.
Usage:
    python main.py run <file.vex>
"""

import sys


def main():
    if len(sys.argv) < 3:
        print("Vex Language v0.1.0")
        print("Usage: vex run <file.vex>")
        return

    command = sys.argv[1]
    filepath = sys.argv[2]

    if command == "run":
        # TODO: wire up lexer → transpiler → runner
        print(f"Running {filepath}...")
    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()