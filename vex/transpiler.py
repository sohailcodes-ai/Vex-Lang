"""Backward-compatible re-export. Prefer vex.translator."""

from vex.translator import fix_strings, transpile

__all__ = ["fix_strings", "transpile"]
