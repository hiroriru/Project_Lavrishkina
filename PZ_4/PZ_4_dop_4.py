'''
Найти и вывести на экран S=1!+2!+3!+4!+…+n! (n>1).
'''
while True:
    try:
        n = int(input("Введите число n (n > 1): "))
        if n <= 1:
            print("n должно быть больше 1!")
            continue
        break
    except:
        print("Ошибка! Введите целое число!")

S = 0
i = 1

while i <= n:
    fact = 1
    j = 1
    while j <= i:
        fact = fact * j
        j = j + 1

    print(f"{i}! = {fact}")
    S = S + fact
    i += 1

print(f"\nS = {S}")