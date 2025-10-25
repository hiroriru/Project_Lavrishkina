'''
 Вывести первые N (N≥3) чисел Фибоначчи и посчитать количество четных чисел
'''
while True:
    try:
        N = int(input("Введите количество чисел Фибоначчи (N ≥ 3): "))
        if N < 3:
            print("N должно быть не меньше 3!")
            continue
        break
    except ValueError:
        print("Введите целое число!")

num_1 = 0
num_2 = 1
even_count = 0
count = 2

print(f"Первые {N} чисел Фибоначчи: {num_1} {num_2}", end= " ")

if num_1 % 2 == 0:
    even_count += 1
if num_2 % 2 == 0:
    even_count += 1

while count < N:
    fib_next = num_1 + num_2
    print(fib_next, end=" ")

    if fib_next % 2 == 0:
        even_count += 1

    num_1 = num_2
    num_2 = fib_next
    count += 1

print(f"Количество четных чисел: {even_count}")
