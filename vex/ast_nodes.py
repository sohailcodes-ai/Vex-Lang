from dataclasses import dataclass, field
from typing import List, Optional


class ASTNode:
    """Base class for all AST nodes."""

    def pretty(self, indent: int = 0) -> str:
        raise NotImplementedError("pretty() must be implemented by subclasses")


@dataclass
class Program(ASTNode):
    body: List[ASTNode] = field(default_factory=list)

    def pretty(self, indent: int = 0) -> str:
        spaces = " " * indent
        lines = [f"{spaces}Program"]
        for node in self.body:
            lines.append(node.pretty(indent + 2))
        return "\n".join(lines)


@dataclass
class Identifier(ASTNode):
    name: str

    def pretty(self, indent: int = 0) -> str:
        spaces = " " * indent
        return f"{spaces}Identifier({self.name})"


@dataclass
class NumberLiteral(ASTNode):
    value: str

    def pretty(self, indent: int = 0) -> str:
        spaces = " " * indent
        return f"{spaces}NumberLiteral({self.value})"


@dataclass
class StringLiteral(ASTNode):
    value: str

    def pretty(self, indent: int = 0) -> str:
        spaces = " " * indent
        return f"{spaces}StringLiteral({self.value!r})"


@dataclass
class BooleanLiteral(ASTNode):
    value: bool

    def pretty(self, indent: int = 0) -> str:
        spaces = " " * indent
        return f"{spaces}BooleanLiteral({self.value})"


@dataclass
class NullLiteral(ASTNode):
    def pretty(self, indent: int = 0) -> str:
        spaces = " " * indent
        return f"{spaces}NullLiteral(None)"


@dataclass
class BinaryExpression(ASTNode):
    left: ASTNode
    operator: str
    right: ASTNode

    def pretty(self, indent: int = 0) -> str:
        spaces = " " * indent
        return "\n".join(
            [
                f"{spaces}BinaryExpression({self.operator})",
                self.left.pretty(indent + 2),
                self.right.pretty(indent + 2),
            ]
        )


@dataclass
class PrintStatement(ASTNode):
    value: ASTNode

    def pretty(self, indent: int = 0) -> str:
        spaces = " " * indent
        return "\n".join(
            [
                f"{spaces}PrintStatement",
                self.value.pretty(indent + 2),
            ]
        )


@dataclass
class AssignmentStatement(ASTNode):
    target: Identifier
    value: ASTNode

    def pretty(self, indent: int = 0) -> str:
        spaces = " " * indent
        return "\n".join(
            [
                f"{spaces}AssignmentStatement",
                self.target.pretty(indent + 2),
                self.value.pretty(indent + 2),
            ]
        )


@dataclass
class IfStatement(ASTNode):
    condition: ASTNode
    body: List[ASTNode] = field(default_factory=list)
    else_body: Optional[List[ASTNode]] = None

    def pretty(self, indent: int = 0) -> str:
        spaces = " " * indent
        lines = [f"{spaces}IfStatement", self.condition.pretty(indent + 2)]

        lines.append(f"{spaces}  Body")
        for node in self.body:
            lines.append(node.pretty(indent + 4))

        if self.else_body:
            lines.append(f"{spaces}  ElseBody")
            for node in self.else_body:
                lines.append(node.pretty(indent + 4))

        return "\n".join(lines)