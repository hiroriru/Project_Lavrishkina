'''
Из исходного текстового файла (ip_address.txt) из раздела «Зарезервированные
адреса» перенести в первый файл строки с ненулевыми первым и вторым октетами,
а во второй – все остальные. Посчитать количество полученных строк в каждом
файле.
'''
import re

with open('ip_address.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

count_first = 0   
count_second = 0  

pattern = re.compile(r'^(\d+)\.(\d+)')

with open('first_file.txt', 'w', encoding='utf-8') as f1, \
     open('second_file.txt', 'w', encoding='utf-8') as f2:

    for line in lines:
        matches = pattern.findall(line)
        
        if matches:
            first_octet_str, second_octet_str = matches[0]
            
            first_octet = int(first_octet_str)
            second_octet = int(second_octet_str)

            if first_octet != 0 and second_octet != 0:
                f1.write(line)
                count_first += 1
            else:
                f2.write(line)
                count_second += 1
        else:
            f2.write(line)
            count_second += 1

print(f"В first_file.txt записано строк: {count_first}")
print(f"В second_file.txt записано строк: {count_second}")