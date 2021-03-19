import random

def generate_password(length, chars):
    password = ''
    for j in range(length):
        password += random.choice(chars)
    return print(password)

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
count_pass = int(input('сколько сгенерировать паролей?: '))
len_pass = int(input('Длинна пароля?: '))
dig_pass = input('Включать ли цифры 0123456789? д = да, н = нет: ')
up_pass = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?; д = да, н = нет: ')
low_pass = input('Включать ли строчные буквы abcdefghiklmnopqrstuwxyz; д = да, н = нет: ')
symbol = input('Включать ли символы !#$%&*+-=?@^_?; д = да, н = нет: ')
bad_symbols = input('Исключать ли неоднозначные символы il1Lo0O; д = да, н = нет: ')
if dig_pass.lower() == 'д':
    chars += digits
elif up_pass.lower() == 'д':
    chars += uppercase_letters
elif low_pass.lower() == 'д':
    chars += lowercase_letters
elif symbol.lower() == 'д':
    chars += punctuation
elif bad_symbols.lower() == 'д':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')

for i in range(count_pass):
    generate_password(len_pass, chars)
input()


