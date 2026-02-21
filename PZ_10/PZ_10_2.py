'''
Из предложенного текстового файла (text18-6.txt) вывести на экран его содержимое, 
количество пробельных символов. Сформировать новый файл, в который поместить текст 
в стихотворной форме предварительно заменив все знаки пунктуации на знак «!». 
'''
f = open("text18-6.txt", encoding="utf-16")
text = f.read()
f.close()

print(f"Содержимое файла:\n{text}\n")

probely = 0
for i in range(len(text)):
    if text[i] == " " or text[i] == "\n":
        probely = probely + 1

print(f"Количество пробельных символов (пробелы и переводы строк): {probely}\n")

znaki = [".", ",", "?", ";", ":", "-", "—", "(", ")", '"', "'"]
noviy_text = ""

for i in range(len(text)):
    if text[i] in znaki:
        noviy_text = noviy_text + "!"
    else:
        noviy_text = noviy_text + text[i]

f2 = open("text18-6_new.txt", "w", encoding="utf-8")
f2.write(noviy_text)
f2.close()

print(f"Текст со знаками '!':\n{noviy_text}")
