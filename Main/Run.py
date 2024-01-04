import math

from Lexer import Lexer
from Parser import Parser
from Interpreter import Interpreter
from Constant import Context
from Constant import SymbolTable
from Values import Number, BuiltInFunction


Number.null = Number(0)
Number.true = Number(1)
Number.false = Number(0)
Number.PI = Number(math.pi)
BuiltInFunction.print = BuiltInFunction('print')
BuiltInFunction.input = BuiltInFunction('input')
BuiltInFunction.inputInt = BuiltInFunction('inputInt')
BuiltInFunction.isNumber = BuiltInFunction('isNumber')
BuiltInFunction.isString = BuiltInFunction('isString')
BuiltInFunction.isList = BuiltInFunction('isList')
BuiltInFunction.isFunction = BuiltInFunction('isFunction')
BuiltInFunction.push = BuiltInFunction('push')
BuiltInFunction.pop = BuiltInFunction('pop')
BuiltInFunction.extend = BuiltInFunction('extend')
BuiltInFunction.len = BuiltInFunction('len')
BuiltInFunction.run = BuiltInFunction('run')
BuiltInFunction.int = BuiltInFunction('int')
BuiltInFunction.str = BuiltInFunction('str')


table = SymbolTable()
table.set('null', Number.null)
table.set('true', Number.true)
table.set('false', Number.false)
table.set('MATH_PI', Number.PI)
table.set('print', BuiltInFunction.print)
table.set('input', BuiltInFunction.input)
table.set('inputInt', BuiltInFunction.inputInt)
table.set('isNumber', BuiltInFunction.isNumber)
table.set('isString', BuiltInFunction.isString)
table.set('isList', BuiltInFunction.isList)
table.set('isFunction', BuiltInFunction.isFunction)
table.set('push', BuiltInFunction.push)
table.set('pop', BuiltInFunction.pop)
table.set('extend', BuiltInFunction.extend)
table.set('len', BuiltInFunction.len)
table.set('run', BuiltInFunction.run)
table.set('int', BuiltInFunction.int)
table.set('str', BuiltInFunction.str)


def run(filename, text):
    lexer = Lexer(filename, text)

    tokens, error = lexer.makeTokens()

    if error:
        return None, error

    parser = Parser(tokens)

    ast = parser.parse()

    if ast.error:
        return None, ast.error

    interpreter = Interpreter()
    context = Context('<PyLang>')
    context.symbolTable = table

    result = interpreter.visit(ast.node, context)

    return result.value, result.error
