class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'Результат операции {self.quantity * "*"}'

    def __add__(self, other):
        return f'Клеток прибавилось: {self.quantity + other.quantity}'

    def __sub__(self, other):
        sub = self.quantity - other.quantity
        return f'То, что осталось от клеток Т_Т: {sub} ' if sub > 0 else 'Её больше нет'

    def __truediv__(self, other):
        return f'Клетки вымирают! Сейчас их {self.quantity // other.quantity} штук.'

    def __mul__(self, other):
        return f'Клетки множатся и почкуются. Теперь их {self.quantity * other.quantity}.'

    def make_order(self, rank):
        res = ''
        for i in range(int(self.quantity / rank)):
            res += '*' * rank + '\\n'
        res += '*' * (self.quantity % rank) + '\\n'
        return res


cell = Cell(15)
cell_2 = Cell(5)
print(cell)
print(cell + cell_2)
print(cell - cell_2)
print(cell / cell_2)
print(cell * cell_2)
print(cell.make_order(10))
