def fact(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


g = int(input("Введите факториал числа, которое нужно узнать: "))
for el in range(1, g + 1):
    print(fact(el))