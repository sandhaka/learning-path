import string
from enum import Enum


class TokenType(Enum):
    ILLEGAL = "ILLEGAL"
    EOF = "EOF"
    # Identifiers + literals
    IDENT = "IDENT"  # add, foobar, x, y, ...
    INT = "INT"  # 1343456
    # Operators
    ASSIGN = "="
    PLUS = "+"
    COMMA = ","
    SEMICOLON = ";"
    LPAREN = "("
    RPAREN = ")"
    LBRACE = "{"
    RBRACE = "}"
    # Keywords
    FUNCTION = "FUNCTION"
    LET = "LET"


class Token:
    def __init__(self, token_type: TokenType, literal: string):
        self.token_type = token_type
        self.literal = literal

    def __str__(self):
        return f"Token({self.token_type}, {self.literal})"
