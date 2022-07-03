import print_all_csv as pr_all_csv
import check_module as ch_md
import print_parent as pr_pa
import print_progress as pr_pr
import logger as log

def button_click():
    print('------------------------------------------')
    print('Добро пожаловать в информационную систему\nнашего небольшого детского сада!\nВведите число для получения информации:')
    mod = input('1 - Показать полный список воспитанников\n2 - Поиск воспитанника по фамилии\nВведите значение: ')
    mod = ch_md.check(mod, 2)
    print('------------------------------------------')
    id_kid = pr_all_csv.print_str('data_kids.csv', mod)

    info = input('1 - Показать информацию о родителях\n2 - Показать информацию по успеваемости\nВведите значение: ')
    info = ch_md.check(info, 2)

    if info == 1:
        pr_pa.find_parent('data_parent.csv', id_kid)
        log.request_contact_logger(id_kid, 4)
    elif info == 2:
        pr_pr.find_progress('data_progress.csv', id_kid)
        log.request_contact_logger(id_kid, 5)

    end = input('1. Повторить запрос.\n2. Закончить.\n')
    mod = ch_md.check(end, 2)
    end = int(end)
    if end == 1:
        button_click()
    else:
        print('Спасибо, что воспользовались нашей системой!')