'''
Составить функцию, которая выведет на экран строку, содержащую задаваемое с 
клавиатуры число символов. 
'''
def print_symbols_count():
    count = int(input("Введите количество символов: "))
    symbol = input("Введите символ для вывода: ")
    
    result = symbol * count
    print(result)

print_symbols_count()
