"""
runner.py
---------
Vex Runner — takes transpiled Python code and executes it.
Also handles readable error messages when something goes wrong.
"""


class Runner:
    """
    Executes transpiled Python code.
    Catches errors and shows them in a readable Vex-style format.
    """

    def __init__(self, python_code: str):
        self.python_code = python_code

    def run(self):
        """
        Executes the Python code.
        To be implemented.
        """
        pass