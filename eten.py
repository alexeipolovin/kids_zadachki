class Rocket:
    weight = 0
    speed = 0
    size = 0

    def __init__(self):
        self.weight = int(input("Вес:"))
        self.speed = int(input("Скорость:"))
        self.size = int(input("Размер:"))


def proc_func():
    f_rocket = Rocket()
    s_rocket = Rocket()
    t_rocket = Rocket()
    ff_rocket = Rocket()
    fif_rocket = Rocket()

    main_list = [f_rocket, s_rocket, t_rocket, ff_rocket, fif_rocket]

    for i in main_list:
        for j in main_list:
            if i.weight - j.weight == 100 or i.speed/j.speed * 100 == 14 and i.size/j.size*100 == 44:
                print("Ракеты была найдена, это ракета под номером:" + str(main_list.index(i)))

