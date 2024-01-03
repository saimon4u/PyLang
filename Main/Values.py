# from Interpreter import *
from Constant import Context, SymbolTable
import Interpreter
from Error import RunningTimeError

class Value:
    def __init__(self):
        self.context = None
        self.endPos = None
        self.startPos = None

    def setPos(self, startPos=None, endPos=None):
        self.startPos = startPos
        self.endPos = endPos
        return self

    def setContext(self, context=None):
        self.context = context
        return self

    def addition(self, other):
        return None, self.illegalOperation(other)

    def subtraction(self, other):
        return None, self.illegalOperation(other)

    def multiplication(self, other):
        return None, self.illegalOperation(other)

    def division(self, other):
        return None, self.illegalOperation(other)

    def power(self, other):
        return None, self.illegalOperation(other)

    def equal(self, other):
        return None, self.illegalOperation(other)

    def notEqual(self, other):
        return None, self.illegalOperation(other)

    def greaterThan(self, other):
        return None, self.illegalOperation(other)

    def greaterThanEqual(self, other):
        return None, self.illegalOperation(other)

    def lesserThan(self, other):
        return None, self.illegalOperation(other)

    def lesserThanEqual(self, other):
        return None, self.illegalOperation(other)

    def bitwiseOr(self, other):
        return None, self.illegalOperation(other)

    def bitwiseAnd(self, other):
        return None, self.illegalOperation(other)

    def notOperation(self):
        return None, self.illegalOperation()

    def execute(self, args):
        res = Interpreter.RuntimeResult()
        return res.failure(self.illegalOperation())

    def copy(self):
        raise Exception('No copy method defined')

    def isTrue(self):
        return False

    def illegalOperation(self, other=None):
        if other is None:
            other = self

        return RunningTimeError(self.startPos, self.endPos, 'Illegal Operation', self.context)


class Number(Value):
    def __init__(self, value):
        super().__init__()
        self.context = None
        self.endPos = None
        self.startPos = None
        self.value = value

    def addition(self, other):
        if isinstance(other, Number):
            return Number(self.value + other.value).setContext(self.context), None
        else:
            return None, Value.illegalOperation(self, other)

    def subtraction(self, other):
        if isinstance(other, Number):
            return Number(self.value - other.value).setContext(self.context), None
        else:
            return None, Value.illegalOperation(self, other)

    def multiplication(self, other):
        if isinstance(other, Number):
            return Number(self.value * other.value).setContext(self.context), None
        else:
            return None, Value.illegalOperation(self, other)

    def power(self, other):
        if isinstance(other, Number):
            return Number(self.value ** other.value).setContext(self.context), None
        else:
            return None, Value.illegalOperation(self, other)

    def division(self, other):
        if isinstance(other, Number):
            if other.value == 0:
                return None, RunningTimeError(other.startPos, other.endPos, "Division by zero", self.context)
            return Number(self.value / other.value).setContext(self.context), None
        else:
            return None, Value.illegalOperation(self, other)

    def equal(self, other):
        if isinstance(other, Number):
            return Number(int(self.value == other.value)).setContext(self.context), None
        else:
            return None, Value.illegalOperation(self, other)

    def notEqual(self, other):
        if isinstance(other, Number):
            return Number(int(self.value != other.value)).setContext(self.context), None
        else:
            return None, Value.illegalOperation(self, other)

    def greaterThan(self, other):
        if isinstance(other, Number):
            return Number(int(self.value > other.value)).setContext(self.context), None
        else:
            return None, Value.illegalOperation(self, other)

    def greaterThanEqual(self, other):
        if isinstance(other, Number):
            return Number(int(self.value >= other.value)).setContext(self.context), None
        else:
            return None, Value.illegalOperation(self, other)

    def lesserThan(self, other):
        if isinstance(other, Number):
            return Number(int(self.value < other.value)).setContext(self.context), None
        else:
            return None, Value.illegalOperation(self, other)

    def lesserThanEqual(self, other):
        if isinstance(other, Number):
            return Number(int(self.value <= other.value)).setContext(self.context), None
        else:
            return None, Value.illegalOperation(self, other)

    def bitwiseAnd(self, other):
        if isinstance(other, Number):
            return Number(int(self.value and other.value)).setContext(self.context), None
        else:
            return None, Value.illegalOperation(self, other)

    def bitwiseOr(self, other):
        if isinstance(other, Number):
            return Number(int(self.value or other.value)).setContext(self.context), None
        else:
            return None, Value.illegalOperation(self, other)

    def notOperation(self):
        return Number(1 if self.value == 0 else 0).setContext(self.context), None

    def isTrue(self):
        return self.value != 0

    def copy(self):
        copy = Number(self.value)
        copy.setPos(self.startPos, self.endPos)
        copy.setContext(self.context)
        return copy

    def __repr__(self):
        return str(self.value)
    
    
