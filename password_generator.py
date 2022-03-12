from random import *

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
similar_symbols = 'il1Lo0O'

chars = ''

amount_pw = input('Сколько паролей нужно сгенерировать?')
len_pw = input('Сколько символов длинной должен быть пароль?')
use_digits = input('Использовать цифры? (да/нет)')
use_upper = input('Использовать прописные буквы? (да/нет)')
use_lower = input('Использовать строчные буквы? (да/нет)')
use_punctuation = input('Использовать спецсимволы? (да/нет)')
use_similar = input('Использовать неоднозначные символы (il1Lo0O)? (да/нет)')

def create_chars_list():
    global chars
    if use_digits == 'да':
        chars += digits
    if use_upper == 'да':
        chars += uppercase_letters
    if use_lower == 'да':
        chars += lowercase_letters
    if use_punctuation == 'да':
        chars += punctuation

def generate_password(lenght):
    global use_similar
    global chars
    global similar_symbols
    result = ''
    if use_similar == 'да':
        while len(result) < int(lenght):
            result += choice(chars)
    else:
        while len(result) < int(lenght):
            i = choice(chars)
            if i not in similar_symbols:
                result += i
    return result

create_chars_list()
for i in range(int(amount_pw)):
    print(generate_password(len_pw))
