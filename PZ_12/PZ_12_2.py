'''
Сгенерировать матрицу, в которой элементы больше 10 заменяются на 0.
'''
import random

matrix = [[random.randint(0, 20) for i in range(5)] for i in range(5)]

print("Исходная матрица:")
for row in matrix:
    print(row)

matrix = [[0 if elem > 10 else elem for elem in row] for row in matrix]

print("\nИзменённая матрица:")
for row in matrix:
    print(row)
