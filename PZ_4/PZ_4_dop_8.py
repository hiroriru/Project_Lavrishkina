'''
Даны два целых числа А и В (А < В). Найти сумму всех целых чисел от А до В
включительно (использовать оператор цикла).
'''
while True:
    try:
        A = int(input("Введите первое целое число: "))
        B = int(input("Введите второе целое число: "))
        if A >= B:
            print("Первое число должно быть меньше второго  числа! Попробуйте снова.")
            continue
        break
    except ValueError:
        print("Введите целые числа!")
summ = 0
current = A

while current <= B:
    summ = summ + current
    current = current + 1
print(f"Сумма чисел от {A} до {B} равна {summ}.")
