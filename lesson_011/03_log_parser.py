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
    global time
    count = 0
    start_per = ''
    next_str = gen_lines(file_name=file_names)
    for line in next_str:
        time = line
        if start_per == '':
            start_per = line
        if time == start_per:
            start_per = line
            count += 1
        else:
            old_per = start_per
            start_per = time
            sum_count = count
            count = 1
            yield old_per, sum_count


# TODO При работе генератора теряется последнее накопленное значение.
#  Должна выводиться строка с количеством событий в 2018-05-17 11:34.
even = grouped_events()
for time, counts in even:
    print(f'[{time}] {counts}')
