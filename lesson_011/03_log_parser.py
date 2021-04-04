# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>  # Итератор или генератор? выбирайте что вам более понятно
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234

from collections import defaultdict

file_names = 'events.txt'
slice_date_start_1 = 1
slice_date_finish_1 = 17
slice_date_start_2 = 0
slice_date_finish_2 = 0


def gen_lines(file_name):
    with open(file_name, 'r') as ff:
        for line in ff:

            if not line:
                continue
            line = line[:-1]
            if line[29:] == 'NOK':
                line_w_nok = line[slice_date_start_1:slice_date_finish_1]
                yield line_w_nok



def grouped_events():
    count = 0
    start_per = ''
    line = gen_lines(data)
    if line[29:] == 'NOK':
        if start_per == '':
            start_per = line[slice_date_start_1:slice_date_finish_1]
            time = line[slice_date_start_1:slice_date_finish_1]
                if time == start_per:
                    count += 1
                else:
                    old_per = start_per
                    start_per = time
                    sum_count = count
                    count = 1
                    yield old_per, sum_count




# TODO При работе генератора теряется последнее накопленное значение.
#  Должна выводиться строка с количеством событий в 2018-05-17 11:34.
even = grouped_events(file_name=file_names)
for time, count in even:
    print(f'[{time}] {count}')
