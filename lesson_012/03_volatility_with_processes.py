# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПРОЦЕССНОМ стиле
#
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
import operator
import os
import multiprocessing
import time


path = 'trades'


def read_dir(path_dir):
    files = os.listdir(path=path_dir)
    return files


def next_file_name():
    list_files = read_dir(path_dir=path)
    for name_files in list_files:
        yield str(name_files)


def sort_count_ticker(data):
    sorted_tuple = sorted(data.items(), key=operator.itemgetter(1))
    dict(sorted_tuple)
    return sorted_tuple


def output_data(dic):
    start_index = 0
    index = 0
    name_zero_tick = []
    volat_list = list(dic)
    max_volat = list(dic)[-1:-4:-1]
    min_volat = []
    print('Максимальная волантильность')
    for i in max_volat:
        ticker = str(i[0])
        volat = round(float(i[1]), 3)
        print(f'Тикер-> {ticker} - {volat} %')
    print('Минимальная волантильность')
    for i in volat_list:
        if i[1] > 0:
            start_index = index
            min_volat = volat_list[start_index:start_index + 3]
            min_volat.reverse()
            break
        index += 1
    for i in min_volat:
        ticker = str(i[0])
        volat = round(float(i[1]), 3)
        print(f'Тикер-> {ticker} - {volat} %')
    print('Нулевая волантильность')
    zero_volont = volat_list[:start_index]
    for i in zero_volont:
        name_zero_tick.append(i[0])
    name_zero_tick.sort()
    print(str(name_zero_tick))


class Ticker(multiprocessing.Process):
    def __init__(self, next_file, collector, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name_file = next_file
        self.min_price_tickers = 0
        self.max_price_tickers = 0
        self.half = 0
        self.volat = 0
        self.path = path
        self.name_ticker = ''
        self.collector = collector

    def run(self):
        real_files = os.path.normpath(self.path) + '/' + self.name_file
        with open(real_files, 'r', encoding='utf8') as ft:
            ft.readline()
            line = next(ft)
            line = line[:-1]
            secid, tradetime, price, quantity = line.split(',')
            self.name_ticker = secid
            self.min_price_tickers = float(price)
            self.max_price_tickers = float(price)
            for cnt, line in enumerate(ft):
                line = line[:-1]
                secid, tradetime, price, quantity = line.split(',')
                if self.min_price_tickers > float(price):
                    self.min_price_tickers = float(price)
                elif self.max_price_tickers < float(price):
                    self.max_price_tickers = float(price)
            self.half = (self.max_price_tickers + self.min_price_tickers) / 2
            self.volat = ((self.max_price_tickers - self.min_price_tickers) / self.half) * 100
        self.collector.put([self.name_ticker, self.volat])


def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()
        result = func(*args, **kwargs)
        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'Функция работала {elapsed} секунд(ы)')
        return result
    return surrogate


@time_track
def main():
    collector = multiprocessing.Queue()
    volants = [Ticker(file, collector=collector) for file in next_file_name()]
    tickers_data = {}
    for volant in volants:
        volant.start()
    for volant in volants:
        volant.join()

    while not collector.empty():
        data = collector.get()
        tickers_data[data[0]] = data[1]
    res_1 = sort_count_ticker(tickers_data)
    output_data(res_1)


if __name__ == '__main__':
    main()
