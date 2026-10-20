class Calculator:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)
