class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


def my_func():
    try:
        a = int(input('Введите делимое: '))
        b = int(input('Введите делитель: '))
        if b == 0:
            raise MyError("Делить на ноль нельзя!")
        else:
            c = a / b
            return c
    except ValueError:
        return "Вы ввели не число"
    except MyError as error:
        return error


print(my_func())
