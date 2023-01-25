"""
Notes:
Lexical analysis is the process of converting a sequence of characters into a sequence of tokens.
Tokens are an accessibly small unit of meaning.
"""
import string
from .token import Token, TokenType


class Lexer:
    def __init__(self, text: string):
        self.input = text
        self.read_offset = 0
        self.offset = 0
        self.char = None
        self.read_char()

    def next_token(self):
        token = self.get_token()
        self.read_char()
        return token

    def get_token(self):
        self.skip_whitespace()
        if self.char is None:
            return Token(TokenType.EOF, None)
        if self.char.isalpha():
            return self.read_identifier()
        if self.char.isdigit():
            return self.read_number()
        if self.char == "=":
            return Token(TokenType.ASSIGN, self.char)
        if self.char == "+":
            return Token(TokenType.PLUS, self.char)
        if self.char == ",":
            return Token(TokenType.COMMA, self.char)
        if self.char == ";":
            return Token(TokenType.SEMICOLON, self.char)
        if self.char == "(":
            return Token(TokenType.LPAREN, self.char)
        if self.char == ")":
            return Token(TokenType.RPAREN, self.char)
        if self.char == "{":
            return Token(TokenType.LBRACE, self.char)
        if self.char == "}":
            return Token(TokenType.RBRACE, self.char)
        return Token(TokenType.ILLEGAL, self.char)

    def read_char(self):
        if self.read_offset >= len(self.input):
            self.char = None
        self.char = self.input[self.read_offset]
        self.offset = self.read_offset
        self.read_offset += 1

    def read_number(self):
        initial_offset = self.offset
        while self.char is not None and self.char.isdigit():
            self.read_char()
        return Token(TokenType.INT, self.input[initial_offset : self.offset])

    def skip_whitespace(self):
        while self.char is not None and self.char.isspace():
            self.read_char()

    def read_identifier(self):
        initial_offset = self.offset
        while self.char is not None and self.char.isalnum():
            self.read_char()
        return Token(TokenType.IDENT, self.input[initial_offset : self.offset])
