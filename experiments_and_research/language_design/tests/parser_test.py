from experiments_and_research.language_design.parser import Parser
from experiments_and_research.language_design.lexer import Lexer
from experiments_and_research.language_design.ast import ExpressionKind


def test_parse_decimals():
    lexer = Lexer("r = 5.78")
    parser = Parser(lexer)
    statement = parser.parse_expression()
    assert statement.kind == ExpressionKind.Infix
    assert statement.left.kind == ExpressionKind.Identifier
    assert statement.left.literal == "r"
    assert statement.literal == "="
    assert statement.right.kind == ExpressionKind.NumberLiteral
    assert statement.right.literal == "5.78"


def test_parse_constants():
    lexer = Lexer("838383")
    parser = Parser(lexer)
    statement = parser.parse_expression()
    assert statement.kind == ExpressionKind.NumberLiteral
    assert statement.literal == "838383"


def test_precedences():
    lexer = Lexer("5 + 5 + 5")
    parser = Parser(lexer)
    statement = parser.parse_expression()
    assert statement.kind == ExpressionKind.Infix
    assert statement.left.kind == ExpressionKind.Infix
    assert statement.left.left.kind == ExpressionKind.NumberLiteral
    assert statement.left.left.literal == "5"
    assert statement.left.literal == "+"
    assert statement.left.right.kind == ExpressionKind.NumberLiteral
    assert statement.left.right.literal == "5"
    assert statement.literal == "+"
    assert statement.right.kind == ExpressionKind.NumberLiteral
    assert statement.right.literal == "5"


def test_precedence_product():
    lexer = Lexer("5 * 5 + 5")
    parser = Parser(lexer)
    statement = parser.parse_expression()
    assert statement.kind == ExpressionKind.Infix
    assert statement.left.kind == ExpressionKind.Infix
    assert statement.left.left.kind == ExpressionKind.NumberLiteral
    assert statement.left.left.literal == "5"
    assert statement.left.literal == "*"
    assert statement.left.right.kind == ExpressionKind.NumberLiteral
    assert statement.left.right.literal == "5"
    assert statement.literal == "+"
    assert statement.right.kind == ExpressionKind.NumberLiteral
    assert statement.right.literal == "5"


def test_precedence_more_complex():
    lexer = Lexer("5 * 5 + 5 * 5")
    parser = Parser(lexer)
    statement = parser.parse_expression()
    assert statement.kind == ExpressionKind.Infix
    assert statement.left.kind == ExpressionKind.Infix
    assert statement.left.left.kind == ExpressionKind.NumberLiteral
    assert statement.left.left.literal == "5"
    assert statement.left.literal == "*"
    assert statement.left.right.kind == ExpressionKind.NumberLiteral
    assert statement.left.right.literal == "5"
    assert statement.literal == "+"
    assert statement.right.kind == ExpressionKind.Infix
    assert statement.right.left.kind == ExpressionKind.NumberLiteral
    assert statement.right.left.literal == "5"
    assert statement.right.literal == "*"
    assert statement.right.right.kind == ExpressionKind.NumberLiteral
    assert statement.right.right.literal == "5"


def test_precedence_parentheses():
    lexer = Lexer("5 * (5 + 5) * 5")
    parser = Parser(lexer)
    statement = parser.parse_expression()
    assert statement.kind == ExpressionKind.Infix
    assert statement.left.kind == ExpressionKind.Infix
    assert statement.left.left.kind == ExpressionKind.NumberLiteral
    assert statement.left.left.literal == "5"
    assert statement.left.literal == "*"
    assert statement.left.right.kind == ExpressionKind.GroupedExpression
    assert statement.left.right.literal.kind == ExpressionKind.Infix
    assert statement.left.right.literal.left.kind == ExpressionKind.NumberLiteral
    assert statement.left.right.literal.left.literal == "5"
    assert statement.left.right.literal.literal == "+"
    assert statement.left.right.literal.right.kind == ExpressionKind.NumberLiteral
    assert statement.left.right.literal.right.literal == "5"
    assert statement.literal == "*"
    assert statement.right.kind == ExpressionKind.NumberLiteral
    assert statement.right.literal == "5"


def test_precedence_parentheses_2():
    lexer = Lexer("(5 + 5) * 5")
    parser = Parser(lexer)
    statement = parser.parse_expression()
    assert statement.kind == ExpressionKind.Infix
    assert statement.left.kind == ExpressionKind.GroupedExpression
    assert statement.left.literal.kind == ExpressionKind.Infix
    assert statement.left.literal.left.kind == ExpressionKind.NumberLiteral
    assert statement.left.literal.left.literal == "5"
    assert statement.left.literal.literal == "+"
    assert statement.left.literal.right.kind == ExpressionKind.NumberLiteral
    assert statement.left.literal.right.literal == "5"
    assert statement.literal == "*"
    assert statement.right.kind == ExpressionKind.NumberLiteral
    assert statement.right.literal == "5"


def test_precedence_parentheses_long_expression():
    lexer = Lexer("5 * (5 + 5 * 5) * 5")
    parser = Parser(lexer)
    statement = parser.parse_expression()
    assert statement.kind == ExpressionKind.Infix
    assert statement.left.kind == ExpressionKind.Infix
    assert statement.left.left.kind == ExpressionKind.NumberLiteral
    assert statement.left.left.literal == "5"
    assert statement.left.literal == "*"
    assert statement.left.right.kind == ExpressionKind.GroupedExpression
    assert statement.left.right.literal.kind == ExpressionKind.Infix
    assert statement.left.right.literal.left.kind == ExpressionKind.NumberLiteral
    assert statement.left.right.literal.left.literal == "5"
    assert statement.left.right.literal.literal == "+"
    assert statement.left.right.literal.right.kind == ExpressionKind.Infix
    assert statement.left.right.literal.right.left.kind == ExpressionKind.NumberLiteral
    assert statement.left.right.literal.right.left.literal == "5"
    assert statement.left.right.literal.right.literal == "*"
    assert statement.left.right.literal.right.right.kind == ExpressionKind.NumberLiteral
    assert statement.left.right.literal.right.right.literal == "5"
    assert statement.literal == "*"
    assert statement.right.kind == ExpressionKind.NumberLiteral
    assert statement.right.literal == "5"


def test_assignment():
    lexer = Lexer("a = 5")
    parser = Parser(lexer)
    statement = parser.parse_expression()
    assert statement.kind == ExpressionKind.Infix
    assert statement.left.kind == ExpressionKind.Identifier
    assert statement.left.literal == "a"
    assert statement.right.kind == ExpressionKind.NumberLiteral
    assert statement.right.literal == "5"


def test_boolean_expression():
    lexer = Lexer("true")
    parser = Parser(lexer)
    statement = parser.parse_expression()
    assert statement.kind == ExpressionKind.Identifier  # BooleanExpression not supported yet, treat as identifier
    assert statement.literal == "true"


def test_decimal_expression():
    lexer = Lexer("1.5")
    parser = Parser(lexer)
    statement = parser.parse_expression()
    assert statement.kind == ExpressionKind.NumberLiteral
    assert statement.literal == "1.5"
