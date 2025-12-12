'''
Дана строка-предложение на русском языке. Зашифровать ее, выполнив 
циклическую замену каждой буквы на следующую за ней в алфавите и сохранив при 
этом регистр букв («А» перейдет в «Б», «а» — в «б», «Б» — в «В», «я» — в «а» и т. 
д.). Букву «ё» в алфавите не учитывать («е» должна переходить в «ж»). Знаки 
препинания и пробелы не изменять.
'''
C = input("Введите строку-предложение на русском языке: ")

capital_letters = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
lower_letters = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

result = ""
for ch in C:
    changed = False
    for i in range(len(capital_letters)):
        if ch == capital_letters[i]:
            if i == len(capital_letters) - 1:
                result += capital_letters[0]
            else:
                result += capital_letters[i + 1]
            changed = True

    if not changed:
        for i in range(len(lower_letters)):
            if ch == lower_letters[i]:
                if i == len(lower_letters) - 1:
                    result += lower_letters[0]
                else:
                    result += lower_letters[i + 1]
                changed = True

    if not changed:
        result += ch
        
print("Зашифрованный текс:", result)
