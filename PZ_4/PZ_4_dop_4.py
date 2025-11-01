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
fact = 1
i = 1

while i <= n:
    fact = fact * i
    print(f"{i}! = {fact}")
    S = S + fact
    i = i + 1

print(f"S = {S}")