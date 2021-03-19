'''Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.'''


import requests
url = 'https://stepic.org/media/attachments/course67/3.6.3/699991.txt'
r = requests.get(url)
d = {}
d['key'] = r.text
while url[-3:] == 'txt':
    url = 'https://stepic.org/media/attachments/course67/3.6.3/'
    url += d['key']
    r = requests.get(url)
    print(r.text)
    d['key'] = r.text