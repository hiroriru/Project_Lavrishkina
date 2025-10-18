'''
Найти и вывести на экран квадраты и кубы чисел от 2 до 5.
'''
number = 2

while number <= 5:
    kvadrat = number ** 2
    kub = number ** 3
    print(f"Квадрат числа {number}: {kvadrat}")
    print(f"Куб числа {number}: {kub}")

    number += 1
