class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = ({"name": name, "surname": surname})
        self.position = position
        self._income = ({"wage": int(wage), "bonus": int(bonus)})


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name["name"] + self.name["surname"]

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


staff_name = input('Введите имя сотрудника: ')
staff_surname = input('Введите фамилию сотрудника: ')
staff_position = input('Введите должность сотрудника: ')
staff_wage = input('Введите оклад сотрудника: ')
staff_bonus = input('Введите премию сотрудника: ')
human = Position(staff_name, staff_surname, staff_position, staff_wage, staff_bonus)
print(f'Сотрудник - {human.get_full_name()}. Общий доход сотрудника на позиции {staff_position} составляет {human.get_total_income()} рублей.')

