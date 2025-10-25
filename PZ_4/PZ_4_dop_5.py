'''
Ввести N чисел. Найти и вывести их среднее арифметическое.
'''
try:
    N = int(input("Введите количество чисел: "))

    print(f"Введите {N} чисел:")

    summa = 0
    i = 1

    while i <= N:
        number = float(input(f"Число {i}: "))
        summa = summa + number
        i = i + 1

    eee = summa / N

    print(f"Сумма: {summa}")
    print(f"Среднее арифметическое: {eee}")
except ValueError:
    print("Введите целое число.")
