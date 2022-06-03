#Задача 3. Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

print()
print('---------------- Семинар 4 -----------------')
import random

n = int(input('Введите количество элементов последовательности N: '))

oldList = []
newList =[]
for i in range(1, n+1):
    t = random.randint(0, 5)
    oldList.append(t)
print(f'Исходная последовательность - {oldList}')

temp = oldList [0]
newList.append(temp)

for i in oldList:
    mod = 1
    for j in newList:
        if i==j:
            mod = 0
    if mod == 1:
       newList.append(i)
    else:
        mod = 1
print(f'Новая последовательность - {newList}')
print('------------------ Конец -------------------')
print()