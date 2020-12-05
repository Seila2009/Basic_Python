class Complex:
    def __init__(self, x, y, *args):
        self.x = x
        self.y = y
        self.z = 'x + y * i'

    def __add__(self, other):
        print(f'Сумма комплексных чисел равна:')
        return f'z = {self.x + other.x} + {self.y + other.y} * i'

    def __mul__(self, other):
        print(f'Произведение комплексных чисел равно:')
        return f'z = {self.x * other.x - (self.y * other.y)} + {self.y * other.x} * i'

    def __str__(self):
        return f'z = {self.x} + {self.y} * i'


z_1 = Complex(5, 4)
z_2 = Complex(15, -3)
print(z_1 + z_2)
print(z_1 * z_2)
