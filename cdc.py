import sys


class Calculator:
    def __init__(self):
        self.stack = []

    def push(self, value):
        if isinstance(value, str):
            value = parse_number(value)
        self.stack.append(value)

    def mul(self):
        x = self.stack.pop()
        y = self.stack.pop()
        self.stack.append(y * x)

    def div(self):
        x = self.stack.pop()
        y = self.stack.pop()
        self.stack.append(y / x)

    def pop(self):
        value = complex(self.stack.pop())
        real = value.real or 0.0
        sign = "-" if value.imag < 0 else "+"
        return f"{real:g} {sign} j{abs(value.imag):g}"


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


def parse_number(text):
    text = text.replace(" ", "")
    try:
        if "j" not in text:
            return complex(text)
        return complex(text.replace("j", "") + "j")
    except ValueError:
        raise ValueError("Error: invalid token") from None


COMMANDS = ("push", "pop", "add", "sub", "mul", "div", "delete")


def run(text):
    tokens = text.lower().split()
    calc = Calculator()
    outputs = []
    try:
        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token == "push":
                number = []
                while i + 1 < len(tokens) and tokens[i + 1] not in COMMANDS:
                    i += 1
                    number.append(tokens[i])
                calc.push(parse_number(" ".join(number)))
            elif token == "add":
                calc.add()
            elif token == "sub":
                calc.sub()
            elif token == "mul":
                calc.mul()
            elif token == "div":
                calc.div()
            elif token == "delete":
                calc.delete()
            elif token == "pop":
                outputs.append(calc.pop())
            else:
                raise ValueError("Error: invalid token")
            i += 1
        if outputs:
            return "\n".join(outputs)
    except IndexError:
        return "Error: stack underflow"
    except ZeroDivisionError:
        return "Error: division by zero"
    except ValueError as error:
        return str(error)


if __name__ == "__main__":
    output = run(" ".join(sys.argv[1:]))
    if output is not None:
        print(output)
