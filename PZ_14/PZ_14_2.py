'''
Разработать программу с применением пакета tk, взяв в качестве условия одну
любую задачу из ПЗ №№ 1 – 9.

Даны целые числа N (>2), A и B. Сформировать и вывести целочисленный список 
размера 10, первый элемент которого равен A, второй равен B, а каждый 
последующий элемент равен сумме всех предыдущих.
'''
import tkinter as tk

def generate_list():
    """Функция, обрабатывающая нажатие кнопки."""
    try:
        N = int(entry_n.get())
        A = int(entry_a.get())
        B = int(entry_b.get())

        if N <= 2:
            result_label.config(text="Ошибка: N должно быть больше 2.", fg="red")
        else:
            lst = [A, B]
            i = 0
            while i < 8:
                next_element = sum(lst)
                lst.append(next_element)
                i += 1

            result_label.config(text=f"Список: {lst}", fg="black") 

    except ValueError:
        result_label.config(text="Упс. Произошла ошибка. Введите целые числа.", fg="red")


root = tk.Tk()
root.title("Генератор списка")
root.geometry("500x300") 
root.resizable(False, False) 

label_n = tk.Label(root, text="Введите N (>2):")
label_n.pack(pady=(10, 0))
entry_n = tk.Entry(root)
entry_n.pack(pady=5)

label_a = tk.Label(root, text="Введите A:")
label_a.pack(pady=(5, 0))

entry_a = tk.Entry(root)
entry_a.pack(pady=5)

label_b = tk.Label(root, text="Введите B:")
label_b.pack(pady=(5, 0))

entry_b = tk.Entry(root)
entry_b.pack(pady=5)

button_generate = tk.Button(root, text="Сгенерировать", command=generate_list, fg='green')
button_generate.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 10), wraplength=450, justify="left")
result_label.pack(pady=10)

root.mainloop()
