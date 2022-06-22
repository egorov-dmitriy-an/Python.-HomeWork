def check(sensor):
    while True:
        while sensor.isdecimal() == False:
            sensor = input('Для вывода в столбец нажмите 1, для для вывода в строку нажмите 2: ')
        if 1 <= int(sensor) <= 2:
            break
        else:
            sensor = input('Для вывода в столбец нажмите 1, для для вывода в строку нажмите 2: ')
    return int(sensor)