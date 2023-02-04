"""
Grammar for the interpreter language in EBNF syntax
https://en.wikipedia.org/wiki/Extended_Backus–Naur_form

expression      ::= factor | expression operator expression
factor          ::= number | identifier | assignment | '(' expression ')'
assignment      ::= identifier '=' expression

operator        ::= '+' | '-' | '*' | '/' | '%'

identifier      ::= letter | '_' { identifier-char }
identifier-char ::= '_' | letter | digit

number          ::= { digit } [ '.' digit { digit } ]

letter          ::= 'a' | 'b' | ... | 'y' | 'z' | 'A' | 'B' | ... | 'Y' | 'Z'
digit           ::= '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
"""
from experiments_and_research.language_design.lexer import Lexer, TokenType, Precedence
from experiments_and_research.language_design.ast import (
    Identifier,
    NumberLiteral,
    PrefixExpression,
    InfixExpression,
    Boolean,
    GroupedExpression,
)


class Parser:
    def __init__(self, lexer: Lexer):
        self.lexer = lexer
        self.peek_token = None
        self.current_token = None
        self.prefix_parse_fns = {
            TokenType.IDENT: self.parse_identifier,
            TokenType.NUMB: self.parse_integer_literal,
            TokenType.BANG: self.parse_prefix_expression,
            TokenType.MINUS: self.parse_prefix_expression,
            TokenType.TRUE: self.parse_boolean,  # Not available yet
            TokenType.FALSE: self.parse_boolean,  # Not available yet
            TokenType.LPAREN: self.parse_grouped_expression,
        }
        self.infix_parse_fns = {
            TokenType.PLUS: self.parse_infix_expression,
            TokenType.MINUS: self.parse_infix_expression,
            TokenType.SLASH: self.parse_infix_expression,
            TokenType.ASTERISK: self.parse_infix_expression,
            TokenType.EQUAL: self.parse_infix_expression,
            TokenType.NOT_EQUAL: self.parse_infix_expression,
            TokenType.LESS_THAN: self.parse_infix_expression,
            TokenType.GREATER_THAN: self.parse_infix_expression,
            TokenType.ASSIGN: self.parse_infix_expression,
        }
        self.precedences_map = {
            TokenType.ASSIGN: Precedence.EQUALS,
            TokenType.EQUAL: Precedence.EQUALS,
            TokenType.NOT_EQUAL: Precedence.EQUALS,
            TokenType.LESS_THAN: Precedence.LESSGREATER,
            TokenType.GREATER_THAN: Precedence.LESSGREATER,
            TokenType.PLUS: Precedence.SUM,
            TokenType.MINUS: Precedence.SUM,
            TokenType.SLASH: Precedence.PRODUCT,
            TokenType.ASTERISK: Precedence.PRODUCT,
            TokenType.LPAREN: Precedence.CALL,
        }

        # Init current token and peek token
        self.next_token()
        self.next_token()

    def parse_identifier(self):
        return Identifier(self.current_token.literal)

    def parse_integer_literal(self):
        return NumberLiteral(self.current_token.literal)

    def parse_prefix_expression(self):
        operator = self.current_token.literal
        self.next_token()
        right = self.parse_expression()
        return PrefixExpression(operator, right)

    def parse_infix_expression(self, left):
        infix_exp = InfixExpression(left, self.current_token.literal, None)
        precedence = self.current_precedence()
        self.next_token()
        infix_exp.right = self.parse_expression(precedence)
        return infix_exp

    def parse_boolean(self):
        return Boolean(self.current_token.literal)

    def parse_grouped_expression(self):
        self.next_token()
        exp = self.parse_expression()
        if self.peek_token.token_type != TokenType.RPAREN:
            raise Exception("expected )")
        self.next_token()
        return GroupedExpression(exp)

    def next_token(self):
        self.current_token = self.peek_token
        self.peek_token = self.lexer.next_token()

    def parse_program(self):
        raise NotImplementedError

    def parse_expression(self, precedence=Precedence.LOWEST):
        if self.current_token.token_type not in self.prefix_parse_fns:
            raise Exception(f"no prefix parse function for {self.current_token.token_type}")
        left_exp = self.prefix_parse_fns[self.current_token.token_type]()
        while self.peek_token.token_type != TokenType.EOF and precedence.value < self.peek_precedence().value:
            if self.peek_token.token_type not in self.infix_parse_fns:
                return left_exp
            self.next_token()
            left_exp = self.infix_parse_fns[self.current_token.token_type](left_exp)
        return left_exp

    def current_precedence(self):
        if self.current_token.token_type in self.precedences_map:
            return self.precedences_map[self.current_token.token_type]
        return Precedence.LOWEST

    def peek_precedence(self):
        if self.peek_token.token_type in self.precedences_map:
            return self.precedences_map[self.peek_token.token_type]
        return Precedence.LOWEST
