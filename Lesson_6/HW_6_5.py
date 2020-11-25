class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки.'


class Pen(Stationery):

    def draw(self):
        return f'Отрисовка с использованием инструмента - {self.title}.'


class Pencil(Stationery):

    def draw(self):
        return f'Отрисовка с использованием инструмента - {self.title}.'


class Handle(Stationery):

    def draw(self):
        return f'Отрисовка с использованием инструмента - {self.title}.'


pen = Pen("Ручка")
pencil = Pencil("Карандаш")
handle = Handle("Маркер")
print(pen.draw())
print(pencil.draw())
print(handle.draw())
