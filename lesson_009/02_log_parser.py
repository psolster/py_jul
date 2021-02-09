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


class LogParser:

    def __init__(self, filename):
        self.filename = filename
        self.count_lines = 0
        self.position_on_files = 0

        self.voc_time_nok = defaultdict(int)

        self.nok_count = 0

    def len_files(self):

        ff = open(self.filename, 'r', encoding='cp1251')
        self.count_lines = sum(1 for _ in ff)
        ff.close()
        return self.count_lines

    def list_number_lines_w_nok(self):

        while self.count_lines != 0:
            ff = open(self.filename, 'r', encoding='cp1251')
            ff.seek(self.position_on_files)
            data = ff.readline()
            self.position_on_files = ff.tell()

            if data[29:] == 'NOK\n':
                time = data[1:17]
                self.voc_time_nok[time] += 1

                self.nok_count += 1

            self.count_lines -= 1

            ff.close()
        return self.voc_time_nok

    def data_print(self, data):
        for key, count in data.items():
            print(key, count)

    def print_to_file(self, data):
        ff = open('pars_log.txt', 'w', encoding='cp1251')
        for key, count in data.items():
            data = key + ':-)  ' + str(count) + '\n'
            ff.writelines(data)
        ff.close()


file_names = 'events.txt'
work = LogParser(file_names)

res = work.len_files()
res2 = work.list_number_lines_w_nok()
work.data_print(data=res2)
work.print_to_file(res2)

# После зачета первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
