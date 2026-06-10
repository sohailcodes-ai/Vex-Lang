"""
cli.py
------
Vex CLI — registers the 'vex' command globally after pip install.

Usage:
    vex run <file.vex>
    vex translate <file.vex>
    vex init <project_name>
    vex version
"""

import sys
from pathlib import Path
from typing import Optional

from vex import __version__
from vex.errors import (
    format_file_not_found,
    format_unknown_command,
)
from vex.runtime import run
from vex.translator import transpile

PROJECT_TEMPLATE = """#mode hinglish

bolo "Hello from {project_name}!"
"""


def _print_usage() -> None:
    print(f"Vex Language v{__version__}")
    print("Usage:")
    print("  vex run <file.vex>")
    print("  vex translate <file.vex>")
    print("  vex init <project_name>")
    print("  vex version")


def _read_vex_file(filepath: str) -> Optional[str]:
    try:
        with open(filepath, "r", encoding="utf-8") as source_file:
            return source_file.read()
    except FileNotFoundError:
        print(format_file_not_found(filepath))
        return None


def cmd_run(filepath: str) -> None:
    source = _read_vex_file(filepath)
    if source is None:
        return

    python_code = transpile(source)
    run(python_code)


def cmd_translate(filepath: str) -> None:
    source = _read_vex_file(filepath)
    if source is None:
        return

    print(transpile(source))


def cmd_init(project_name: str) -> None:
    project_dir = Path(project_name)

    if project_dir.exists():
        print(f"[Vex Error] Folder pehle se hai: {project_name}")
        return

    project_dir.mkdir(parents=True)
    main_file = project_dir / "main.vex"
    main_file.write_text(
        PROJECT_TEMPLATE.format(project_name=project_name),
        encoding="utf-8",
    )
    print(f"[Vex] Project ban gaya: {project_name}/")
    print("  - main.vex")
    print(f"\nRun karo: vex run {project_name}/main.vex")


def main() -> None:
    if len(sys.argv) < 2:
        _print_usage()
        return

    command = sys.argv[1]

    if command == "version":
        print(f"Vex v{__version__}")
        return

    if command == "run":
        if len(sys.argv) < 3:
            print("[Vex] Error: file path do")
            print("Usage: vex run <file.vex>")
            return
        cmd_run(sys.argv[2])
        return

    if command == "translate":
        if len(sys.argv) < 3:
            print("[Vex] Error: file path do")
            print("Usage: vex translate <file.vex>")
            return
        cmd_translate(sys.argv[2])
        return

    if command == "init":
        if len(sys.argv) < 3:
            print("[Vex] Error: project name do")
            print("Usage: vex init <project_name>")
            return
        cmd_init(sys.argv[2])
        return

    print(format_unknown_command(command))
    _print_usage()


if __name__ == "__main__":
    main()
