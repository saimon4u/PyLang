

class NumberNode:
    def __init__(self, token):
        self.token = token

    def __repr__(self):
        return f'{self.token}'


class BinaryOpNode:
    def __init__(self, leftNode, opTok, rightNode):
        self.leftNode = leftNode
        self.opTok = opTok
        self.rightNode = rightNode

    def __repr__(self):
        return f'({self.leftNode}, {self.opTok}, {self.rightNode})'

class UnaryOpNode:
    def __init__(self, opTok, node):
        self.opTok = opTok
        self.node = node

    def __repr__(self):
        return f'({self.opTok}, {self.node})'
