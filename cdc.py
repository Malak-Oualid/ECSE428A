class Calculator:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def mul(self):
        x = self.stack.pop()
        y = self.stack.pop()
        self.stack.append(y * x)

    def pop(self):
        value = self.stack.pop()
        return f"{value} + j0"
