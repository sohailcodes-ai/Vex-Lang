"""
runtime.py
----------
Executes transpiled Python code and shows readable Vex errors.
"""

from vex.errors import format_runtime_error, format_syntax_error


def run(python_code: str) -> None:
    try:
        exec(compile(python_code, "<vex>", "exec"), {})
    except SyntaxError as error:
        print(format_syntax_error(error))
    except Exception as error:
        print(format_runtime_error(error))
