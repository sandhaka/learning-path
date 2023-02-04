from experiments_and_research.language_design.lexer import Lexer
from experiments_and_research.language_design.parser import Parser


class Repl:
    def __init__(self):
        self.exits = ["exit", "quit", "q"]

    @staticmethod
    def welcome():
        print("Welcome into an experimental interpreter!")
        print("Type 'quit|exit|q' to quit the interpreter.")
        print()

    def start(self):
        self.welcome()
        while True:
            user_input = input(">> ")
            if user_input in self.exits:
                break

            parser = Parser(Lexer(user_input))
            ast = parser.parse_expression()

            # TODO: Evaluate expressions.
