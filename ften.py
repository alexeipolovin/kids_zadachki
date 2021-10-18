class Worker:
    experience = 3
    salary = 12500
    education = 1

    summ = 0

    def __init__(self, experience, salary, education):
        self.experience = experience
        self.salary = salary
        self.education = education

        self.summ = self.experience + self.salary/10000 + self.education


def Factorio():
    worker1 = Worker(1, 12800, 1)
    worker2 = Worker(2, 15000, 3)
    worker3 = Worker(5, 11000, 2)

    m_list = [worker1, worker2, worker3]

    for i in m_list:
        if i.education == 1:
            print("Сотрудник " + str(m_list.index(i)) + " направлен на предприятие столярной обработки")
        elif i.education == 2:
            print("Сотрудник " + str(m_list.index(i)) + " направлен на предприятие бухгалтерии")
        elif i.education == 3:
            print("Сотрудник " + str(m_list.index(i)) + " направлен на предприятие сварочного цеха")
    m_list.sort(key=lambda x: x.summ, reverse=True)
    print("Самым выгодным является работник с суммарным кол-вом очков:" + str(m_list[-1].summ))
