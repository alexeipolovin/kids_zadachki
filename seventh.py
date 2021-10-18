import math


def calc_bolt():
    g = 9.8
    a = 2.2
    v = 2.4
    h = 2.5
    t = math.sqrt((2 * h) / (g + a))
    s = v * t - (g * t * t) / 2
    print(s)
