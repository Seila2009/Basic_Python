my_list = [28, 85, 9542, 85, 74, 963, 852, 789, 521, 56, 7125, 62, 1]
new_list = []
for el in range(len(my_list) - 1):
    n = my_list[el]
    el += 1
    m = my_list[el]
    if m > n:
        new_list.append(m)

print(f"Новый список: {new_list}")
