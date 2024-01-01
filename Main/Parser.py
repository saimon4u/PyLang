import Constant
from Nodes import NumberNode, BinaryOpNode, UnaryOpNode
from Error import InvalidSyntaxError


class ParseResult:
    def __init__(self):
        self.error = None
        self.node = None

    def register(self, res):
        if isinstance(res, ParseResult):
            if res.error:
                self.error = res.error
            return res.node
        return res

    def success(self, node):
        self.node = node
        return self

    def failure(self, error):
        self.error = error
        return self


class Parser:
    def __init__(self, tokens):
        self.currentTok = None
        self.tokens = tokens
        self.tokIdx = -1
        self.advance()

    def advance(self):
        self.tokIdx += 1
        if self.tokIdx < len(self.tokens):
            self.currentTok = self.tokens[self.tokIdx]

        return self.currentTok

    def parse(self):
        res = self.expression()

        if not res.error and self.currentTok.tokenType != Constant.TT_EOF:
            return res.failure(InvalidSyntaxError(self.currentTok.startPos, self.currentTok.endPos, "Expected '+', "
                                                                                                    "'-', '*' or '/'"))

        return res

    def factor(self):
        res = ParseResult()
        token = self.currentTok

        if token.tokenType in (Constant.TT_PLUS, Constant.TT_MINUS):
            res.register(self.advance())
            factor = res.register(self.factor())
            if res.error:
                return res
            return res.success(UnaryOpNode(token, factor))

        elif token.tokenType in (Constant.TT_INT, Constant.TT_FLOAT):
            res.register(self.advance())
            return res.success(NumberNode(token))

        elif token.tokenType == Constant.TT_LPAREN:
            res.register(self.advance())
            expr = res.register(self.expression())
            if res.error:
                return res

            if self.currentTok.tokenType == Constant.TT_RPAREN:
                res.register(self.advance())
                return res.success(expr)
            else:
                return res.failure(InvalidSyntaxError(self.currentTok.startPos, self.currentTok.endPos, "Expected ')'"))

        return res.failure(InvalidSyntaxError(token.startPos, token.endPos, "Expected int or float"))

    def term(self):
        return self.binaryOperation(self.factor, (Constant.TT_MUL, Constant.TT_DIV))

    def expression(self):
        return self.binaryOperation(self.term, (Constant.TT_MINUS, Constant.TT_PLUS))

    def binaryOperation(self, func, opTokens):
        res = ParseResult()
        left = res.register(func())
        if res.error:
            return res
        while self.currentTok.tokenType in opTokens:
            opTok = self.currentTok
            res.register(self.advance())
            right = res.register(func())
            if res.error:
                return res

            left = BinaryOpNode(left, opTok, right)

        return res.success(left)
