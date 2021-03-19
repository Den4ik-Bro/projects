def average_rating(text):
    file = open('C:\\Users\\User\\Desktop\\test.txt', 'w')
    lst = []
    lst2 = []
    lst3 = []
    d = {}
    text = text.read().strip().splitlines()
    for i in range(len(text)):
        lst2.append(text[i].split(';'))
    for i in lst2:
        lst3.append(i[0])
        x = (int(i[1]) + int(i[2]) + int(i[3])) / 3
        lst3.append(x)
        d[lst3[0]] = lst3[1]
        lst3.clear()
    for i in d:
        file.write(str(d[i]) + '\n')


def average_1(text):
    file = open('C:\\Users\\User\\Desktop\\test.txt', 'a')
    lst = []
    lst2 = []
    lst3 = []
    lst4 = []
    text = text.read().strip().splitlines()
    for i in range(len(text)):
        lst.append(text[i].split(';'))
    for i in lst:
        lst2.append(int(i[1]))
        lst3.append(int(i[2]))
        lst4.append(int(i[3]))
    x = len(lst2)
    x1 = len(lst3)
    x2 = len(lst4)
    a = sum(lst2) / x
    b = sum(lst3) / x1
    c = sum(lst4) / x2
    final_list = []
    final_list.append(a)
    final_list.append(b)
    final_list.append(c)
    for i in final_list:
        file.write(str(i) + ' ')



text = open('C:\\Users\\User\\Desktop\\dataset_3363_4 (1).txt', 'r')
average_rating(text) 
text.close()
text = open('C:\\Users\\User\\Desktop\\dataset_3363_4 (1).txt', 'r')
average_1(text)
