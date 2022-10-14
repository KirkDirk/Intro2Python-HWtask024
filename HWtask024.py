# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

## формируем сжатую строку и записываем в файл 2
data1 = open('C:\Sas\LearningGB\Intro2Python\HW\HWtask024\data1.txt', 'r')
data2 = open('C:\Sas\LearningGB\Intro2Python\HW\HWtask024\data2.txt', 'w')
string1 = data1.read()
string2 = ''
count_char = 1
char1 = ''
for char in string1:
    if char == char1: 
        count_char += 1
    else:
        if char1:
            string2 += str(count_char) + char1
        count_char = 1
    char1 = char
string2 += str(count_char) + char1
data2.write(string2)
data1.close()
data2.close()

## формируем расжатую строку и записываем в файл 3
with open('C:\Sas\LearningGB\Intro2Python\HW\HWtask024\data2.txt', 'r') as data2:
    string2 = data2.read()
string3 = ''
for char in string2:
    if char.isdigit(): 
        temp = char
    else:
        string3 += char * int(temp)
        temp = ''
with open('C:\Sas\LearningGB\Intro2Python\HW\HWtask024\data3.txt', 'w') as data3:
    data3.write(string3)