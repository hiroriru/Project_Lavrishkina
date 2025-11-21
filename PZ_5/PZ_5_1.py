"""
Составить функцию, которая выведет на экран строку, содержащую задаваемое с
клавиатуры число символов.
"""
def print_symbols_count():
    try:
        count = int(input("Введите количество символов: "))
        symbol = input("Введите символ для вывода: ")

        if not symbol:
            print("К сожалению, символ не можжет быть пустым. ")

        if count < 0:
            print("Упс. Произошла ошибка. Введите число больше нуля.")

        result = symbol * count
        print(result)

    except ValueError:
        print("Упс. Ошибка. Введите целое число количества символов.")


print_symbols_count()
