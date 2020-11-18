def int_func(a):
    words = a.title()
    return words


print(int_func(input("Введите пробное слово: ")))
y = input("Введите несколько слов, разделенных пробелом: ").split()
d = list(map(int_func, y))
s = ' '.join(d)
print(s)
