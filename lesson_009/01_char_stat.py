# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shзыщдandrinov/python_base_snippets/snippets/4

import operator
from pprint import pprint

alpha_count = {}

for cod in range(1040, 1104):
    alpha_count[chr(cod)] = 0
file_name = 'voyna-i-mir.txt'

with open(file_name, 'r', encoding='cp1251') as file:
    for line in file:
        for char in line:
            if char in alpha_count.keys():

                alpha_count[char] += 1

sorted_list = sorted(alpha_count.items(), key=operator.itemgetter(1), reverse=True)
sorted_alpha_count = {k: v for k, v in sorted_list}
print('+---------------+')
print('|{mes1:^7}|{mes2:^7}|'.format(mes1='Буква', mes2='Кол-во'))
print('+---------------+')
for letter, count in sorted_alpha_count.items():
    print('|{letter:^6} | {count:6d}|'.format(letter=letter, count=count))
print('+---------------+')
print('|{mes1:^7}|{mes2:^7}|'.format(mes1='Итого', mes2=sum(sorted_alpha_count.values())))
print('+---------------+')

# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
