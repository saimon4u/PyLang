from Lexer import Lexer
from Parser import Parser
from Interpreter import Interpreter
from Constant import Context


def run(filename, text):
    lexer = Lexer(filename, text)

    tokens, error = lexer.makeTokens()

    # print(tokens)

    if error:
        return None, error

    parser = Parser(tokens)

    ast = parser.parse()
    if ast.error:
        return None, ast.error

    interpreter = Interpreter()
    context = Context('<PyLang>')

    result = interpreter.visit(ast.node, context)

    return result.value, result.error
