"""
transpiler.py
-------------
Vex Transpiler — converts Vex source code into valid Python code.
This is the core of Vex. Hinglish/English keywords get swapped to Python.
Extra Vex features (pipe operator, auto f-strings, etc.) get transformed here.

Example:
    bolo "Hello {naam}"
    → print(f"Hello {naam}")
"""

from vex.keywords import HINGLISH_TO_PYTHON, ENGLISH_KEYWORDS


class Transpiler:
    """
    Takes Vex source code string, returns Python source code string.
    """

    def __init__(self, source: str, mode: str = "english"):
        self.source = source
        self.mode = mode  # "hinglish" or "english"

    def transpile(self) -> str:
        """
        Main method — converts Vex code to Python code.
        To be implemented.
        """
        pass