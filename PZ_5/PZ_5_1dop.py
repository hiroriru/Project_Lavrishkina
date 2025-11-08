def sum_of_digits(n):
    if n < 0:
        n = -n
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

def main():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    c = int(input("Введите третье число: "))

    sum_a = sum_of_digits(a)
    sum_b = sum_of_digits(b)
    sum_c = sum_of_digits(c)

    if sum_a > sum_b and sum_a > sum_c:
        print(f"У числа {a} наибольшая сумма цифр: {sum_a}")
    elif sum_b > sum_a and sum_b > sum_c:
        print(f"У числа {b} наибольшая сумма цифр: {sum_b}")
    elif sum_c > sum_a and sum_c > sum_b:
        print(f"У числа {c} наибольшая сумма цифр: {sum_c}")
    else:
        if sum_a == sum_b == sum_c:
            print(f"У всех трех чисел одинаковая сумма цифр: {sum_a}")
        elif sum_a == sum_b:
            print(f"У чисел {a} и {b} одинаковая наибольшая сумма цифр: {sum_a}")
        elif sum_a == sum_c:
            print(f"У чисел {a} и {c} одинаковая наибольшая сумма цифр: {sum_a}")
        else:
            print(f"У чисел {b} и {c} одинаковая наибольшая сумма цифр: {sum_b}")

if __name__ == "__main__":
    main()
