'''
Вести число. Если оно четное, разделить его на 4, если нечетное - умножить на 5. 
'''
try:
    num = float(input("Введите число: "))

    if num % 2 == 0:
        op_1 = num / 4
        print(op_1)
    elif num % 2 != 0:
        op_2 = num * 5
        print(op_2)
except ValueError:
    print("Ошибка.Введите число заново.")
