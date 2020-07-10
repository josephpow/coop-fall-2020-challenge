class EventSourcer():
    # Do not change the signature of any function

    def __init__(self):
        self.value = 0
        self.eventStack = []
        self.redoStack = []

    def add(self, num: int):
        self.eventStack.append(num)
        self.value += num

    def subtract(self, num: int):
        self.eventStack.append(-num)
        self.value -= num

    def undo(self):
        if len(self.eventStack) > 0:
            event = self.eventStack.pop()
            self.value -= event
            self.redoStack.append(event)

    def redo(self):
        if len(self.redoStack) > 0:
            event = self.redoStack.pop()
            self.eventStack.append(event)
            self.value += event

    def bulk_undo(self, steps: int):
        for _ in range(min(len(self.eventStack), steps)):
            self.undo()

    def bulk_redo(self, steps: int):
        for _ in range(min(len(self.redoStack), steps)):
            self.redo()
