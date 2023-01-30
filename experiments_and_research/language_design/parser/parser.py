from experiments_and_research.language_design.lexer import Lexer, TokenType
from experiments_and_research.language_design.ast import Identifier
from .program import Program


class Parser:
    def __init__(self, lexer: Lexer):
        self.lexer = lexer
        self.peek_token = None
        self.current_token = None
        self.register_prefix = {
            TokenType.IDENT: self.parse_identifier,
            TokenType.INT: self.parse_integer_literal,
            TokenType.TRUE: self.parse_boolean,
            TokenType.FALSE: self.parse_boolean,
            TokenType.BANG: self.parse_prefix_expression,
            TokenType.MINUS: self.parse_prefix_expression,
            TokenType.LPAREN: self.parse_grouped_expression,
        }
        # Init current token and peek token
        self.next_token()
        self.next_token()

    def next_token(self):
        self.current_token = self.peek_token
        self.peek_token = self.lexer.next_token()

    def parse_program(self):
        program = Program()
        while self.current_token.token_type != TokenType.EOF:
            program.statements.append(self.parse_expressions())
        return program

    def parse_integer_literal(self):
        pass

    def parse_grouped_expression(self):
        pass

    def parse_boolean(self):
        pass

    def parse_identifier(self):
        token = self.current_token
        self.next_token()
        return Identifier(token.literal)

    def parse_prefix_expression(self):
        return

    # Start parsing an expression
    def parse_expressions(self):
        pass
