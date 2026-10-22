class Calculator:
    def __init__(self):
        self.stack = []


    
    def push(self, value):
        if isinstance(value, str):
            try:
                if value.startswith("j"):
                    value = complex(0, float(value[1:]))

                elif value.startswith("-j"):
                    value = complex(0, -float(value[2:]))

                else:
                    value = value.replace("j", "")

                    if "+" in value[1:]:
                        real, imag = value.split("+")
                        value = complex(float(real), float(imag))

                    elif "-" in value[1:]:
                        index = value.find("-", 1)
                        real = value[:index]
                        imag = value[index:]
                        value = complex(float(real), float(imag))

                    else:
                        value = float(value)

            except (ValueError, TypeError):
                raise ValueError("Error: invalid token") from None

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
        sign = "-" if value.imag < 0 else "+"
        return f"{value.real:g} {sign} j{abs(value.imag):g}"


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
    if "j" not in text:
        return complex(text)
    return complex(text.replace("j", "") + "j")


COMMANDS = ("push", "pop", "mul", "div")


def run(text):
    tokens = text.split()
    calc = Calculator()
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
            elif token == "mul":
                calc.mul()
            elif token == "div":
                calc.div()
            elif token == "pop":
                return calc.pop()
            i += 1
    except IndexError:
        return "Error: stack underflow"
    except ZeroDivisionError:
        return "Error: division by zero"
