from bases import Node, ExpressionKind


class Identifier(Node):
    def __init__(self, value):
        super().__init__(ExpressionKind.Identifier, value)
