file = open("text.txt", 'w')
file_data = input('Введите любой текст: \n')
while file_data:
    file.writelines(file_data)
    file_data = input('Еще раз введите текст: \n')
    if not file_data:
        break

file.close()
file = open("text.txt", 'r')
content = file.readlines()
print(content)
file.close()
