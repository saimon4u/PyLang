class NumberNode:
    def __init__(self, token):
        self.token = token
        self.startPos = token.startPos
        self.endPos = token.endPos

    def __repr__(self):
        return f'{self.token}'


class BinaryOpNode:
    def __init__(self, leftNode, opTok, rightNode):
        self.leftNode = leftNode
        self.opTok = opTok
        self.rightNode = rightNode
        self.startPos = leftNode.startPos
        self.endPos = rightNode.endPos

    def __repr__(self):
        return f'({self.leftNode}, {self.opTok}, {self.rightNode})'


class UnaryOpNode:
    def __init__(self, opTok, node):
        self.opTok = opTok
        self.node = node
        self.startPos = opTok.startPos
        self.endPos = node.endPos

    def __repr__(self):
        return f'({self.opTok}, {self.node})'


class VarAccessNode:
    def __init__(self, varNameTok):
        self.varNameTok = varNameTok
        self.startPos = varNameTok.startPos
        self.endPos = varNameTok.endPos


class VarAssignNode:
    def __init__(self, varNameTok, valueNode):
        self.varNameTok = varNameTok
        self.valueNode = valueNode

        self.startPos = self.varNameTok.startPos
        self.endPos = self.valueNode.endPos


class IfNode:
    def __init__(self, cases, elseCase):
        self.cases = cases
        self.elseCase = elseCase

        self.startPos = self.cases[0][0].startPos
        self.endPos = (self.elseCase or self.cases[len(self.cases) - 1][0]).endPos
