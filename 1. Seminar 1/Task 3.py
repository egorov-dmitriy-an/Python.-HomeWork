# Задача 3. Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка
# (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

print()
print('---------------- Семинар 1 -----------------')
while True:
    x = int(input('Введите координату X = '))
    y = int(input('Введите координату Y = '))
    if not (x == 0 and y == 0):
        break
    else:
        print('X и Y не могут быть равны 0 одновременно')

if x > 0 and y > 0:
    print(f'Точка [{x}, {y}] находится в четверти - 1')
elif x < 0 and y > 0:
    print(f'Точка [{x}, {y}] находится в четверти - 2')
elif x < 0 and y < 0:
    print(f'Точка [{x}, {y}] находится в четверти - 3')
elif x > 0 and y < 0:
    print(f'Точка [{x}, {y}] находится в четверти - 4')
elif x == 0:
    print(f'Точка [{x}, {y}] находится на оси Y')
elif y == 0:
    print(f'Точка [{x}, {y}] находится на оси X')
print('------------------ Конец -------------------')
print()
