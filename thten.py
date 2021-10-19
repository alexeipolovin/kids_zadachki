import random


class Flower:
    type = 0
    weather = 0
    water_needs = 0

    def __init__(self, type):
        self.weather = random.randint(0, 2)
        self.type = type
        if self.type != 0:
            self.water_needs = self.weather * self.type
        else:
            print("Не выбран тип")
        self.start_life_cycle()

    def start_life_cycle(self):
        while True:
            if random.randint(0, 4) % 2 != 0:
                print("Погода сменилась")
                self.weather += 1
                self.water_needs = self.weather + self.type
            s = input("Полить цветок? Требуется " + str(self.water_needs) + " воды Y/N: ")
            if s.upper() == "N":
                break
            if random.randint(0, 120921875192) % 10 == 0:
                print("Цветок полит достаточно")
                break
