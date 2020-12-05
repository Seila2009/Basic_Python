class Technics:
    def __init__(self, name, year_of_manufacture, country, price, quantity, numb, *args):
        self.name = name
        self.year_of_manufacture = year_of_manufacture
        self.country = country
        self.price = price
        self.quantity = quantity
        self.numb = numb
        self.my_store_full = []
        self.my_store = []
        self.items = {'Наименнование производителя': name, 'Год выпуска': year_of_manufacture,
                      'Страна производитель': country, 'Цена за ед': price, 'Количество': quantity}

    def __str__(self):
        return f'{self.name}, Год выпуска: {self.year_of_manufacture}, Страна производитель: {self.country}, ' \
               f'Цена {self.price} Количество {self.quantity} '

    def receiving(self):
        try:
            name = str(input(f'Введите производителя: '))
            year_of_manufacture = int(input(f'Введите год выпуска: '))
            country = str(input(f'Введите страну производителя: '))
            price = int(input(f'Введите цену: '))
            quantity = int(input(f'Введите количество: '))
            unique = {'Наименнование производителя': name, 'Год выпуска': year_of_manufacture,
                      'Страна производитель': country, 'Цена за ед': price, 'Количество': quantity}
            self.items.update(unique)
            self.my_store.append(self.items)
            print(f'Текущий список - {self.items}')
        except ValueError:
            return f'Недопустимое значение!'

        print(f'Для продолжения - Y, для выхода - Enter')
        y = input(f'---> ').lower()
        if y == 'y':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад - {self.my_store_full}')
            return f'Выход'
        else:
            return Technics.receiving(self)


class Printer(Technics):
    def to_print(self):
        return f'Номер принтера в списке {self.numb}'


class Scanner(Technics):
    def to_scan(self):
        return f'Номер сканера в сприске {self.numb}'


class Xerox(Technics):
    def to_xerox(self):
        return f'Номер ксерокса в списке {self.numb}'


tech_1 = Printer('Canon', 2018, 'Китай', 5499, 10, 1)
tech_2 = Scanner('Canon', 2015, 'Тайвань', 3699, 10, 2)
tech_3 = Xerox('Xerox', 1500, 'Япония', 1, 15, 3)

print(tech_1.receiving())
print(tech_2.receiving())
print(tech_3.receiving())
print(tech_1.to_print())
print(tech_3.to_copier())
