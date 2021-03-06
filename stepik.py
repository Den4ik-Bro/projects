'''Недавно мы считали для каждого слова количество его вхождений в строку.
 Но на все слова может быть не так интересно смотреть, как, например, 
 на наиболее часто используемые.

Напишите программу, которая считывает текст из файла
(в файле может быть больше одной строки) и выводит
самое частое слово в этом тексте и через пробел то,
сколько раз оно встретилось.
Если таких слов несколько,
 вывести лексикографически первое
(можно использовать оператор < для строк).

В качестве ответа укажите вывод программы, а не саму программу.

Слова, написанные в разных регистрах, считаются одинаковыми.

Sample Input:

abc a bCd bC AbC BC BCD bcd ABC
Sample Output:

abc 3''' 
        # на данном тесте программа сработала как надо
         # но на файле выдает не то слово, количество вхождений выдает
         # правильное
#---------------------------------------------------------------------


text = open('C:\\Users\\User\\Desktop\\dataset_3363_3.txt', 'r')
lst = []
lst2 = []
for line in text:   #читаем по строчно текст
    line = line.lower().strip()     # удаляем лишние пробелы и \n   
    lst = line.split()   #делаем из каждой строки список
    lst2.extend(lst)
print(lst2)

count_lst = []
count = 0
s = ''
for i in range(len(lst2) - 1):
    count = lst2.count(lst2[i])
    count_lst.append(count)
    if lst2.count(lst2[i]) > lst2.count(lst2[i + 1]):
        s = lst2[i]
    else:
        s = lst2[i + 1]
print(s, max(count_lst))

