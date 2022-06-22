import logger as log
import data_provider as dt
import check_module as ch
import checking_file as chfl
import add_contact as ad_con
import check_print as ch_pr

def button_click():
    print()
    number = (input('Для поиска контакта нажмите 1, для добавления нажмите 2: '))
    number = ch.check(number)

    contact = dt.get_contact(number)

    log.request_contact_logger(contact, number)

    if number == 1:
        contact_list = chfl.check_file('guide.txt', contact)
        if len(contact_list) == 0:
            print('Такого контакта нет')
        else:
            mod = (input('В каком формате вывести данные: 1 - столбец, 2 - строка: '))
            mod = ch_pr.check(mod)
            
            print()
            print('Искомый контакт:')
            if mod == 1:
                for i in range(0, len(contact_list)):
                    temp = contact_list[i].split(';')
                    for j in range(0, 4):
                        print(temp[j])
                print()
            else:
                for i in range(0, len(contact_list)):
                    temp = contact_list[i].split(';')
                    for j in range(0, 4):
                        if j != 3:
                            print(temp[j], end = ', ')
                        else:
                            print(temp[j])
                print()
    elif number == 2:
        ad_con.save_contact('guide.txt', contact)