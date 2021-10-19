import re


class CustomException(Exception):
    pass


def get_string(main_str: str, what_to_do: str):
    sec_str: list = list(main_str)
    sec_arr: list = []
    for i in sec_str:
        # print(i)
        if str.isdigit(i):
            sec_arr.append(int(i))
    res = 0
    for i in sec_arr:
        for j in range(i + 1, len(sec_arr)):
            if i == j:
                # print(i, j)
                raise CustomException("Два одиннаковых числа")
    if len(sec_arr) > 0:
        if what_to_do == '+':
            for i in sec_arr:
                res += i
        elif what_to_do == '-':
            for i in sec_arr:
                res -= i
        elif what_to_do == '/':
            for i in sec_arr:
                try:
                    res /= i
                except ZeroDivisionError:
                    print("Деление на ноль")
        elif what_to_do == '*':
            for i in sec_arr:
                res *= i
    return res
