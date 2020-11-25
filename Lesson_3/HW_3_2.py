def pers_data(name="", last_name="", year="", city="", email="", tel_num=""):
    return f"Привет, меня зовут - {name} {last_name}. Я родилась в {year} в городе {city}. " \
           f"Мои контактные данные: email - {email}, телефон - {tel_num}."

print(pers_data(name=input('Введите имя: '),
                last_name=input('Введите фамилию: '),
                year=input('Введите год рождения: '),
                city=input('Введите город рождения: '),
                email=input('Введите e-mail: '),
                tel_num=input('Введите номер телефона: ')))
