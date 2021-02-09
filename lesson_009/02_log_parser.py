# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4

import operator
from collections import defaultdict

# position_on_files = 0
global count_lines
from collections import defaultdict

def len_files(file_name):
    file_name = file_name
    ff = open(file_name, 'r', encoding='cp1251')
    count_lines = sum(1 for _ in ff)
    ff.close()
    return count_lines


def list_number_lines_w_nok(file_name, count_lines):
    voc_time_nok = defaultdict(int)
    position_on_files = 0
    nok_count = 0
    while count_lines != 0:
        ff = open(file_name, 'r', encoding='cp1251')
        ff.seek(position_on_files)
        data = ff.readline()
        position_on_files = ff.tell()

        if data[29:] == 'NOK\n':
            time = data[1:17]
            voc_time_nok[time] += 1

            nok_count += 1

        count_lines -= 1

        ff.close()
    return nok_count, voc_time_nok


file_names = 'events.txt'
count_lines = 0
res = len_files(file_name=file_names)
res2 = list_number_lines_w_nok(file_name=file_names, count_lines=res)
print(res, res2)

# После зачета первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
