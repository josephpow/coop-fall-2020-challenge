class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.eventStack = []
        self.redoStack = []

    def add(self, num: int):
        self.eventStack.append(num)
        self.value += num
        pass

    def subtract(self, num: int):
        self.eventStack.append(-num)
        self.value -= num
        pass

    def undo(self):
        if len(self.eventStack) > 0:
            event = self.eventStack.pop()
            self.value -= event
            self.redoStack.append(event)
        pass

    def redo(self):
        if len(self.redoStack) > 0:
            event = self.redoStack.pop()
            self.value += event
        pass

    def bulk_undo(self, steps: int):
        while steps > 0:
            self.undo()
            steps -= 1
        pass

    def bulk_redo(self, steps: int):
        while steps > 0:
            self.redo()
            steps -= 1
        pass
