class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_road(self):
        self_mass = 25
        thick_road = 0.05
        mass = self._width * self._length * self_mass * thick_road / 1000
        print(f'Масса асфальта: {mass}т.')
        # Результат отличается от результата из задачи т.к. сантиметр толщины полотна переведен в метр


track = Road(5000, 20)
track.mass_road()
