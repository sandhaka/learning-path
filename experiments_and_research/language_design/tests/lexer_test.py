from experiments_and_research.language_design.lexer import Lexer, Token, TokenType


def init_lexer(statement):
    lexer = Lexer(statement)
    tokens = []
    token = lexer.next_token()
    tokens.append(token)
    while token.token_type != TokenType.EOF:
        token = lexer.next_token()
        tokens.append(token)
    return tokens


def test_base_statement():
    statement = "x = 7"
    tokens = init_lexer(statement)
    assert len(tokens) == 4
    assert tokens[0].token_type == TokenType.IDENT
    assert tokens[1].token_type == TokenType.ASSIGN
    assert tokens[2].token_type == TokenType.INT
    assert tokens[3].token_type == TokenType.EOF


def test_base_statement2():
    statement = "x + 6"
    tokens = init_lexer(statement)
    assert len(tokens) == 4
    assert tokens[0].token_type == TokenType.IDENT
    assert tokens[1].token_type == TokenType.PLUS
    assert tokens[2].token_type == TokenType.INT
    assert tokens[3].token_type == TokenType.EOF


def test_statement():
    statement = "(4 - 6) * 7"
    tokens = init_lexer(statement)
    assert len(tokens) == 8
    assert tokens[0].token_type == TokenType.LPAREN
    assert tokens[1].token_type == TokenType.INT
    assert tokens[2].token_type == TokenType.MINUS
    assert tokens[3].token_type == TokenType.INT
    assert tokens[4].token_type == TokenType.RPAREN
    assert tokens[5].token_type == TokenType.ASTERISK
    assert tokens[6].token_type == TokenType.INT
    assert tokens[7].token_type == TokenType.EOF


def test_statement2():
    statement = "10 == 10"
    lexer = Lexer(statement)
    tokens = []
    token = lexer.next_token()
    tokens.append(token)
    while token.token_type != TokenType.EOF:
        token = lexer.next_token()
        tokens.append(token)
    assert len(tokens) == 4
    assert tokens[0].token_type == TokenType.INT
    assert tokens[1].token_type == TokenType.EQUAL
    assert tokens[2].token_type == TokenType.INT
    assert tokens[3].token_type == TokenType.EOF
