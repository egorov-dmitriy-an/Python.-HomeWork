# Задача 1. Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

print()
print('---------------- Семинар 1 -----------------')
n = input('Введите цифру, обозначающую день недели: ')
while True:
    while n.isdecimal() == False:
        n = input('Введите цифру от 1 до 7: ')
    
    if 0 < int(n) < 8:
        break
    else:
        n = input('Введите цифру от 1 до 7: ')

if int(n) == 6 or int(n) == 7:
    print('Введеный день - выходной!')
else:
    print('Введеный день - рабочий!')

print('------------------ Конец -------------------')
print()
