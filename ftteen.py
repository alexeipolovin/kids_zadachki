import random


def Angar():
    main_tuple = (
        random.randint(0, 1200000), random.randint(0, 1200000), random.randint(0, 1200000), random.randint(0, 1200000))
    global error_value
    global error_index
    for i in range(0, len(main_tuple)):
        print("Индекс:" + str(i))
        print(main_tuple[i])
        s = input("Верно? Y/N")
        if s.upper() == "N":
            m = input("Введите нужное число:")
            error_index = i
            error_value = int(m)
            break
    new_arr = []
    for i in range(0, len(main_tuple)):
        if i == error_index:
            new_arr.append(error_value)
        else:
            new_arr.append(main_tuple[i])
    print(new_arr)
