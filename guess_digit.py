#   Game "Guess digit"

from random import *

#   input right border
def is_right_border():
    print('Введите число, до которого будем угадывать.', 'Начальное число 1', sep='\n')
    global right_border
    right_border= int(input())

#   valid user digit for 1 - right_border
def is_valid(digit):
    if digit.isdigit() == True and 0 < int(digit) <= right_border:
        return True
    else:
        return False
#   game code
def game():
    rand_digit = randrange(1, right_border + 1)
    count = 0
    user_digit = 0
    print('Угадай целое число от 1 до', right_border)
    while rand_digit != user_digit:
        user_digit = input()
        if is_valid(user_digit) == True:
            if int(user_digit) < rand_digit:
                print('Слишком мало, попробуйте еще раз.')
                count += 1
                continue
            elif int(user_digit) > rand_digit:
                print('Слишком много, попробуйте еще раз.')
                count += 1
                continue
            else:
                print('Вы угадали, поздравляем!')
                count += 1
                print('Вы совершили', count, 'попыток.')
                print('Сыграем ещё?', 'Введите "да" или "нет" без кавычек', sep='\n')
                repeat = input()
                if repeat == 'да':
                    return True
                else:
                    return False
        else:
            print('Введите число от 1 до', right_border)

    if repeat == 'да':
        return True
    else:
        return False

run_game = True
while run_game == True:
    is_right_border()
    run_game = game()
else:
    print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
