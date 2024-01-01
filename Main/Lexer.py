from Constant import Position
import Constant
from Token import Token
from Error import IllegalCharError


class Lexer:
    def __init__(self, filename, text):
        self.currentChar = None
        self.filename = filename
        self.text = text
        self.position = Position(-1, 0, -1, filename, text)
        self.advance()

    def advance(self):
        self.position.advance(self.currentChar)
        self.currentChar = self.text[self.position.index] if self.position.index < len(self.text) else None

    def makeTokens(self):

        tokens = []

        while self.currentChar is not None:
            if self.currentChar in ' \t':
                self.advance()

            elif self.currentChar in Constant.DIGITS:
                tokens.append(self.makeNumber())

            elif self.currentChar == '+':
                tokens.append(Token(Constant.TT_PLUS, startPos=self.position))
                self.advance()

            elif self.currentChar == '-':
                tokens.append(Token(Constant.TT_MINUS, startPos=self.position))
                self.advance()

            elif self.currentChar == '*':
                tokens.append(Token(Constant.TT_MUL, startPos=self.position))
                self.advance()

            elif self.currentChar == '/':
                tokens.append(Token(Constant.TT_DIV, startPos=self.position))
                self.advance()

            elif self.currentChar == '(':
                tokens.append(Token(Constant.TT_LPAREN, startPos=self.position))
                self.advance()

            elif self.currentChar == ')':
                tokens.append(Token(Constant.TT_RPAREN, startPos=self.position))
                self.advance()

            else:
                startPos = self.position.copy()
                char = self.currentChar
                self.advance()
                return [], IllegalCharError(startPos, self.position, "'" + char + "'")

        tokens.append(Token(Constant.TT_EOF, startPos=self.position))
        return tokens, None

    def makeNumber(self):
        numStr = ''
        dotCount = 0
        pos = self.position.copy()

        while self.currentChar is not None and self.currentChar in Constant.DIGITS + '.':
            if self.currentChar == '.':
                if dotCount == 1: break
                dotCount += 1
                numStr += '.'

            else:
                numStr += self.currentChar

            self.advance()

        if dotCount == 0:
            return Token(Constant.TT_INT, int(numStr), startPos=pos, endPos=self.position)
        else:
            return Token(Constant.TT_FLOAT, float(numStr), startPos=pos, endPos=self.position)

