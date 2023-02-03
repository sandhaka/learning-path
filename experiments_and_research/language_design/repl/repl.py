from experiments_and_research.language_design.lexer import Lexer
from experiments_and_research.language_design.parser import Parser


class Repl:
    def __init__(self):
        self.exits = ["exit", "quit", "q"]

    def welcome(self):
        print("Welcome into an experimental interpreter!")
        print(
            """
             ______________
       ,===:'.,            `-._
            `:.`---.__         `-._
              `:.     `--.         `.
                \.        `.         `.
        (,,(,    \.         `.   ____,-`.,
     (,'     `/   \.   ,--.___`.'
 ,  ,'  ,--.  `,   \.;'         `
  `{D, {    \  :    \;
    V,,'    /  /    //
    j;;    /  ,' ,-//.    ,---.      ,
    \;'   /  ,' /  _  \  /  _  \   ,'/
          \   `'  / \  `'  / \  `.' /
           `.___,'   `.__,'   `.__,'
            """
        )

    def start(self):
        self.welcome()
        while True:
            user_input = input(">> ")
            if user_input in self.exits:
                break

            lexer = Lexer(user_input)
            parser = Parser(lexer)
            ast = parser.parse_expression()

            # TODO: Evaluate expressions. For now, just print tokens
            for token in lexer.token_generator():
                print(token)
