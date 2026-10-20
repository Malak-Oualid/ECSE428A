class Calculator:
    def __init__(self):
        self.stack = []

    def push(self, value):
        if isinstance(value, str):
            value = value.replace("j", "").replace("+", "+")
            if "+" in value[1:]:
                real, imag = value.split("+")
                value = complex(float(real), float(imag))
            elif "-" in value[1:]:
                index = value.find("-", 1)
                real = value[:index]
                imag = value[index:]
                value = complex(float(real), float(imag))

        self.stack.append(value)


    def sub(self):
        if len(self.stack) < 2:
            raise ValueError("Error: stack underflow")

        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a - b)


    def delete(self):
        if len(self.stack) < 1:
            raise ValueError("Error: stack underflow")

        self.stack.pop()


    def add(self):
        if len(self.stack) < 2:
            raise ValueError("Error: stack underflow")

        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a + b)
