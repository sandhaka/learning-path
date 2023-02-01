from experiments_and_research.language_design.parser import Parser
from experiments_and_research.language_design.lexer import Lexer


def test_parser():
    input_text = "x = 5;"
    lexer = Lexer(input_text)
    parser = Parser(lexer)
    program = parser.parse_program()
    assert program.statements[0].token_literal() == "x"
