"""
errors.py
---------
Vex error types and user-facing error formatting.
"""


class VexError(Exception):
    """Base error for Vex CLI and runtime failures."""


class VexFileNotFoundError(VexError):
    """Raised when a requested .vex file does not exist."""


class VexProjectExistsError(VexError):
    """Raised when vex init targets an existing directory."""


class VexConfigError(VexError):
    """Raised when vex.toml is missing or invalid."""


def format_file_not_found(filepath: str) -> str:
    return f"[Vex Error] File nahi mila: {filepath}"


def format_syntax_error(error: SyntaxError) -> str:
    return f"\n[Vex Error] Syntax galat hai — line {error.lineno}: {error.msg}"


def format_runtime_error(error: Exception) -> str:
    return f"\n[Vex Error] {type(error).__name__}: {error}"


def format_unknown_command(command: str) -> str:
    return f"[Vex] Unknown command: {command}"


def format_config_not_found() -> str:
    return "[Vex] Error: vex.toml nahi mila. Usage: vex run <file.vex>"


def format_config_error(message: str) -> str:
    return f"[Vex Error] {message}"
