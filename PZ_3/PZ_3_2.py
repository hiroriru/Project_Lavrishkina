'''
Смоделировать простейший калькулятор, умеющий выполнять 4 основные 
арифметические операции 
'''
print("Простой калькулятор")
print("Доступные операции: +, -, *, /")
print("Для выхода введите '0'")

while True:
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        
        operation = input("Введите операцию (+, -, *, /) или '0' для выхода: ")
        
        if operation == '0':
            print("До свидания!")
            break
       
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Ошибка: деление на ноль!")
                continue
            result = num1 / num2
        else:
            print("Ошибка: неизвестная операция!")
            continue
        
        print(f"Результат: {num1} {operation} {num2} = {result}")
        
    except ValueError:
        print("Ошибка: введите числа корректно!")
    except KeyboardInterrupt:
        print("\nПрограмма прервана. До свидания!")
        break
