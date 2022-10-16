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
list1=[]
list2=[]
string3 = ''
temp = string2[0]
list1.append(temp)
i=1
while i < len(string2):
    if not string2[i].isdigit():
        list2.append(string2[i])
    elif string2[i].isdigit() and string2[i-1].isdigit():
        temp += string2[i]
        list1[index_temp] = temp 
    else:
        temp = string2[i]
        list1.append(string2[i])
        index_temp = len(list1)-1
    i += 1
list3 = list(map(lambda x, y: int(x)*y, list1, list2))
string3 = ''.join(list3)