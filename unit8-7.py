class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.complex = "a + i * b"

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNumber(self.a * other.a, self.b * other.b)

    def __str__(self):
        return f'complex = {self.a} + i*{self.b}'


x = ComplexNumber(3, 7)
y = ComplexNumber(2, 8)
print(x)
print(y)
print(x + y)
print(x * y)
