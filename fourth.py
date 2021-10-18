import os
from os import walk
from os.path import getsize
from os.path import getctime


def fourth_walk():
    f = []
    for (dirpath, dirnames, filenames) in walk('./'):
        f.extend(filenames)
        break

    print(sorted(f))

    size_list = []
    for i in f:
        size_list.append(getsize(i))
    for j in range(0, len(f)):
        print(str(j) + '.' + str(f))
    creation_time_list = []
    for i in f:
        creation_time_list.append(getctime(i))

    choose_your_detiny = int(input("Сравнить или отсортировать? 1, 2:"))
    if choose_your_detiny == 1:
        first_file = input("file name:")
        second_file = input("file name:")

        f_open = open(first_file, 'r')
        s_open = open(second_file, 'r')
        if f_open.read() == s_open.read():
            print("Они одиннаковые")
        else:
            print("Отличаются")
    elif choose_your_detiny == 2:
        choose_param = int(input("Размер, Дата? 1, 2:"))
        if choose_param == 2:
            search_dir = "./"
            os.chdir(search_dir)
            files = filter(os.path.isfile, os.listdir(search_dir))
            files = [os.path.join(search_dir, f) for f in files]
            files.sort(key=lambda x: os.path.getmtime(x))
            print(files)
        else:

            filepaths = []
            for basename in os.listdir('./'):
                filename = os.path.join('./', basename)
                if os.path.isfile(filename):
                    filepaths.append(filename)

            for i in range(len(filepaths)):
                filepaths[i] = (filepaths[i], os.path.getsize(filepaths[i]))

            filepaths.sort(key=lambda filename: filename[1], reverse=False)
            for i in range(len(filepaths)):
                filepaths[i] = filepaths[i][0]
            print(filepaths)
