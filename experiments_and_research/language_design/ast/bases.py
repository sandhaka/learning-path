from enum import Enum


class StatementKind(Enum):
    Let = "let"
    Return = "return"
    Expression = "expression"
    Block = "block"


class ExpressionKind(Enum):
    Identifier = "identifier"
    IntegerLiteral = "integerLiteral"
    Prefix = "prefix"
    Infix = "infix"
    Boolean = "boolean"
    # If = "if"
    # FunctionalLiteral = "functionalLiteral"
    # Call = "call"


class Node:
    def __init__(self, kind, literal):
        self.kind = kind
        self.literal = literal

    def __str__(self):
        return f"Node({self.kind}, {self.literal})"
