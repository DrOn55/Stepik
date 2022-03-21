
#   clarifying questions
#cipher = input('Шифруем или дешифруем? (ш/д)')
cipher = 'д'
#language = input('Какой язык алфавита? (рус/анг)')
language = 'анг'
key = input('Шаг сдвига?')
#text = input('Введите текст.')
text = 'Hawnj pk swhg xabkna ukq nqj.'
def do_cipher(cipher, language, key, text):
    lst = list()
    eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    if language == 'анг':
        lower_alphabet = eng_lower_alphabet
        upper_alphabet = eng_upper_alphabet
    else:
        lower_alphabet = rus_lower_alphabet
        upper_alphabet = rus_upper_alphabet

    if cipher == 'ш':
        key = int(key)
    else:
        key = -int(key)

    for i in range(len(text)):
        if text[i] in lower_alphabet:
            index_i = lower_alphabet.find(text[i])
            if (index_i + key) > (len(lower_alphabet) - 1):
                index_key = index_i + key - len(lower_alphabet)
            else:
                index_key = index_i + key
            lst.append(lower_alphabet[index_key])
        elif text[i] in upper_alphabet:
            index_i = upper_alphabet.find(text[i])
            if (index_i + key) > (len(upper_alphabet) - 1):
                index_key = index_i + key - len(upper_alphabet)
            else:
                index_key = index_i + key
            lst.append(upper_alphabet[index_key])
        else:
            lst.append(text[i])
    result = ''.join(lst)
    return result


print(do_cipher(cipher, language, key, text))