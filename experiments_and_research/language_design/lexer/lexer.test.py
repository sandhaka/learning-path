from lexer import Lexer
from .token import Token, TokenType

simple_expr_inputs = ["x = 7", "x + 6", "y + 7"]

var_declarations_inputs = [
    "let x = 7",
    "let y = 7",
    "let foobar = 7",
    "let x = 7; let y = 8",
    "let x = 7; let y = 8; let foobar = 9",
]


def test_lexer_with_simple_expressions():
    for input_test in simple_expr_inputs:
        lexer = Lexer(input_test)
        token = None
        while token.token_type != TokenType.EOF:
            token = lexer.next_token()
            print(token)
        print(token)
        print("")


def test_lexer_with_var_declaration_expressions():
    for input_test in var_declarations_inputs:
        lexer = Lexer(input_test)
        token = None
        while token.token_type != TokenType.EOF:
            token = lexer.next_token()
            print(token)
        print(token)
        print("")
