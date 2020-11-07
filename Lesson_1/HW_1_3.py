n = int(input("Введите целое положительное число: "))
sum_n = 0
for i in range(3):
    sum_n += int(str(n) + i * str(n))
print(sum_n)