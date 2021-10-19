class Student:
    fav_food = -1
    is_hungry = True
    is_food_given = False

    def give_food(self, value):
        if value == self.fav_food:
            self.is_food_given = True
            self.is_hungry = False
        else:
            self.is_food_given = False
            print("Студент голодный")


class FirstStudent(Student):
    fav_food = 0
    is_hungry = True
    is_food_given = False

    def __init__(self):
        pass


class SecondStudent(Student):
    fav_food = 1
    is_hungry = True
    is_food_given = False

    def __init__(self):
        pass


class ThirdStudent(Student):
    fav_food = 2
    is_hungry = True
    is_food_given = False

    def __init__(self):
        pass


class Cafe:
    food_costs: list = []
    stud_array: list = []

    def __init__(self, meet_costs, sal_costs):
        self.first_student: FirstStudent = FirstStudent()
        self.second_student: SecondStudent = SecondStudent()
        self.third_student: ThirdStudent = ThirdStudent()
        self.stud_array.append(self.first_student)
        self.stud_array.append(self.second_student)
        self.stud_array.append(self.third_student)
        self.meet_costs = meet_costs
        self.sal_costs = sal_costs
        self.fish_costs = meet_costs - meet_costs * 0.2
        self.food_costs.append(self.meet_costs)
        self.food_costs.append(self.sal_costs)
        self.food_costs.append(self.fish_costs)
        self.start_cycle()

    def start_cycle(self):
        not_hungry = 0
        for i in self.stud_array:
            if i.is_hungry:
                i.give_food(i.fav_food)
            else:
                not_hungry += 1
        if not_hungry == 3:
            print("Общая цена:" + str(self.meet_costs + self.fish_costs + self.sal_costs))
