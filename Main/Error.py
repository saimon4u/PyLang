from StringWithArrow import string_with_arrows


class Error:
    def __init__(self, startPos, endPos, errorName, details):
        self.startPos = startPos
        self.endPos = endPos
        self.errorName = errorName
        self.details = details

    def as_string(self):
        result = f'{self.errorName}: {self.details}\n'
        result += f'File {self.startPos.filename}, line {self.startPos.lineNumber + 1}'
        result += '\n' + string_with_arrows(self.startPos.content, self.startPos, self.endPos)
        return result


class IllegalCharError(Error):
    def __init__(self, startPos, endPos, details):
        super().__init__(startPos, endPos, 'Illegal Character', details)


class InvalidSyntaxError(Error):
    def __init__(self, startPos, endPos, details):
        super().__init__(startPos, endPos, 'Invalid Syntax', details)