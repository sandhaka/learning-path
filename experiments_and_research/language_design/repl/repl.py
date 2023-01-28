from experiments_and_research.language_design.lexer import Lexer


class Repl:
    def __init__(self):
        self.exits = ["exit", "quit", "q"]

    def start(self):
        while True:
            user_input = input(">> ")
            if user_input in self.exits:
                break

            lexer = Lexer(user_input)

            # TODO: Evaluate expressions. For now, just print tokens
            for token in lexer.token_generator():
                print(token)
