with open("list_num.txt", 'w+') as list_num:
    file_data = input('Введите любые числа через пробел: ')
    list_num.writelines(file_data)
    my_num = file_data.split()

print(sum(map(int, my_num)))

