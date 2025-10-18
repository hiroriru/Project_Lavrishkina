'''
Даны два целых числа A и B (A < B). Найти сумму всех целых чисел от A до B
включительно.
'''
while True:
    try:
        A = int(input("Введите первое число: "))
        B = int(input("Введите второе число: "))
        if A >= B:
            print("Первое число должно быть меньше второго  числа! Попробуйте снова.")
            continue
        break
    except ValueError:
        print("Введите целые числа!")

total = 0
current = A

while current <= B:
    total = total + current
    current = current + 1

print(f"Сумма всех чисел от {A} до {B} включительно: {total}")