from random import*
from time import*

def gray(): # серый
	print("\033[1m\033[30m")
def red(): # красный
	print("\033[1m\033[31m")
def green(): # зелёный
	print("\033[1m\033[32m")
def yellow(): # желтый
    print("\033[1m\033[33m")
def blue(): # синий
	print("\033[1m\033[34m") 
def lilac(): # сиреневый
	print("\033[1m\033[35m")
def white_blue(): # голубой
	print("\033[1m\033[36m")
def white(): # белый
    print("\033[0m\033[37m")

answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определенно да','Можешь быть уверен в этом','Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да', ' Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно']

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')

name = input('Как вас зовут? ', )
print('Привет', name)

flag = True
while flag == True:
    question = input('Задайте свой вопрос ', )
    sleep(2)
    ans = choice(answers)
    if ans in answers[:5]:
        green()
    elif ans in answers[5:10]:
        blue()
    elif ans in answers[10:15]:
        yellow()
    elif ans in answers[15:]:
        red()
    print(ans)
    white()
    next = input('Хотите задать еще один вопрос? ', )
    if next.lower() == 'да':
        flag = True
    else:
        flag = False
        print('Возвращайся, если возникнут вопросы')
        break