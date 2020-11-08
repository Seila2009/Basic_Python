a = int(input("Введите количество секунд "))
hour = ((a // 3600) % 24)
minute = (a // 60) % 60
second = a % 60
stroka = f"{hour:02}:{minute:02}:{second:02}"
print(stroka)