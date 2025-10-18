'''
Дано целое число N (>0). Используя операции деления нацело и взятия остатка от
деления, вывести все его цифры, начиная с самой правой (разряда единиц).
'''
while True:
    try:
        N = int(input("Введите целое число: "))
        if N <= 0:
            print("Ошибка. Число должно быть положительное.")
            continue
        break
    except ValueError:
        print("Введите целые числа!")

temp = N

while temp > 0:
    last_digit = temp % 10
    print(last_digit)
    temp = temp // 10