'''
Дано два числа.
Если их сумма кратна 5, то прибавить 1, иначе вычесть 2.
'''
try:
    num_1 = float(input("Введите первое число: "))
    num_2 = float(input("Введите второе число: "))

    summ = num_1 + num_2

    if summ % 5 == 0:
        op_1 = summ + 1
        print(op_1)
    else:
        op_2 = summ - 2
        print(op_2)

except ValueError:
    print("Ошибка. Пожалуйста, введите число.")