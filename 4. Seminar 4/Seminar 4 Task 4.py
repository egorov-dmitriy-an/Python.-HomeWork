# Задача 4. Задана натуральная степень n.
# Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени
# пример записи в файл при n=3 ==> 33x^3 + 8x^2 + 64x + 85 = 0 при n=2 ==> 27x^2 + 95x + 79 = 0

import random
def PolyFill(n):
    coefList = []
    for i in range(0, n+1):
        temp = str(random.randint(0, 100))
        coefList.append(temp)
    
    polynom = ''
    for i in range(0, n+1):
        if i == n:
            polynom = polynom + coefList[i] + ' = 0'
        elif i == n-1:
            polynom = polynom + coefList[i] + 'x' + ' + '
        elif i <= n-1:
            polynom = polynom + coefList[i] + 'x^' + str(n - i) + ' + '
    return(polynom)

n_1 = int(input('Введите натуральное значение степени для первого многочлена: '))
n_2 = int(input('Введите натуральное значение степени для второго многочлена: '))

f = open('Seminar_4_Task_4_Polynom_1.txt', 'w+')
f.write(PolyFill(n_1))
f.close()

f = open('Seminar_4_Task_4_Polynom_2.txt', 'w+')
f.write(PolyFill(n_2))
f.close()