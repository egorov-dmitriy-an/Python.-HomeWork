# Задача 1. Вычислить число пи, (использовать формулу Нилаканта
# или что лучше) c заданной точностью d.

print()
print('---------------- Семинар 4 -----------------')
def Pi(x):
    mod = 1
    result = 3
    n = 2
    while True:
        temp = round(result, x)
        result += mod * 4/(n*(n+1)*(n+2))
        if round(result, x) == temp:
            print(f'Число пи с точностью до { x} знака равно {round(result, x)}')
            break
        else:
            mod *= -1
            n += 2

d = int(input('Введите необходимую точность: '))
Pi(d)
print('------------------ Конец -------------------')
print()