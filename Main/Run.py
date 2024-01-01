from Lexer import Lexer


def run(filename, text):
    lexer = Lexer(filename, text)

    tokens, error = lexer.makeTokens()

    return tokens, error
