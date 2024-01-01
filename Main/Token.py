class Token:
    def __init__(self, tokenType, value=None):
        self.tokenType = tokenType
        self.value = value

    def __repr__(self):
        if self.value is not None:
            return f'{self.tokenType}:{self.value}'
        return f'{self.tokenType}'
