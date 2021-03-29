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


def grouped_events(file_name):
    count = 0
    start_per = ''
    with open(file_name, 'r') as ff:
        for line in ff:
            if not line:
                continue
            line = line[:-1]
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
                    count = 0
                    yield old_per, sum_count
            else:
                continue

        # else:
        #     continue


# def grouped_events():
#     count = 0
#     start_per = get_lines(file_name=file_names)
#
#     for data in get_lines(file_name=file_names):
#         time = data[slice_date_start_1:slice_date_finish_1]
#         if time != start_per:
#             start_per = time
#             count += 1
#             # yield time, count
#         else:
#             count += 1
#         yield start_per, count
#
#
#
#
#
#         yield time , count


# TODO Группировка событий должна происходить внутри функции генератора,
#  который должен выдавать время и количество событий.
#  События в файле отсортированы по возрастанию даты и времени.
#  Поэтому нет необходимости предварительно обрабатывать данные, и только потом возвращать.
#  Такой подход не оптимален из-за необходимости хранить все данные.
#  Нужно переделать код таким образом, чтобы возвращать (yield) результат сразу после его получения.
#  Т. е. хранить нужно только счётчик событий и строку с текущим периодом времени.
#  При обработке строки нужно проверять, что период совпадает, и тогда нужно только увеличить
#  счётчик. Если значение не совпадает, то нужно возвращать период и накопленное количество событий.
#  И заменяете старый период на новый. После завершения цикла по строкам файлов нужно сделать
#  заключительным yield, возвращая последний накопленный результат.

even = grouped_events(file_name=file_names)
for time, count in even:
    print(time, count)
