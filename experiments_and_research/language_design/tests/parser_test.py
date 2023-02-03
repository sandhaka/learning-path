from experiments_and_research.language_design.parser import Parser
from experiments_and_research.language_design.lexer import Lexer


def test_parser():
    input_tests = [
        "7 - 1 + 4 * 2",
        "x = 5",
        "y = 10 + 4",
        "838383",
        "y = 5",
        "5 + 5",
        "5 + 5 + 5",
        "x = (9 - 3 * 3)",
        "7 * 9 + 7",
        "r = 5.78",
    ]

    for input_text in input_tests:
        lexer = Lexer(input_text)
        parser = Parser(lexer)
        statement = parser.parse_expression()
        print(statement)
