from random import*
#константы
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
#запрашиваем у пользователя информацию
n = int(input('Количество паролей для генерации ', ))
length = int(input('Длина одного пароля ', ))
digit = input('Включать в пароль цифры? ', )
up_let = input('Включать в пароль прописные буквы? ' , )
low_let = input('Включать в пароль строчные буквы? ', )
symbols = input('Включать в пароль символы: "!#$%&*+-=?@^_" ? ', )
no_one_sym = input('Исключить из пароля неоднозначные символы: "il1Lo0O" ? ', )

if digit.lower() == 'да':
    chars += digits
if up_let.lower() == 'да':
    chars += uppercase_letters
if low_let.lower() == 'да':
    chars += lowercase_letters
if symbols.lower() == 'да':
    chars += punctuation
if no_one_sym.lower() == 'да':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')

def generate_password(l, ch):
    return sample(ch, l)

print('Сгенерированные пароли:')    
for _ in range(n):
    print(*generate_password(length, chars), sep = '')
print('Работа завершена')