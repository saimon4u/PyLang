DIGITS = '0123456789'


TT_INT = 'INT'
TT_FLOAT = 'FLOAT'
TT_PLUS = 'PLUS'
TT_MINUS = 'MINUS'
TT_DIV = 'DIV'
TT_MUL = 'MUL'
TT_LPAREN = 'LPAREN'
TT_RPAREN = 'RPAREN'
TT_EOF = 'EOF'


class Position:
    def __init__(self, index, lineNumber, colNumber, filename, content):
        self.lineNumber = lineNumber
        self.colNumber = colNumber
        self.index = index
        self.filename = filename
        self.content = content

    def advance(self, currentChar=None):
        self.index += 1
        self.colNumber += 1

        if currentChar == '\n':
            self.lineNumber += 1
            self.colNumber = 0

        return self

    def copy(self):
        return Position(self.index, self.lineNumber, self.colNumber, self.filename, self.content)

