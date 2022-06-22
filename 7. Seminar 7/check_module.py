def check(sensor):
    while True:
        while sensor.isdecimal() == False:
            sensor = input('Для поиска контакта нажмите 1, для добавления нажмите 2: ')
        if 1 <= int(sensor) <= 2:
            break
        else:
            sensor = input('Для поиска контакта нажмите 1, для добавления нажмите 2: ')
    return int(sensor)