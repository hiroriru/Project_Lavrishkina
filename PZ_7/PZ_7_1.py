'''
Дан символ C, изображающий цифру или букву (латинскую или русскую). Если C
изображает цифру, то вывести строку «digit», если латинскую букву — вывести
строку «lat», если русскую — вывести строку «rus».
'''
C = input("Введите символ: ")

if len(C) != 1:
    print("Ошибка: введите ровно один символ")
else:
    char = C
    
    if char.isdigit():
        print("digit")
    elif char.isalpha():
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            print("lat")
        elif 'а' <= char <= 'я' or 'А' <= char <= 'Я':
            print("rus")
        else:
            print("Неизвестный символ")
    else:
        print("Неизвестный символ")
