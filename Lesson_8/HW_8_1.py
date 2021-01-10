from datetime import date


class Data:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def type(cls):
        try:
            day, month, year = [int(i) for i in data.split('-')]
            return f"{type(day), day}\n{type(month), month}\n{type(year), year}"
        except ValueError:
            return 'Указана неправильная дата!'

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2019 >= year >= 0:
                    return f'Все верно'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'


print(Data.valid(31, 11, 2022))
print(Data.valid(14, 13, 2015))
print(Data.valid(15, 12, 2020))