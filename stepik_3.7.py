f = open('C:\\Users\\User\\Desktop\\dataset_3380_5 (2).txt', 'r')
d = {
    '1': [],
    '2': [],
    '3': [],
    '4': [],
    '5': [],
    '6': [],
    '7': [],
    '8': [],
    '9': [],
    '10': [],
    '11': []
}
for line in f:
    lst = line.strip().split()
    if lst[0] in d:
        d[lst[0]].append(int(lst[-1]))
for i in d:
    print(i, sum(d[i]) / len(d[i]))
