from .bases import Node, ExpressionKind


class Identifier(Node):
    def __init__(self, value):
        super().__init__(ExpressionKind.Identifier, value)


class PrefixExpression(Node):
    def __init__(self, operator, right):
        super().__init__(ExpressionKind.Prefix, operator)
        self.right = right


class InfixExpression(Node):
    def __init__(self, left, operator, right):
        super().__init__(ExpressionKind.Infix, operator)
        self.left = left
        self.right = right


class IntegerLiteral(Node):
    def __init__(self, value):
        super().__init__(ExpressionKind.IntegerLiteral, value)


class Boolean(Node):
    def __init__(self, value):
        super().__init__(ExpressionKind.Boolean, value)


class GroupedExpression(Node):
    def __init__(self, expression):
        super().__init__(ExpressionKind.GroupedExpression, expression)
