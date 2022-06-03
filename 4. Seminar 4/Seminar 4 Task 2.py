# Задача 2. Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

print()
print('---------------- Семинар 4 -----------------')
def Simple (x):
    dividerList = []
    while x != 1:
        divider = 2
        while True:
                if (x % divider) == 0:
                    dividerList.append(divider)
                    x /= divider
                    break
                else:
                    divider += 1
    print(dividerList)

n = int(input('Введите число N: '))
Simple(n)       
print('------------------ Конец -------------------')
print()