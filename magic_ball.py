import random
otvet = ['да', 'конечно']
answear = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да','Можешь быть уверен в этом',
            'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да',
            'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять',
            'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно']
print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
name = input('Как тебя зовут? \n')
print('Привет,', name)
while True:
    question = input('Задай вопрос:\n')
    print(random.choice(answear))
    print('Хотите продолжить? \n')
    s = input()
    if s in otvet:
        continue
    else:
        print('Возвращайся как возникнут вопросы!')
        break
input()
