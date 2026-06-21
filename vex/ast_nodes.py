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
        return f"{' ' * indent}Identifier({self.name})"


@dataclass
class NumberLiteral(ASTNode):
    value: str

    def pretty(self, indent: int = 0) -> str:
        return f"{' ' * indent}NumberLiteral({self.value})"


@dataclass
class StringLiteral(ASTNode):
    value: str

    def pretty(self, indent: int = 0) -> str:
        return f"{' ' * indent}StringLiteral({self.value!r})"


@dataclass
class BooleanLiteral(ASTNode):
    value: bool

    def pretty(self, indent: int = 0) -> str:
        return f"{' ' * indent}BooleanLiteral({self.value})"


@dataclass
class NullLiteral(ASTNode):
    def pretty(self, indent: int = 0) -> str:
        return f"{' ' * indent}NullLiteral(None)"


@dataclass
class BinaryExpression(ASTNode):
    left: ASTNode
    operator: str
    right: ASTNode

    def pretty(self, indent: int = 0) -> str:
        return "\n".join([
            f"{' ' * indent}BinaryExpression({self.operator})",
            self.left.pretty(indent + 2),
            self.right.pretty(indent + 2),
        ])


@dataclass
class CallExpression(ASTNode):
    callee: Identifier
    arguments: List[ASTNode] = field(default_factory=list)

    def pretty(self, indent: int = 0) -> str:
        spaces = " " * indent
        lines = [f"{spaces}CallExpression", self.callee.pretty(indent + 2)]
        if self.arguments:
            lines.append(f"{spaces}  Arguments")
            for arg in self.arguments:
                lines.append(arg.pretty(indent + 4))
        return "\n".join(lines)


@dataclass
class PrintStatement(ASTNode):
    value: ASTNode

    def pretty(self, indent: int = 0) -> str:
        return "\n".join([
            f"{' ' * indent}PrintStatement",
            self.value.pretty(indent + 2),
        ])


@dataclass
class AssignmentStatement(ASTNode):
    target: Identifier
    value: ASTNode

    def pretty(self, indent: int = 0) -> str:
        return "\n".join([
            f"{' ' * indent}AssignmentStatement",
            self.target.pretty(indent + 2),
            self.value.pretty(indent + 2),
        ])


@dataclass
class ReturnStatement(ASTNode):
    value: Optional[ASTNode] = None

    def pretty(self, indent: int = 0) -> str:
        spaces = " " * indent
        lines = [f"{spaces}ReturnStatement"]
        if self.value is not None:
            lines.append(self.value.pretty(indent + 2))
        return "\n".join(lines)


@dataclass
class FunctionDefinition(ASTNode):
    name: Identifier
    params: List[Identifier] = field(default_factory=list)
    body: List[ASTNode] = field(default_factory=list)

    def pretty(self, indent: int = 0) -> str:
        spaces = " " * indent
        lines = [f"{spaces}FunctionDefinition", self.name.pretty(indent + 2)]

        if self.params:
            lines.append(f"{spaces}  Params")
            for param in self.params:
                lines.append(param.pretty(indent + 4))

        lines.append(f"{spaces}  Body")
        for node in self.body:
            lines.append(node.pretty(indent + 4))

        return "\n".join(lines)


@dataclass
class BreakStatement(ASTNode):
    def pretty(self, indent: int = 0) -> str:
        return f"{' ' * indent}BreakStatement"


@dataclass
class ContinueStatement(ASTNode):
    def pretty(self, indent: int = 0) -> str:
        return f"{' ' * indent}ContinueStatement"
@dataclass
class WhileStatement(ASTNode):
    condition: ASTNode
    body: List[ASTNode] = field(default_factory=list)

    def pretty(self, indent: int = 0) -> str:
        spaces = " " * indent
        lines = [f"{spaces}WhileStatement", self.condition.pretty(indent + 2)]

        lines.append(f"{spaces}  Body")
        for node in self.body:
            lines.append(node.pretty(indent + 4))

        return "\n".join(lines)


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