class String(Value):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def addition(self, other):
        if isinstance(other, String):
            return String(self.value + other.value).setContext(self.context), None
        else:
            return None, Value.illegalOperation(self, other)

    def multiplication(self, other):
        if isinstance(other, Number):
            return String(self.value * other.value).setContext(self.context), None
        else:
            return None, Value.illegalOperation(self, other)

    def isTrue(self):
        return len(self.value) > 0

    def copy(self):
        copy = String(self.value)
        copy.setContext(self.context)
        copy.setPos(self.startPos, self.endPos)
        return copy

    def __repr__(self):
        return f'"{self.value}"'

class List(Value):
    def __init__(self, elements):
        super().__init__()
        self.elements = elements

    def addition(self, other):
        newList = self.copy()
        newList.elements.append(other)
        return newList, None

    def multiplication(self, other):
        if isinstance(other, List):
            newList = self.copy()
            newList.elements.extend(other.elements)
            return newList, None
        else:
            return None, Value.illegalOperation(self, other)

    def subtraction(self, other):
        if isinstance(other, Number):
            newList = self.copy()
            try:
                newList.elements.pop(other.value)
                return newList, None
            except:
                return None, RunningTimeError(other.startPos, other.endPos,
                                              "Element at this index could not be removed from the list because" +
                                              "index is out of bounds", self.context)
        else:
            return None, Value.illegalOperation(self, other)

    def division(self, other):
        if isinstance(other, Number):
            try:
                return self.elements[other.value], None
            except:
                return None, RunningTimeError(other.startPos, other.endPos,
                                              "Element at this index could not be retrieved from the list because" +
                                              "index is out of bounds", self.context)
        else:
            return None, Value.illegalOperation(self, other)

    def copy(self):
        copy = List(self.elements[:])
        copy.setPos(self.startPos, self.endPos)
        copy.setContext(self.context)
        return copy

    def __repr__(self):
        return f'[{",".join([str(x) for x in self.elements])}]'


class Function(Value):
    def __init__(self, name, bodyNode, argNames):
        super().__init__()
        self.name = name or "<anonymous>"
        self.bodyNode = bodyNode
        self.argNames = argNames

    def execute(self, args):
        res = Interpreter.RuntimeResult()
        interpreter = Interpreter.Interpreter()

        newContext = Context(self.name, self.context, self.startPos)
        newContext.symbolTable = SymbolTable(newContext.parent.symbolTable)

        if len(args) > len(self.argNames):
            return res.failure(RunningTimeError(self.startPos, self.endPos,
                                                f"{len(args) - len(self.argNames)} too many args passed into '{self.name}'",
                                                self.context))

        if len(args) < len(self.argNames):
            return res.failure(RunningTimeError(self.startPos, self.endPos,
                                                f"{len(self.argNames) - len(args)} too few args passed into '{self.name}'",
                                                self.context))

        for i in range(len(args)):
            argName = self.argNames[i]
            argValue = args[i]
            argValue.setContext(newContext)
            newContext.symbolTable.set(argName, argValue)

        value = res.register(interpreter.visit(self.bodyNode, newContext))
        if res.error:
            return res

        return res.success(value)

    def copy(self):
        copy = Function(self.name, self.bodyNode, self.argNames)
        copy.setContext(self.context)
        copy.setPos(self.startPos, self.endPos)
        return copy

    def __repr__(self):
        return f"<function {self.name}>"
