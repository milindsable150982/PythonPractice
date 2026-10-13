class MathOperator:

    a : int = 0
    b : int = 0

    def __init__(self):
        self.a = 8
        self.b = 2

    def Add(self):
        return self.a + self.b

    def Subtract(self):
        return self.a - self.b    

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b == 0:
            return "Error: Division by zero"
        return self.a / self.b;