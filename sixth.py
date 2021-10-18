import random


class MyFunnyList:
    main_list = []

    def __init__(self, main_list):
        self.main_list = main_list

    def add_elem(self, element):
        self.main_list.append(element)

    def remove_element(self, remove_element):
        self.main_list.remove(remove_element)

    def proc_main(self):
        chet = 0
        nechet = 0
        for i in self.main_list:
            if i % 2 == 0:
                chet += 1
            else:
                nechet += 1
        if chet > nechet:
            filename = input("Enter filename:")
            file = open(filename, 'r')
            print(file.read())
        else:
            filename = input("Enter filename:")
            print(filename.split('.')[-1])

    def feel_rand(self, how_much):
        for i in range(0, how_much):
            self.main_list.append(random.randint(0, how_much))
