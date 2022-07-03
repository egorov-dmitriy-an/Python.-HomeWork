def check(sensor, list_number):
    while True:
        while sensor.isdecimal() == False:
            sensor = input(f'Введите ЧИСЛО: ')
        sensor = int(sensor)
        if sensor in list_number:
            break
        else:
            sensor = input(f'Введите число из {list_number}: ')
    return sensor