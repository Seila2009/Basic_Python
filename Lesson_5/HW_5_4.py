rus_num = {"One": "Один",
           "Two": "Два",
           "Three": "Три",
           "Four": "Четыре"
           }
new_num = []
with open('numbers.txt', 'r', encoding='utf-8') as en_num, open("numbers_rus.txt", 'w', encoding='utf-8') as my_num:
    for i in en_num:
        print(i)
        i = i.split(" ", 1)
        new_num.append(rus_num[i[0]] + " " + i[1])
    my_num.writelines(new_num)
print(new_num)



