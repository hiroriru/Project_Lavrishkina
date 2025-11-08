'''
Описать функцию InvertDigits(K), меняющую порядок следования цифр целого 
положительного числа K на обратный (K — параметр целого типа, являющийся 
одновременно входным и выходным). С помощью этой функции поменять порядок 
следования цифр на обратный для каждого из пяти данных целых чисел. 
'''
def InvertDigits(K):
    inverted = 0
    temp = K
    
    while temp > 0:
        inverted = inverted * 10 + temp % 10
        temp //= 10
    
    print(f"{K} -> {inverted}")
    return inverted

print("Введите 5 целых положительных чисел:")
numbers = []

i = 0
while i < 5:
    try:
        num = int(input(f"Число {i+1}: "))
        if num > 0:
            numbers.append(num)
            i += 1
        else:
            print("Число должно быть положительным!")
    except ValueError:
        print("Ошибка ввода!")

print("Обратный порядок цифр:")

j = 0
while j < len(numbers):
    InvertDigits(numbers[j])
    j += 1
