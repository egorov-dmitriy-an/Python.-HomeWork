# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Предложить улучшения кода для решённых задач

x = open('Seminar_6_Task_4_Text.txt', 'r')
text = x.readline()
x.close()

def Find(old_text):
    count = 1
    new_text = ''
    leng = len(old_text)
    for i in range(0, leng):
        if i == (leng - 1):
            if count == 1:
                new_text += old_text[i]
            else:
                new_text += str(count) + old_text[i]
            break
        
        if old_text[i+1] == old_text[i]:
            count += 1
        else:
            if count == 1:
                new_text += old_text[i]
            else:
                new_text += str(count) + old_text[i]
                count = 1
    return new_text

f = open('Seminar_6_Task_4_RLE.txt', 'w+')
f.write(Find(text))
f.close()

x = open('Seminar_6_Task_4_RLE.txt', 'r')
rle_text = x.readline()
x.close()

revers_text = ''
index = ''
len = len(rle_text)

# --------------------------------------------
# Исходный фрагмент кода:
# for i in range(0, len):
#     if rle_text[i].isdigit() == True:
#         index += rle_text[i]
#     else:
#         if index == '':
#             revers_text += rle_text[i]
#         else:
#             t = rle_text[i]
#             for j in range(0, int(index)):
#                 revers_text += t    
#             index = ''

# --------------------------------------------
# Создадим список с указанием цифра или нет с использованием lambda, map
text_2 = list(map(lambda x: x.isdigit(), rle_text)) 
for i in range(0, len):
    if text_2[i]:
        index += rle_text[i]
    else:
        if index == '':
            revers_text += rle_text[i]
        else:
            t = rle_text[i]
            for j in range(0, int(index)):
                revers_text += t
            index = ''
# -------------------------------------------

f = open('Seminar_6_Task_4_Revers.txt', 'w+')
f.write(revers_text)
f.close()