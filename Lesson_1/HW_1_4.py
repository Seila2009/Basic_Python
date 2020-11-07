n = int(input("Введите целое положительное число "))
a = []
while n > 0:
    a.append(n % 10)
    n //= 10
max_a = max(a)
print(max_a)