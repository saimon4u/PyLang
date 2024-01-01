from Lexer import Lexer
from Parser import Parser


def run(filename, text):
    lexer = Lexer(filename, text)

    tokens, error = lexer.makeTokens()

    # print(tokens)

    if error:
        return None, error

    parser = Parser(tokens)

    ast = parser.parse()

    return ast.node, ast.error
