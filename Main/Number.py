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

    def power(self, other):
        if isinstance(other, Number):
            return Number(self.value ** other.value).setContext(self.context), None

    def division(self, other):
        if isinstance(other, Number):
            if other.value == 0:
                return None, RunningTimeError(other.startPos, other.endPos, "Division by zero", self.context)
            return Number(self.value / other.value).setContext(self.context), None

    def equal(self, other):
        if isinstance(other, Number):
            return Number(int(self.value == other.value)).setContext(self.context), None

    def notEqual(self, other):
        if isinstance(other, Number):
            return Number(int(self.value != other.value)).setContext(self.context), None

    def greaterThan(self, other):
        if isinstance(other, Number):
            return Number(int(self.value > other.value)).setContext(self.context), None

    def greaterThanEqual(self, other):
        if isinstance(other, Number):
            return Number(int(self.value >= other.value)).setContext(self.context), None

    def lesserThan(self, other):
        if isinstance(other, Number):
            return Number(int(self.value < other.value)).setContext(self.context), None

    def lesserThanEqual(self, other):
        if isinstance(other, Number):
            return Number(int(self.value <= other.value)).setContext(self.context), None

    def bitwiseAnd(self, other):
        if isinstance(other, Number):
            return Number(int(self.value and other.value)).setContext(self.context), None

    def bitwiseOr(self, other):
        if isinstance(other, Number):
            return Number(int(self.value or other.value)).setContext(self.context), None

    def notOperation(self):
        return Number(1 if self.value == 0 else 0).setContext(self.context), None

    def copy(self):
        copy = Number(self.value)
        copy.setPos(self.startPos, self.endPos)
        copy.setContext(self.context)
        return copy

    def __repr__(self):
        return str(self.value)
