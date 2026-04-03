"""
runner.py
---------
Executes transpiled Python code and shows readable errors.
"""


def run(python_code: str):
    try:
        exec(compile(python_code, "<vex>", "exec"), {})
    except SyntaxError as e:
        print(f"\n[Vex Error] Syntax galat hai — line {e.lineno}: {e.msg}")
    except Exception as e:
        print(f"\n[Vex Error] {type(e).__name__}: {e}")