"""
cli.py
------
Vex CLI — registers the 'vex' command globally after pip install.

Usage:
    vex run [file.vex]
    vex translate <file.vex>
    vex tokens <file.vex>
    vex ast <file.vex>
    vex init <project_name>
    vex version
"""

import sys
from pathlib import Path
from typing import Optional

from vex import __version__
from vex.config import (
    CONFIG_FILENAME,
    format_config,
    resolve_entry_file,
)
from vex.errors import (
    VexConfigError,
    format_config_error,
    format_config_not_found,
    format_file_not_found,
    format_unknown_command,
)
from vex.lexer import tokenize
from vex.parser import parse
from vex.runtime import run
from vex.translator import transpile

PROJECT_TEMPLATE = """#mode hinglish

bolo "Hello from {project_name}!"
"""


def _print_usage() -> None:
    print(f"Vex Language v{__version__}")
    print("Usage:")
    print("  vex run [file.vex]")
    print("  vex translate <file.vex>")
    print("  vex tokens <file.vex>")
    print("  vex ast <file.vex>")
    print("  vex init <project_name>")
    print("  vex version")


def _read_vex_file(filepath: str) -> Optional[str]:
    try:
        with open(filepath, "r", encoding="utf-8") as source_file:
            return source_file.read()
    except FileNotFoundError:
        print(format_file_not_found(filepath))
        return None


def _resolve_run_filepath(filepath: Optional[str]) -> Optional[str]:
    if filepath:
        return filepath

    entry_file = resolve_entry_file()
    if entry_file is None:
        print(format_config_not_found())
        return None

    return str(entry_file)


def cmd_run(filepath: Optional[str] = None) -> None:
    resolved = _resolve_run_filepath(filepath)
    if resolved is None:
        return

    source = _read_vex_file(resolved)
    if source is None:
        return

    python_code = transpile(source)
    run(python_code)


def cmd_translate(filepath: str) -> None:
    source = _read_vex_file(filepath)
    if source is None:
        return

    print(transpile(source))


def cmd_tokens(filepath: str) -> None:
    source = _read_vex_file(filepath)
    if source is None:
        return

    tokens = tokenize(source)

    for token in tokens:
        print(f"{token.type.value}({token.value!r}) line={token.line}, col={token.column}")


def cmd_ast(filepath: str) -> None:
    source = _read_vex_file(filepath)
    if source is None:
        return

    tokens = tokenize(source)
    ast_tree = parse(tokens)

    print(ast_tree.pretty())


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
    config_file = project_dir / CONFIG_FILENAME
    config_file.write_text(
        format_config(name=project_name),
        encoding="utf-8",
    )
    print(f"[Vex] Project ban gaya: {project_name}/")
    print("  - main.vex")
    print(f"  - {CONFIG_FILENAME}")
    print(f"\nRun karo:")
    print(f"  cd {project_name}")
    print("  vex run")


def main() -> None:
    if len(sys.argv) < 2:
        _print_usage()
        return

    command = sys.argv[1]

    if command == "version":
        print(f"Vex v{__version__}")
        return

    if command == "run":
        filepath = sys.argv[2] if len(sys.argv) >= 3 else None
        try:
            cmd_run(filepath)
        except VexConfigError as error:
            print(format_config_error(str(error)))
        return

    if command == "translate":
        if len(sys.argv) < 3:
            print("[Vex] Error: file path do")
            print("Usage: vex translate <file.vex>")
            return
        cmd_translate(sys.argv[2])
        return

    if command == "tokens":
        if len(sys.argv) < 3:
            print("[Vex] Error: file path do")
            print("Usage: vex tokens <file.vex>")
            return
        cmd_tokens(sys.argv[2])
        return

    if command == "ast":
        if len(sys.argv) < 3:
            print("[Vex] Error: file path do")
            print("Usage: vex ast <file.vex>")
            return
        cmd_ast(sys.argv[2])
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