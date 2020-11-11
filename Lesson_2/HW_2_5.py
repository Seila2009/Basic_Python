my_list = [15, 14.5, 14, 13, 11, 10, 7, 6, 4, 4, 4, 3, 2, 1]
user_num = int(input("Введите какое-нибудь число: "))
fl = False
for i in my_list:
    if user_num > i:
        a = my_list.index(i)
        my_list.insert(a, user_num)
        fl = True
        break
if not fl:
    my_list.append(user_num)
print(my_list)