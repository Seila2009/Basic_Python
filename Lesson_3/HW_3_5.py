def user_sum():
    res = 0
    while True:
        num = input("Введите числа, разделенных пробелом (для завершения поставьте восклицательный знак !): ")
        for num in num.split():
            if num == "!":
                break
            else:
                res += float(num)
        return num


print(user_sum())