import random
def is_valid(s):
    if s.isdigit() and 1 <= int(s) <= 100:
        return True
    else:
        return False

def game():
    count = 0
    print('Добро пожаловать в числовую угадайку')
    right_border = int(input('компьютер загадает число от единицы до того, какое вы введете.\n Введите число:  '))
    num = random.randint(1, right_border)
    print('Угадайте какое число загадал компьютер от 1 до' ,right_border)
    while True:
        n = input('Введите число: ')
        if is_valid(n) == True:
            n = int(n)
            count += 1
        else:
            print('Нужно ввести число в диапозоне от единицы до ста!')
            continue
        if count > 8:
            print('У вас кончились попытки, вы проиграли.')
            break
        elif n > num:
            print('Ваше число больше загаданного, попробуйте еще разок')
        elif n < num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif n == num:
            print('Вы угадали, поздравляем!')
            break
           
    print('''Спасибо, что играли в числовую угадайку,
            если хотите повторить попытку введите "Y"''')
    answer = input()
    if answer.lower == 'Y' or  answer == 'н':
        game()
    else:
        print('Досвидания!')
            
        
game()










             
