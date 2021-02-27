# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.
# import os


class NotNameError(Exception):

    def __init__(self):
        self.message = 'Ошибка в указании имени'

    def __str__(self):
        return self.message


class NotEmailError(Exception):

    def __init__(self):
        self.message = 'Ошибка при вводе e-mail'

    def __str__(self):
        return self.message


def filling_check(sline):
    name, e_male, age = sline.split(' ')
    age = int(age)
    try:
        if len(name) or len(e_male) or len(str(age)) != 0:
            if not name.isalpha():
                raise NotNameError()
            elif '@' not in e_male:
                if '.' not in e_male:
                    raise NotEmailError()
            elif not 10 < age < 99:
                raise ValueError('возраст не тот')
            else:
                fg.write(line + '\n')
    finally:
        pass


name_file = 'registrations.txt'
with open(name_file, 'r', encoding='utf8') as ff, open('registrations_good.log', 'a+', encoding='utf8') as fg, open(
        'registrations_bad.log', 'a+', encoding='utf8') as fb:
    for line in ff:
        line = line[:-1]
        try:
            filling_check(line)
        except (NotNameError, NotEmailError, ValueError) as err:
            fb.write(line + ' ошибка ' + str(err) + '\n')

# Зачёт!
