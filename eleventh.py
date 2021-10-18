from random import randint


class Plane:
    time_to_land = randint(0, 50)
    is_extreme_landing = False
    is_landing = False
    is_landed = False

    def __init__(self, is_landing, is_extreme_landing=False):
        self.is_landing = is_landing
        if not is_landing:
            print("Самолёт взлетает")
        else:
            print("Самолёт садится")

    def proc_extreme(self):
        if randint(0, 12000) % 10 == 0:
            self.is_extreme_landing = True


class Airport:
    plane_list = []

    def __init__(self):
        first_plane = Plane(False)
        second_plane = Plane(False)
        third_plane = Plane(False)
        fourth_plane = Plane(False, is_extreme_landing=True)
        fifth_plane = Plane(True)
        sixth_plane = Plane(True)
        seventh_plane = Plane(True)
        eighth_plane = Plane(True)

        self.plane_list.append(first_plane)
        self.plane_list.append(second_plane)
        self.plane_list.append(third_plane)
        self.plane_list.append(fourth_plane)
        self.plane_list.append(fifth_plane)
        self.plane_list.append(sixth_plane)
        self.plane_list.append(seventh_plane)
        self.plane_list.append(eighth_plane)

    def proc_func(self):
        for i in self.plane_list:
            i.is_landed = True
            if i.is_landing:
                print("Самолёт сел")
            else:
                print("Самолёт взлетел")

    def sort_planes(self):
        self.plane_list.sort(key=lambda x: x.time_to_land, reverse=True)
        for i in self.plane_list:
            if i.is_extreme_landing:
                self.plane_list.remove(i)
                self.plane_list.insert(0, i)
                for j in self.plane_list:
                    if not j.is_extreme_landing:
                        j.time_to_land += 30
