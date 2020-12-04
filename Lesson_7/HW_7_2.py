class Clothes:

    def __init__(self, width, height):
        self.w = width
        self.h = height

    @property
    def get_sq_full(self):
        return f'Общее количество затраченной ткани: {self.w / 6.5 + 0.5 + 2 * self.h + 0.3 :.2f} квадратных метров'


class Coat(Clothes):
    def get_sq_full(self):
        return f'Расход ткани для пальто: {self.w / 6.5 + 0.5 :.2f} квадратных метров ткани'


class Costume(Clothes):
    def get_sq_full(self):
        return f'Расход ткани для костюма: {2 * self.h + 0.3 :.2f} квадратных метров ткани'


coat = Coat(40, 30)
costume = Costume(55, 75)
clothes = Clothes(Costume, Coat)
print(coat.get_sq_full())
print(costume.get_sq_full())
print(get_sq_full())
# Тут появляется ошибка поподсчету общей суммы, не могу понять как с ней разобраться
