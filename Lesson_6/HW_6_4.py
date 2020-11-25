class Car:

    def __init__(self, name, speed, color, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'{self.name} в движении.'

    def stop(self):
        return f'{self.name} остановилась.'

    def turn(self, direction):
        return f'Машина поворачивает {direction}.'

    def show_speed(self):
        return f'Скорость машины {self.speed}.'

    def police_car(self):
        if self.is_police:
            return f'{self.name} - это машина полицейского департамента'
        else:
            return f'{self.name} - это гражданский автомобиль'


class PoliceCar(Car):
    pass


class SportCar(Car):
    pass


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            return f'Ваша скорость {self.speed}. Скорость выше допустимой (60 км/ч). Необходимо снизить скорость'
        else:
            return f'Скорость в пределах нормы'


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            return f'Ваша скорость {self.speed}. Скорость выше допустимой (40 км/ч). Необходимо снизить скорость'
        else:
            return f'Скорость в пределах нормы'


town = TownCar('Mersedens', 100, 'Белая', False)
print(town.go(), town.show_speed(), town.turn('налево'), town.turn('потом направо'), town.police_car())

work = WorkCar('Lada Granda', 30, 'Белая', True)
print(work.go(), work.show_speed(), work.turn('направо'), work.stop(), work.police_car())

police = PoliceCar("Ford Mustang", 70, "Темно-синяя", True)
print(police.go(), police.show_speed(), police.turn('направо'), police.police_car())

sport = SportCar('Ferrari', 170, 'Красная', False)
print(sport.go(), sport.show_speed(), sport.turn('налево'), sport.stop(), sport.police_car())
