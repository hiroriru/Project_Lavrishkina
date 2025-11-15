'''
Дан список размера N. Найти максимальный из его локальных минимумов 
(локальный минимум — это элемент, который меньше любого из своих соседей). 
'''
N = int(input("Введите размер списка N: "))
lst = list(map(int, input(f"Введите {N} целых чисел через пробел: ").split()))

if len(lst) != N:
    print("Ошибка: количество введённых чисел не совпадает с N.")
else:
    local_mins = []

    for i in range(1, N - 1):
        if lst[i] < lst[i - 1] and lst[i] < lst[i + 1]:
            local_mins.append(lst[i])

    if local_mins:
        max_local_min = max(local_mins)
        print(max_local_min)
    else:
        print("Локальных минимумов нет.")
