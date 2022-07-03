from datetime import datetime as dt

def request_contact_logger(data, index):
    time = dt.now().strftime('%H:%M')
    
    if index == 1: # Вывод полного списка воспитанников
        with open('log_seminar_8.csv', 'a') as file:
            file.write('{};Show the list of pupils;\n'
                        .format(time))
    
    elif index == 2: # Поиск по фамилии воспитанника
        with open('log_seminar_8.csv', 'a') as file:
            file.write('{};Search by pupil last name;{}\n'
                        .format(time, data))

    elif index == 3: # Выбор воспитанника
        with open('log_seminar_8.csv', 'a') as file:
            file.write('{};Pupils choice;{}\n'
                        .format(time, data))

    elif index == 4: # Вывод родителей воспитанника
        with open('log_seminar_8.csv', 'a') as file:
            file.write('{};Print of the pupils parents;{}\n'
                        .format(time, data))

    elif index == 5: # Вывод успеваемости воспитанника
        with open('log_seminar_8.csv', 'a') as file:
            file.write('{};Print Students progress;{}\n'
                        .format(time, data))