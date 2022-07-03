def check(sensor, limit):
    while True:
        while sensor.isdecimal() == False:
            sensor = input(f'Введите ЧИСЛО от 1 до {limit}: ')
        sensor = int(sensor)
        if 1 <= sensor <= limit:
            break
        else:
            sensor = input(f'Введите число ОТ 1 ДО {limit}: ')
    return sensor