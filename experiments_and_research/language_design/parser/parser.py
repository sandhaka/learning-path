from experiments_and_research.language_design.lexer import Lexer, TokenType
from experiments_and_research.language_design.ast import (
    Identifier,
    PrefixExpression,
    InfixExpression,
    IntegerLiteral,
    Boolean,
    ExpressionKind,
)

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
        self.register_infix = {
            TokenType.PLUS: self.parse_infix_expression,
            TokenType.MINUS: self.parse_infix_expression,
            TokenType.SLASH: self.parse_infix_expression,
            TokenType.ASTERISK: self.parse_infix_expression,
            TokenType.EQUAL: self.parse_infix_expression,
            TokenType.NOT_EQUAL: self.parse_infix_expression,
            TokenType.LESS_THAN: self.parse_infix_expression,
            TokenType.GREATER_THAN: self.parse_infix_expression,
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
        expression = PrefixExpression(self.current_token, self.current_token.literal)
        self.next_token()
        expression.right = self.parse_expressions()
        return expression

    def parse_infix_expression(self):
        expression = InfixExpression(self.current_token, self.current_token.literal)
        self.next_token()
        expression.left = self.parse_expressions()
        return expression

    # Start parsing an expression
    def parse_expressions(self):
        if self.is_register_prefix(self.current_token.token_type):
            raise FileNotFoundError("No prefix parse function for {} found".format(self.current_token.token_type))
        statement = self.register_prefix[self.current_token.token_type]()
        if statement.kind != ExpressionKind.Prefix:
            raise ValueError("Expected prefix expression")
        while self.peek_token.token_type != TokenType.SEMICOLON:
            if self.is_register_infix(self.peek_token.token_type):
                return statement
            statement = self.register_infix[self.peek_token.token_type]()
            if statement.kind != ExpressionKind.Infix:
                return statement
            self.next_token()
        return statement

    def parse_let_statement(self):
        raise NotImplementedError

    def is_register_prefix(self, token_type: TokenType):
        return token_type in self.register_prefix.keys()

    def is_register_infix(self, token_type: TokenType):
        return token_type in self.register_infix.keys()
