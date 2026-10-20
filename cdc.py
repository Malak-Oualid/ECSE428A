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

    def add(self):
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a + b)


    
    def sub(self):
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a - b)

