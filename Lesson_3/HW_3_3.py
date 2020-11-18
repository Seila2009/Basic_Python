def my_func(a, b, c):
    sum_val = sum(a + b + c)
    min_val = min(a, b, c)
    res = sum_val - min_val
    return res


print(my_func(a=int(input("Введите первое число: ")),
              b=int(input("Введите второе число: ")),
              c=int(input("Введите третье число: "))))
