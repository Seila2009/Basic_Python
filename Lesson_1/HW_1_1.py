print('Привет всем!')
a = input('Меня зовут Оля. Хочешь решить загадку? Введи слово "Да" или "Нет" с заглавной буквы: ')

if a == "Да":
    print("Здорово! Первая загадка:")
    print("Бабушка вязала внукам шарфы и варежки. Всего она связала 3 шарфа и 6 варежек.")
    b = int(input("Сколько внуков у бабушки? Введи целое число: "))
    if b < 3:
        print("К сожалению, это не так. Их 3-ое.")
    elif b > 3:
        print("Ты не угадал. Их 3-ое.")
    else:
        print("Да! Их 3-ое")
    c = (input('Как насчет еще одной? Введи слово "Да" или "Нет" с заглавной буквы: '))
    if c == "Да":
        print("Тогда немного сложнее:")
        print("В комнате четыре угла. В каждом углу сидит кошка.")
        print("Напротив каждой кошки по три кошки, на хвосте каждой кошки по одной кошки по одной кошке.")
        d = int(input("Сколько же кошек в комнате? "))
        if d < 4:
            print("Нет. Их больше - 4 штуки.")
        elif d > 4:
            print("А вот и нет, их всего 4.")
        else:
            print("Верно. Их 4")
    else:
        print("Ну, что ж. Тогда до встречи!")
else:
    print("Очень жаль! Тогда попробуем в другой раз.")