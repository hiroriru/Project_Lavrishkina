"""
Описать функцию InvertDigits(K), меняющую порядок следования цифр целого
положительного числа K на обратный (K — параметр целого типа, являющийся
одновременно входным и выходным). С помощью этой функции поменять порядок
следования цифр на обратный для каждого из пяти данных целых чисел.
"""
def InvertDigits(K):
    original = K
    inverted = 0

    while K > 0:
        inverted = inverted * 10 + K % 10
        K //= 10

    print(f"Обратное число от {original}: {inverted}")
    return inverted


print("Введите 5 целых положительных чисел:")

i = 0
while i < 5:
    try:
        num = int(input(f"Число {i+1}: "))
        if num > 0:
            InvertDigits(num)
            i += 1
        else:
            print("Число должно быть положительным!")
    except ValueError:
        print("Ошибка ввода! Введите целое число.")
