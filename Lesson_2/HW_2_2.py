My_list = list(input("Введите какое-нибудь число: "))
for i in range(0, len(My_list) - 1, 2):
    My_list[i], My_list[i + 1] = My_list[i + 1], My_list[i]
print(My_list)