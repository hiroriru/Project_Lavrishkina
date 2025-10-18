'''
Ввести N чисел. Посчитать и вывести количество чисел равных нулю.
'''
try:
    n = int(input("Введите количество чисел: "))

    print(f"Введите {n} чисел:")

    count_zero = 0
    i = 1

    while i <= n:
        number = float(input(f"Число {i}: "))
        if number == 0:
            count_zero = count_zero + 1
        i = i + 1

    print(f"Количество чисел равных нулю: {count_zero}")

except:
    print("Ошибка! Введите корректные данные!")

