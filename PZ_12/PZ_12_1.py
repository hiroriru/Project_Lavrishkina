'''
В матрице элементы первого столбца возвести в куб.
'''
import random

matrix = [[random.randint(0, 20) for j in range(5)] for i in range(5)]

print("Исходная матрица:")
for i in matrix:
    print(i)

for i in range(len(matrix)):
    matrix[i][0] = matrix[i][0] ** 3

print("\nМатрица после возведения первого столбца в куб:")
for i in matrix:
    print(i)
