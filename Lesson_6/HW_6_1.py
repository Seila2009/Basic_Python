import time


class TrafficLight:
    __color = ["Красный", "Желтый", "Зелёный"]

    def running(self):
        a = 0
        while a < 3:
            print(TrafficLight.__color[a])
            if a == 0:
                time.sleep(7)
            elif a == 1:
                time.sleep(2)
            elif a == 1:
                time.sleep(10)
            a += 1


traffic = TrafficLight()
traffic.running()