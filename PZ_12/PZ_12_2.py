'''
Сгенерировать матрицу, в которой элементы больше 10 заменяются на 0.
'''
import random

n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))

matrix = [[random.randint(0, 20) for i in range(n)] for i in range(m)]

print("Исходная матрица:")
for row in matrix:
    print(row)

matrix = [[0 if elem > 10 else elem for elem in row] for row in matrix]

print("\nИзменённая матрица:")
for row in matrix:
    print(row)

