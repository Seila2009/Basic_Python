def my_func(x, y):
    return 1 / x ** (y * -1)


print(my_func(x=int(input("Введите число: ")),
              y=int(input("Введите отрицательную степень: "))))


def my_func2(x, y):
    res = 1
    while y < 0:
        res = res * x
        y += 1
    return 1 / res


print(my_func2(x=int(input("Введите число: ")),
               y=int(input("Введите отрицательную степень: "))))
