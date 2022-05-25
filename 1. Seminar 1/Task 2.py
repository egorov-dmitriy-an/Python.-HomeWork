# Задача 2.	Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат..,

print()
print('---------------- Семинар 1 -----------------')

truth_table = [
    [False, False, False],
    [False, False, True],
    [False, True, False],
    [False, True, True],
    [True, False, False],
    [True, False, True],
    [True, True, False],
    [True, True, True]
]
result = False
for i in truth_table:
    if (not (i[0] or i[1] or i[2])) == (not i[0] and not i[1] and not i[2]):
        result = True
if result == True:
    print('Утверждение истинно!')
else:
    print('Утверждение ложно!')
print('------------------ Конец -------------------')
print()