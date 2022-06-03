# Задача 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

x = open('Seminar_4_Task_4_Polynom_1.txt', 'r')
polynom_1 = x.readline()
x.close()

x = open('Seminar_4_Task_4_Polynom_2.txt', 'r')
polynom_2 = x.readline()
x.close()

def Poly_List(polynom):
    coefList = []
    numb = ''
    i = 0
    while True:
        s = str(polynom[i])
        if polynom[i] == '^':
            while str(polynom[i+1]).isdigit() == True:
                polynom = polynom[:i+1] + polynom[i+2:]
        if polynom[i] == '=':
            break
        if s.isdigit() == True:
            numb += s
        elif len(numb) != 0:
            coefList.append(int(numb))
            numb = ''
        i += 1
    return(coefList)

coef_1 = Poly_List(polynom_1)
coef_2 = Poly_List(polynom_2)

delta = len(coef_1) - len(coef_2)
if delta <= 0:
    count = len(coef_1)
    index = len(coef_2)
    result = coef_2
else:
    count = len(coef_2)
    index = len(coef_1)
    result = coef_1

for i in range(0, count):
    differ = index - i - 1
    if delta <= 0:
        result[differ] = result[differ] + coef_1[differ + delta]
    else:
        result[differ] = result[differ] + coef_2[differ - delta]

poly = ''
for i in range(0, index):
    if i == index - 1:
        poly = poly + str(result[i]) + ' = 0'
    elif i == index-2:
        poly = poly + str(result[i]) + 'x' + ' + '
    elif i <= index-2:
        poly = poly + str(result[i]) + 'x^' + str(index - i - 1) + ' + '

f = open('Seminar_4_Task_5_Polynom.txt', 'w+')
f.write(poly)
f.close()