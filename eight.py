class Converter:

    def __init__(self, us_type, f_value, sec_value, us_coof=1, reverse=False):
        self.us_type = us_type
        self.us_coof = us_coof
        self.reverse = reverse
        self.f_value = f_value
        self.sec_value = sec_value
        self.check_conv()

    def check_conv(self):
        if self.us_type == 1:
            # кмч в мс
            self.kmtoms()
        elif self.us_type == 2:
            # минуты в секунды
            self.mintosec()
        elif self.us_type == 3:
            self.mintohour()
        elif self.us_type == 4:
            self.mintomon()
        elif self.us_type == 5:
            self.mintoyear()
        else:
            print("Неверный идентификатор")

    def kmtoms(self):
        if not self.reverse:
            print(self.f_value/3.6)
        else:
            print(self.f_value*3.6)

    def mintosec(self):
        if not self.reverse:
            print(self.f_value/60)
        else:
            print(self.f_value*60)

    def mintohour(self):
        if not self.reverse:
            print(self.f_value/60)
        else:
            print(self.f_value*60)

    def mintomon(self):
        if not self.reverse:
            print(self.f_value/43800)
        else:
            print(self.f_value*43800)

    def mintoyear(self):
        if not self.reverse:
            print(self.f_value/525600)
        else:
            print(self.f_value*525600)