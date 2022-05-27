#Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

print()
print('---------------- Семинар 3 -----------------')
import random
n = int(input ('Введите количество чисел в списке n: '))
coll =[]
for i in range(0, n):
    t = random.randint(0, 9)
    coll.append(t)
print(coll)
multi = []
i =0
index = n-1
multiplication = 1
while i <= index :
        multiplication = coll[i] * coll[index]
        multi.append(multiplication)
        index -=1
        i+=1
print(f'Произведение пар чисел списка равно: {multi}')
print('------------------ Конец -------------------')
print()