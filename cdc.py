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
        value = complex(self.stack.pop())
        sign = "-" if value.imag < 0 else "+"
        return f"{value.real:g} {sign} j{abs(value.imag):g}"


def parse_number(text):
    text = text.replace(" ", "")
    if "j" not in text:
        return complex(text)
    return complex(text.replace("j", "") + "j")


def run(text):
    tokens = text.split()
    calc = Calculator()
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token == "push":
            i += 1
            calc.push(parse_number(tokens[i]))
        elif token == "mul":
            calc.mul()
        elif token == "pop":
            return calc.pop()
        i += 1
