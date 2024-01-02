from Error import RunningTimeError


class Number:
    def __init__(self, value):
        self.context = None
        self.endPos = None
        self.startPos = None
        self.value = value

    def setPos(self, startPos=None, endPos=None):
        self.startPos = startPos
        self.endPos = endPos
        return self

    def setContext(self, context=None):
        self.context = context
        return self

    def addition(self, other):
        if isinstance(other, Number):
            return Number(self.value + other.value).setContext(self.context), None

    def subtraction(self, other):
        if isinstance(other, Number):
            return Number(self.value - other.value).setContext(self.context), None

    def multiplication(self, other):
        if isinstance(other, Number):
            return Number(self.value * other.value).setContext(self.context), None

    def division(self, other):
        if isinstance(other, Number):
            if other.value == 0:
                return None, RunningTimeError(other.startPos, other.endPos, "Division by zero", self.context)
            return Number(self.value / other.value).setContext(self.context), None

    def __repr__(self):
        return str(self.value)
