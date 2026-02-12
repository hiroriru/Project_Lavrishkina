"""
Средствами языка Python сформировать текстовый файл (.txt), содержащий
последовательность из целых положительных и отрицательных чисел. Сформировать
новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
обработку элементов:
Исходные данные:
Количество элементов:
Произведение элементов:
Повторяющиеся элементы:
Количество повторяющихся элементов:
Элементы больше 5 увеличены в два раза:
"""

l = ["-12 3 57 -8 3 53 -2 23"]
f1 = open("data_1.txt", "w")
f1.writelines(l)
f1.close()

f2 = open("data_2.txt", "w")

f2.write("Исходные данные:")
f2.write("\n")
f2.writelines(l)
f2.write("\n")

f1 = open("data_1.txt")
k = f1.read()
k = k.split()
for i in range(len(k)):
    k[i] = int(k[i])
f1.close()

kolichestvo = len(k)
f2.write("Количество элементов:\n")
f2.write(str(kolichestvo) + "\n")

t = 1
for i in range(len(k)):
    t = t * k[i]

f2.write("Произведение элементов:\n")
f2.write(str(t) + "\n")

povtor = []
for i in range(len(k)):
    skolko_raz = 0
    for j in range(len(k)):
        if k[i] == k[j]:
            skolko_raz = skolko_raz + 1
    if skolko_raz > 1:
        if k[i] not in povtor:
            povtor.append(k[i])

f2.write("Повторяющиеся элементы:\n")
if len(povtor) == 0:
    f2.write("Нет\n")
else:
    for i in range(len(povtor)):
        f2.write(str(povtor[i]) + " ")
    f2.write("\n")

f2.write("Количество повторяющихся элементов:\n")
f2.write(str(len(povtor)) + "\n") 

el = []
for i in range(len(k)):
    if k[i] > 5:
        el.append(k[i] * 2)
    else:
        el.append(k[i])

f2.write("Элементы больше 5 увеличены в два раза:\n")
for i in range(len(el)):
    f2.write(str(el[i]) + " ")
f2.write("\n")

f2.close()
