"""
Notes:
Lexical analysis is the process of converting a sequence of characters into a sequence of tokens.
Tokens are an accessibly small unit of meaning.
"""
import string
from .token_cls import Token, TokenType


class Lexer:
    def __init__(self, text: string):
        self.input = text
        self.read_offset = 0
        self.offset = 0
        self.char = None
        self.read_char()

    def next_token(self):
        token = self.get_token()
        return token

    def get_token(self):
        self.skip_whitespace()
        if self.char is None:
            return self.build_token(TokenType.EOF, None)
        if self.char.isalpha():
            return self.read_identifier()
        if self.char.isdigit():
            return self.read_number()
        if self.char == "=":
            if self.peek_char() == "=":
                self.read_char()
                return self.build_token(TokenType.EQUAL, "==")
            return self.build_token(TokenType.ASSIGN, self.char)
        if self.char == "+":
            return self.build_token(TokenType.PLUS, self.char)
        if self.char == "-":
            return self.build_token(TokenType.MINUS, self.char)
        if self.char == "!":
            if self.peek_char() == "=":
                self.read_char()
                return self.build_token(TokenType.NOT_EQUAL, "!=")
            return self.build_token(TokenType.BANG, self.char)
        if self.char == "*":
            return self.build_token(TokenType.ASTERISK, self.char)
        if self.char == "/":
            return self.build_token(TokenType.SLASH, self.char)
        if self.char == "<":
            return self.build_token(TokenType.LESS_THAN, self.char)
        if self.char == ">":
            return self.build_token(TokenType.GREATER_THAN, self.char)
        if self.char == ",":
            return self.build_token(TokenType.COMMA, self.char)
        if self.char == ";":
            return self.build_token(TokenType.SEMICOLON, self.char)
        if self.char == "(":
            return self.build_token(TokenType.LPAREN, self.char)
        if self.char == ")":
            return self.build_token(TokenType.RPAREN, self.char)
        if self.char == "{":
            return self.build_token(TokenType.LBRACE, self.char)
        if self.char == "}":
            return self.build_token(TokenType.RBRACE, self.char)
        return self.build_token(TokenType.ILLEGAL, self.char)

    def read_char(self):
        if self.read_offset >= len(self.input):
            self.char = None
        else:
            self.char = self.input[self.read_offset]
        self.offset = self.read_offset
        self.read_offset += 1

    def peek_char(self):
        if self.read_offset >= len(self.input):
            return None
        else:
            return self.input[self.read_offset]

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

    def build_token(self, token_type: TokenType, literal: string):
        self.read_char()
        return Token(token_type, literal)
