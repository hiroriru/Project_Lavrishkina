'''
Дан список размера N. Найти максимальный из его локальных минимумов 
(локальный минимум — это элемент, который меньше любого из своих соседей). 
'''
import random

try:
    N = int(input("Введите размер списка N: "))
    lst = []

    if N < 3:
        print("Локальных минимумов нет (нужно хотя бы 3 элемента).")
    else:
        for i in range(N):
            num = random.randint(-50, 50)
            lst.append(num)
        print("Сгенерированный список:", lst)

        local_mins = []
        i = 1
        
        while i < N - 1:
            c = lst[i]
            left = lst[i - 1]
            right = lst[i + 1]
            i += 1

            if c < left and c < right:
                local_mins.append(c)
                print(f"Ура. Локальный минимум найден: {c}. Соседи {left} и {right}")

        if local_mins:
            print("Максимальный из локальных минимумов:", max(local_mins))
        else:
            print("Локальных минимумов нет.")

except ValueError:
    print("Ошибка: введите целое число для N.")
