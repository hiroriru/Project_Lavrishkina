'''
В матрице элементы первого столбца возвести в куб.
'''
import random

n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))

matrix = [[ random.randint(0, 20) for j in range(n)] for i in range(m)]

print("Исходная матрица:")
for i in matrix:
    print(i)

matrix = list(map(lambda row: [row[0] ** 3] + row[1:], matrix))

print("\nМатрица после возведения первого столбца в куб:")
for i in matrix:
    print(i)

