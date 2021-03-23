"""Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.

Выведите одно число – количество вхождений строки t в строку s.

Пример:
s = "abababa"
t = "aba"

Вхождения строки t в строку s:
abababa
abababa
abababa"""



s = input()
t = input()
count = 0
i = -1
while True:
    i = s.find(t, i + 1)
    if i == -1:
        print(count)
        break
    count += 1