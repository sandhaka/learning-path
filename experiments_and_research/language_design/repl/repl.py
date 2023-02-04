from experiments_and_research.language_design.evaluator import Evaluator


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
        evaluator = Evaluator()
        while True:
            user_input = input(">> ")
            if user_input in self.exits:
                break
            prompt = evaluator.evaluate(user_input)
            print(prompt)
