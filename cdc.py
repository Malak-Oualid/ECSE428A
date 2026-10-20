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
