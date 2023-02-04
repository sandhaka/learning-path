import string
from enum import Enum


class Precedence(Enum):
    LOWEST = 0
    EQUALS = 1
    LESSGREATER = 2
    SUM = 3
    PRODUCT = 4
    PREFIX = 5
    CALL = 6


class TokenType(Enum):
    ILLEGAL = ("ILLEGAL",)
    EOF = ("EOF",)
    IDENT = ("IDENT",)
    NUMB = ("NUMB",)
    ASSIGN = ("=",)
    PLUS = ("+",)
    MINUS = ("-",)
    BANG = ("!",)
    ASTERISK = ("*",)
    SLASH = ("/",)
    MOD = ("%",)
    LESS_THAN = ("<",)
    GREATER_THAN = (">",)
    COMMA = (",",)
    SEMICOLON = (";",)
    LPAREN = ("(",)
    RPAREN = (")",)
    LBRACE = ("{",)
    RBRACE = ("}",)
    LBRACKET = ("[",)
    RBRACKET = ("]",)
    FUNCTION = ("FUNCTION",)
    LET = ("LET",)
    TRUE = ("TRUE",)
    FALSE = ("FALSE",)
    IF = ("IF",)
    ELSE = ("ELSE",)
    RETURN = ("RETURN",)
    EQUAL = ("==",)
    NOT_EQUAL = "!="


class Token:
    def __init__(self, token_type: TokenType, literal: string):
        self.token_type = token_type
        self.literal = literal

    def __str__(self):
        return f"Token({self.token_type}, {self.literal})"
