def calc(is_rain):
    speed = 64
    a = 12
    another_a = 0
    if is_rain:
        another_a = 2
    else:
        another_a = 5
    speed = speed + a + another_a

    print(1200/speed)
