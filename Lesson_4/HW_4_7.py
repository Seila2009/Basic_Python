n = int(input("Введите факториал числа, которое нужно узнать: "))


def fact():
    res = 1
    for i in range(1, n + 1):
        res *= i
        yield res


for el in fact():
    print(el)
