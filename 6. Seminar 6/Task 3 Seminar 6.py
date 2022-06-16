# Задача 3. Создайте программу для игры в "Крестики-нолики". Предложить улучшения кода для решённых задач
print()
print('--------------------- Семинар 6 ----------------------')

# Исходный фрагмент кода:
# tic_tac_toe = [ '1', '2', '3', '4', '5', '6', '7', '8', '9'] 

# Заменим создание списка с помощью list comprehension
tic_tac_toe = [str(n) for n in range(1, 10)]

def Victory(tab):
    if tab[0] == tab[1] and tab[1] == tab[2]:
        return True
    elif tab[3] == tab[4] and tab[4] == tab[5]:
        return True
    elif tab[6] == tab[7] and tab[7] == tab[8]:
        return True
    elif tab[0] == tab[3] and tab[3] == tab[6]:
        return True
    elif tab[1] == tab[4] and tab[4] == tab[7]:
        return True
    elif tab[2] == tab[5] and tab[5] == tab[8]:
        return True
    elif tab[0] == tab[4] and tab[4] == tab[8]:
        return True
    elif tab[2] == tab[4] and tab[4] == tab[6]:
        return True
    else:
        return False

def Print_list(a):
    for i in range(0, len(a), 3):
        print(a[i:i+3])

Print_list(tic_tac_toe)
mod = 1
while True:
    if mod % 2 != 0:
        print('Ход первого игрока')
        index = int(input(f'Введите номер поля, в который нужно поставить крестик: '))
        tic_tac_toe[index - 1] = 'X'
        Print_list(tic_tac_toe)
        mod += 1
    else:
        print('Ход второго игрока')
        index = int(input(f'Введите номер поля, в который нужно поставить нолик: '))
        tic_tac_toe[index - 1] = 'O'
        Print_list(tic_tac_toe)
        mod += 1

    if Victory(tic_tac_toe) == True and mod % 2 == 0:
        print('Победил первый игрок')
        break
    elif Victory(tic_tac_toe) == True and mod % 2 != 0:
        print('Победил второй игрок')
        break
    elif mod > 9:
        print('Победила дружба')
        break
print('----------------------- Конец ------------------------')
print()
