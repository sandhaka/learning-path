from experiments_and_research.language_design.lexer import Lexer, Token, TokenType

simple_expr_inputs = [
    "x = 7",
    "x + 6",
    "y + 7",
    "var = 1024",
    "let x = 7",
    "let y = 7",
    "let foobar = 7",
    # Use semicolon to separate as rows
    "let x = 7; let y = 8",
    "let x = 7; let y = 8; let foobar = 9",
    # Multi lines
    """let f = 89;
    let g =7""",
]


def test_lexer_with_simple_expressions():
    for input_test in simple_expr_inputs:
        print(f"{input_test}:")
        lexer = Lexer(input_test)
        tokens = []
        token = lexer.next_token()
        tokens.append(token)
        while token.token_type != TokenType.EOF:
            token = lexer.next_token()
            tokens.append(token)
        for t in tokens:
            print(t)
        print("---")
