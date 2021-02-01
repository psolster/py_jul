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


class CountNOK:

    def __init__(self, filename):
        self.filename = filename
        self.count_lines = 0
        self.position_on_files = 0
        self.count_dict = defaultdict(int)

    def step_by_step(self):
        self.lenght_file()
        while self.count_lines != 0:
            symb_line = self.get_data(self.filename)
            self.nok_or_ok(symb_line) # заменить на функцию проверки на NOK
        self.count_dict = self.sorter() #

    def lenght_file(self):
        ff = open(self.filename, 'r', encoding='cp1251')
        self.count_lines = sum(1 for _ in ff)
        ff.close()

    def get_data(self, filename):
        file = open(filename, 'r', encoding='cp1251')
        file.seek(self.position_on_files)
        data = file.readline()
        self.position_on_files = file.tell()
        self.count_lines -= 1
        file.close()
        return data

    def nok_or_ok(self, data):
        for char in data:
            if char.isalpha():
                self.count_dict[char] += 1
            elif char == '/n':
                self.count_lines -= 1
                return

    def sorter(self):
        sorted_list = dict(sorted(self.count_dict.items(), key=operator.itemgetter(1), reverse=True))

        return sorted_list

    def print_rezults(self, norm_voc):
        print('+---------------+')
        print('|{mes1:^7}|{mes2:^7}|'.format(mes1='Буква', mes2='Кол-во'))
        print('+---------------+')

        for letter, count in norm_voc.items():
            print('|{letter:^6} | {count:6d}|'.format(letter=letter, count=count))
        print('+---------------+')
        print('|{mes1:^7}|{mes2:^7}|'.format(mes1='Итого', mes2=sum(norm_voc.values())))
        print('+---------------+')


class CountSymbolNumUp(CountSymbol):
    def sorter(self):
        sorted_list = dict(sorted(self.count_dict.items(), key=operator.itemgetter(1), reverse=False))
        return sorted_list


class CountSymbolAlfUp(CountSymbol):
    def sorter(self):
        sorted_list = dict(sorted(self.count_dict.items(), key=operator.itemgetter(0)))
        return sorted_list


class CountSymbolAlfDown(CountSymbol):
    def sorter(self):
        sorted_list = dict(sorted(self.count_dict.items(), key=operator.itemgetter(0), reverse=True))
        return sorted_list


file_name = 'voyna-i-mir.txt'

start = CountSymbol(file_name)
start.step_by_step()
res = start.sorter()
start.print_rezults(res)

start = CountSymbolNumUp(file_name)
start.step_by_step()
res2 = start.sorter()
start.print_rezults(res2)

start = CountSymbolAlfUp(file_name)
start.step_by_step()
res3 = start.sorter()
start.print_rezults(res3)

start = CountSymbolAlfDown(file_name)
start.step_by_step()
res4 = start.sorter()
start.print_rezults(res4)

# После зачета первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
