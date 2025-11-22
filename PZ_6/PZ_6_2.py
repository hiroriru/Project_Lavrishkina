'''
Дан список размера N. Найти максимальный из его локальных минимумов 
(локальный минимум — это элемент, который меньше любого из своих соседей). 
'''
import random

try:
    N = int(input("Введите размер списка N: "))
    
    if N < 1:
        print("Ошибка: N должно быть натуральным числом (>= 1).")
    elif N < 3:
        print("Локальных минимумов нет (нужно хотя бы 3 элемента).")
    else:
        lst = [random.randint(-100, 100) for _ in range(N)]
        print("Сгенерированный список:", lst)

        local_mins = []
        for i in range(1, N - 1):
            if lst[i] < lst[i - 1] and lst[i] < lst[i + 1]:
                local_mins.append(lst[i])

        if local_mins:
            print("Максимальный из локальных минимумов:", max(local_mins))
        else:
            print("Локальных минимумов нет.")

except ValueError:
    print("Ошибка: введите целое число для N.")
