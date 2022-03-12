#   Game "Magic Ball"

from random import *

#   List answer for question
answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]

#   Start program
print('Привет, я магический шар, и я знаю ответ на любой твой вопрос.', 'Как тебя зовут?', sep='\n')
name = input()
print('Привет', name)

# Choice answer
def is_choice():
    global answers
    return choice(answers)
be_question = True
while be_question == True:
    print('Задай свой вопрос.')
    question = input()
    print(is_choice())
    print('У тебя ещё есть вопросы?')
    repeat = input()
    if repeat != 'да':
        be_question = False
