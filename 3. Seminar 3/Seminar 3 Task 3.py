#Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#Пример:
#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

print()
print('---------------- Семинар 3 -----------------')
n = int(input('Введите количество чисел в списке N = '))
coll =[]
for i in range(0, n):
    temp = float(input(f'Введите число {i} = '))
    coll.append(temp)

print(coll, end =' => ')
new = []
point = 0
for i in coll:
    temp = i - int(i)
    if temp != 0 :
        new.append(temp)
    if str(i)[::-1].find('.') > point:
        point = str(i)[::-1].find('.')
max = abs(new[0])
min = abs(new[0])
for i in new:
    if abs(i) > max:
        max = abs(i)
    if abs(i) < min:
        min = abs(i)
print(round(max - min, point))
print('------------------ Конец -------------------')
print()