def get_contact(index):
    if index == 1:
        contact = (input('Введите искомую фамилию или её часть латиницей: '))
        return contact
    elif index == 2:
        surname = (input('Введите фамилию: '))
        name = (input('Введите имя: '))
        telephone = (input('Введите телефон в формате 123-45-67: '))
        description = (input('Введите описание: '))
        contact = (surname, name, telephone, description)
        return contact
