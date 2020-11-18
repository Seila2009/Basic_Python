from itertools import count

my_list = int(input('Введите начальное число: '))
stop_num = int(input('Введите конечное число: '))
for el in count(my_list):
    if el > stop_num:
        break
    else:
        print(el)

from itertools import cycle

elem = input('Введите повторяющийся элемент: ').split()
a = int(input('Введите количество повторений: '))
с = 1
for el in cycle(elem):
    if с > a:
        break
    print(el)
    с += 1