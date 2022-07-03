import csv
import check_module as ch_md
import check_module_list as ch_md_ls
import find_surname as fi_su
import logger as log

def print_str(file_temp, sensor):
    with open(file_temp, encoding='UTF-8') as r_file:
        file = list(csv.reader(r_file, delimiter=','))
        count = 0
        if sensor == 1:
            print('Список всех воспитанников: ')
            for row in file:
                print(row[1], '\t', row[2], '\t', row[3])
                count += 1
            log.request_contact_logger(0, 1)
            print('-----------------------------------------')
        else:
            while True:
                surname = input('Введите искомую фамилию воспитанника: ')
                log.request_contact_logger(surname, 2)
                print('Найденные совпадения: ')
                li = []
                count = 0
                for row in file:
                    if fi_su.find_text(surname, row) == True:
                        print(row[1], '\t', row[2], '\t', row[3])
                        lim = int(row[1])
                        li.append(lim)
                    
                if len(li) != 0:
                    break
                else:
                    print('Воспитанника с такой фамилией нет!')

        index = input('Введите номер воспитанника: ')
        if sensor == 1:
            ch_md.check(index, count-1)
            index = int(index)
        else:
            ch_md_ls.check(index, li)
            index = int(index)
        id_kid_print = file[index][0]
        print(f'Искомый воспитанник: {file[index][2]} {file[index][3]}')
        log.request_contact_logger(file[index][2], 3)
        print('------------------------------------------')
    return id_kid_print