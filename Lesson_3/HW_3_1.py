def my_func():
    a = int(input('Введите делимое: '))
    b = int(input('Введите делитель: '))
    if b == 0:
        print('Некорректные значения. Делитель равен нулю.')
    else:
        res = a / b
        return res
print(round(my_func(), 2))
