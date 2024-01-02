from Number import Number
import Constant


class RuntimeResult:
    def __init__(self):
        self.value = None
        self.error = None

    def register(self, res):
        if res.error:
            self.error = res.error
        return res.value

    def success(self, value):
        self.value = value
        return self

    def failure(self, error):
        self.error = error
        return self


class Interpreter:
    def visit(self, node, context):
        methodName = f'visit_{type(node).__name__}'
        method = getattr(self, methodName, self.no_visit_method)
        return method(node, context)

    def no_visit_method(self, node):
        raise Exception(f'No visit_{type(node).__name__} method defined')

    def visit_NumberNode(self, node, context):
        return RuntimeResult().success(Number(node.token.value).setPos(node.startPos, node.endPos).setContext(context))

    def visit_BinaryOpNode(self, node, context):
        res = RuntimeResult()
        left = res.register(self.visit(node.leftNode, context))
        if res.error:
            return res
        right = res.register(self.visit(node.rightNode, context))
        if res.error:
            return res

        result = None
        error = None
        if node.opTok.tokenType == Constant.TT_PLUS:
            result, error = left.addition(right)

        elif node.opTok.tokenType == Constant.TT_MINUS:
            result, error = left.subtraction(right)

        elif node.opTok.tokenType == Constant.TT_MUL:
            result, error = left.multiplication(right)

        elif node.opTok.tokenType == Constant.TT_DIV:
            result, error = left.division(right)

        elif node.opTok.tokenType == Constant.TT_POW:
            result, error = left.power(right)

        if error:
            return res.failure(error)

        return res.success(result.setPos(node.startPos, node.endPos))

    def visit_UnaryOpNode(self, node, context):
        res = RuntimeResult()
        val = res.register(self.visit(node.node, context))
        if res.error:
            return res

        error = None

        if node.opTok.tokenType == Constant.TT_MINUS:
            val, error = val.multiplication(Number(-1))

        if error:
            return res.failure(error)
        return res.success(val.setPos(node.startPos, node.endPos))
