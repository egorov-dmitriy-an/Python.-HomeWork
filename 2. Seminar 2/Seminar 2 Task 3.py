# Задача 3. Реализуйте алгоритм перемешивания списка.
print()
print('---------------- Семинар 2 -----------------')
import random
n = int(input('Введите длину списка n = '))

coll = []
for i in range(0, n):
    coll.append(i)
print(f'Упорядоченный список: {coll}')

revers = []
while (n > 0):
    index = random.randint(0, n-1)
    revers.append(coll[index])
    del coll[index]
    n -= 1
    
print(f'Перемешанный список:  {revers}')
print('------------------ Конец -------------------')
print()