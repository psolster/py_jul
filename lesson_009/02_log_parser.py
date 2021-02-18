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


from collections import defaultdict


class LogParser:
    slice_date_start_1 = 0
    slice_date_finish_1 = 17
    slice_date_start_2 = 0
    slice_date_finish_2 = 0

    def __init__(self, filename):
        self.filename = filename
        self.count_lines = 0
        self.position_on_files = 0
        self.voc_time_nok = defaultdict(int)
        self.nok_count = 0

    def how_to_work(self):
        data = self.list_number_lines_w_nok()
        self.data_print(data)
        self.print_to_file(data)

    def list_number_lines_w_nok(self):

        with open(self.filename, 'r', encoding='cp1251') as ff:
            for n, line in enumerate(ff, 1):
                data = line
                if data[29:] == 'NOK\n':
                    time = data[self.slice_date_start_1:self.slice_date_finish_1] + ']' + \
                           ' ' + '[' + data[self.slice_date_start_2:self.slice_date_finish_2] + ']'
                    self.voc_time_nok[time] += 1
        return self.voc_time_nok

    def data_print(self, data):
        for key, count in data.items():
            print(key, count)

    def print_to_file(self, data):
        ff = open('pars_log.txt', 'a', encoding='utf8')
        for key, count in data.items():
            data = key + ':->  ' + str(count) + '\n'
            ff.writelines(data)
        ff.close()


class LogParserHours(LogParser):
    slice_date_start_1 = 0
    slice_date_finish_1 = 11
    slice_date_start_2 = 12
    slice_date_finish_2 = 14


class LogParserMonth(LogParser):
    slice_date_start_1 = 0
    slice_date_finish_1 = 5
    slice_date_start_2 = 6
    slice_date_finish_2 = 8


class LogParserYear(LogParser):
    slice_date_start_1 = 0
    slice_date_finish_1 = 5
    slice_date_start_2 = 0
    slice_date_finish_2 = 0


file_names = 'events.txt'
work = LogParser(file_names)
work.how_to_work()

work2 = LogParserHours(file_names)
work2.how_to_work()

work3 = LogParserMonth(file_names)
work3.how_to_work()

work4 = LogParserYear(file_names)
work4.how_to_work()

# После зачета первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
