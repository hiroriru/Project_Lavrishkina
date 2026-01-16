'''
Даны три словаря на три элемента каждый. Объединить все словари в один. Вывести 
исходные словари и результирующий.  
'''
one = {1: "banan", 2: "apple", 3: "pineapple"}
two = {"banan": 1, "apple": 2, "pineapple": 3}
tree = {"Liza": "инженер", "Dasha": "химик", "Anna": "повар"}

print("Исходные словари:")
print(f"Первый словарь: {one}")
print(f"Второй словарь: {two}")
print(f"Третий словарь: {tree}\n")

result_dict = {}
result_dict.update(one) 
result_dict.update(two)
result_dict.update(tree)

print("Результирующий словарь:")
print(result_dict)
