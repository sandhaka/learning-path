from experiments_and_research.language_design.parser import Parser
from experiments_and_research.language_design.lexer import Lexer


def test_parser():
    input_text = "x = (9 - 3 * 3)"
    lexer = Lexer(input_text)
    parser = Parser(lexer)
    statement = parser.parse_expression()
    print(statement)
