# Требует у пользователя только 1 или 2
def is_valid_12(var_1, var_2):
    question = input(f'\nХотите {var_1}? Тогда напишите "1". Если {var_2} - напишите "2". ').strip()
    while True:
        if question in ['1', '2']:
            question = int(question)
            return question
        else:
            question = input(f'Напишите 1, если хотите {var_1}. Если {var_2} - напишите 2. ')

# Требует корректное значение сдвига в зависимости от выбранного алфавита

def is_valid_rot(max_rot, eng, rus):
    rot = input(f'\nНа какое количество символов будет сдвиг? Напишите целое число от 1 до {max_rot}: ').strip()
    language = rus
    if max_rot == 25:
        language = eng
    while True:
        if rot.isdigit():
            rot = int(rot)
            if 1 <= rot <= max_rot:
                return rot
            else:
                rot = input(f'Так как вы решили {language} - сдвиг должен быть от 1 до {max_rot}. ').strip()
        else:
            rot = input(f'Так как вы решили {language} - сдвиг должен быть от 1 до {max_rot}. ').strip()

# Сам Алгоритм Цезаря.

def caesar_algorithm(step, max_rot, process):
    phrase = input(f'\nНапиши фразу на том языке, который выбрал. Тогда я смогу её корректно {process}: ').strip()
    new_phrase = ''
    num = [1103, 1071, 1072, 1040, 32]
    eng = [122, 90, 97, 65, 26]
    if max_rot == 25:
        num = eng
    for i in range(len(phrase)):
        if phrase[i].isalpha():
            new_ord = ord(phrase[i]) + int(step)
            if phrase[i].islower() and new_ord > num[0] or \
                    (phrase[i].isupper() and new_ord > num[1]):
                new_ord = new_ord - num[4]
            elif phrase[i].islower() and new_ord < num[2] or \
                 (phrase[i].isupper() and new_ord < num[3]):
                new_ord = new_ord + num[4]
            new_phrase += chr(new_ord)
        else:
            new_phrase += phrase[i]
    return new_phrase

shifr, deshifr = 'зашифровать текст', 'дешифровать'
question_1 = is_valid_12(shifr, deshifr)
eng, rus = 'использовать английский алфавит', 'русский алфавит'
question_2 = is_valid_12(eng, rus)
max_rot = 25
language = 'английский'
process = 'зашифровать'
if question_2 == 2:
    max_rot = 32
    language = 'русский'
rot = is_valid_rot(max_rot, eng, rus)
step = rot
if question_1 == 2:
    rot = -rot
    process = 'дешифровать'

print(f'\nТы решил {process} свой текст и выбрал для этого {language} язык.')
print(f'Напоминаю, что величина сдвига: {step}.')
new_phrase = caesar_algorithm(rot, max_rot, process)
print(f'\nЛови результат: {new_phrase}')