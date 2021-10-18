def calc(start_lock, start_speed):
    if start_lock > 1200:
        print("Уже достаточно близко")
    else:
        print(((1200 - start_lock)/start_speed+2))

