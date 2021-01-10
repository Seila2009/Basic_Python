class MyException:
    def __init__(self, *args):
        self.my_exception = []

    def my_input(self):
        while True:
            try:
                try:
                    val = int(input('Введите значения для списка и нажимайте Enter: '))
                    self.my_exception.append(val)
                    print(f'Список - {self.my_exception}.')
                    next_val = input('Продолжаем? Y/N: ').lower()

                    if next_val == 'n':
                        print(self.my_exception)
                        break
                except ValueError:
                    raise MyException
            except MyException:
                print(f"Недопустимое значение. Введите числовые значения.")
                second_chance = input(f'Попробовать еще раз? Y/N ').lower()
                if second_chance == 'n':
                    print(self.my_exception)
                    break
                else:
                    self.my_input()


try_except = MyException()
try_except.my_input()
