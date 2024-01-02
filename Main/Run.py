from Lexer import Lexer
from Parser import Parser
from Interpreter import Interpreter
from Constant import Context
from Constant import SymbolTable
from Number import Number

table = SymbolTable()
table.set('null', Number(0))
table.set('true', Number(1))
table.set('false', Number(0))


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
