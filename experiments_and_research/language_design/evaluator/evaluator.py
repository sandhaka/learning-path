from experiments_and_research.language_design.parser import Parser
from experiments_and_research.language_design.lexer import Lexer
from experiments_and_research.language_design.ast import (
    Identifier,
    PrefixExpression,
    InfixExpression,
    NumberLiteral,
    Boolean,
    GroupedExpression,
    ExpressionKind,
)


class Evaluator:
    def __init__(self, env=None):
        self.env = env or {}

    def evaluate(self, statement: str):
        lexer = Lexer(statement)
        parser = Parser(lexer)
        ast = parser.parse_expression()
        ret = self.evaluate_statement(ast)
        return ret

    def evaluate_statement(self, ast: any):
        if ast.kind == ExpressionKind.Identifier:
            return self.evaluate_identifier(ast)
        if ast.kind == ExpressionKind.Prefix:
            return self.evaluate_prefix(ast)
        if ast.kind == ExpressionKind.Infix:
            return self.evaluate_infix(ast)
        if ast.kind == ExpressionKind.NumberLiteral:
            return self.evaluate_integer(ast)
        if ast.kind == ExpressionKind.GroupedExpression:
            return self.evaluate_grouped_expression(ast)

    def evaluate_identifier(self, ast: Identifier):
        value = self.env.get(ast.literal, None)
        if value is None:
            raise RuntimeError(f"{ast.literal} is not defined")
        if self.is_numeric(value) or isinstance(value, str):
            return value
        return self.evaluate_statement(value)

    def evaluate_prefix(self, ast: PrefixExpression):
        operator = ast.literal
        right = self.evaluate_statement(ast.right)
        # if operator == "!":
        #     return not right
        if operator == "-":
            return -right
        raise SyntaxError(f"Unknown operator: {operator}")

    def evaluate_infix(self, ast: InfixExpression):
        def evaluate_numeric_infix(left_op, right_op, operator):
            if operator == "+":
                return left_op + right_op
            if operator == "-":
                return left_op - right_op
            if operator == "*":
                return left_op * right_op
            if operator == "/":
                return left_op / right_op
            if operator == "%":
                return left_op % right_op
            # Not available yet
            # if operator == "==":
            #     return left == right
            # if operator == "!=":
            #     return left != right
            raise SyntaxError(f"Unknown operator: {operator}")

        infix_operator = ast.literal
        if infix_operator == "=" and isinstance(ast.left, Identifier):
            right = self.evaluate_statement(ast.right)
            self.env[ast.left.literal] = right
            return right
        left = self.evaluate_statement(ast.left)
        right = self.evaluate_statement(ast.right)
        if self.is_numeric(left) and self.is_numeric(right):
            return evaluate_numeric_infix(left, right, infix_operator)
        return ast

    @staticmethod
    def evaluate_integer(ast: NumberLiteral):
        if "." in ast.literal:
            return float(ast.literal)
        return int(ast.literal)

    @staticmethod
    def is_numeric(obj):
        return isinstance(obj, int) or isinstance(obj, float)

    def evaluate_grouped_expression(self, ast: GroupedExpression):
        return self.evaluate_statement(ast.body)
