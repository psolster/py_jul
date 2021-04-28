# -*- coding: utf-8 -*-


# Описание предметной области:
#
# При торгах на бирже совершаются сделки - один купил, второй продал.
# Покупают и продают ценные бумаги (акции, облигации, фьючерсы, етс). Ценные бумаги - это по сути долговые расписки.
# Ценные бумаги выпускаются партиями, от десятка до несколько миллионов штук.
# Каждая такая партия (выпуск) имеет свой торговый код на бирже - тикер - https://goo.gl/MJQ5Lq
# Все бумаги из этой партии (выпуска) одинаковы в цене, поэтому говорят о цене одной бумаги.
# У разных выпусков бумаг - разные цены, которые могут отличаться в сотни и тысячи раз.
# Каждая биржевая сделка характеризуется:
#   тикер ценнной бумаги
#   время сделки
#   цена сделки
#   обьем сделки (сколько ценных бумаг было куплено)
#
# В ходе торгов цены сделок могут со временем расти и понижаться. Величина изменения цен называтея волатильностью.
# Например, если бумага №1 торговалась с ценами 11, 11, 12, 11, 12, 11, 11, 11 - то она мало волатильна.
# А если у бумаги №2 цены сделок были: 20, 15, 23, 56, 100, 50, 3, 10 - то такая бумага имеет большую волатильность.
# Волатильность можно считать разными способами, мы будем считать сильно упрощенным способом -
# отклонение в процентах от полусуммы крайних значений цены за торговую сессию:
#   полусумма = (максимальная цена + минимальная цена) / 2
#   волатильность = ((максимальная цена - минимальная цена) / полусумма) * 100%
# Например для бумаги №1:
#   half_sum = (12 + 11) / 2 = 11.5
#   volatility = ((12 - 11) / half_sum) * 100 = 8.7%
# Для бумаги №2:
#   half_sum = (100 + 3) / 2 = 51.5
#   volatility = ((100 - 3) / half_sum) * 100 = 188.34%
#
# В реальности волатильность рассчитывается так: https://goo.gl/VJNmmY
#
# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью.
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
# Подготовка исходных данных
# 1. Скачать файл https://drive.google.com/file/d/1l5sia-9c-t91iIPiGyBc1s9mQ8RgTNqb/view?usp=sharing
#       (обратите внимание на значок скачивания в правом верхнем углу,
#       см https://drive.google.com/file/d/1M6mW1jI2RdZhdSCEmlbFi5eoAXOR3u6G/view?usp=sharing)
# 2. Раззиповать средствами операционной системы содержимое архива
#       в папку python_base/lesson_012/trades
# 3. В каждом файле в папке trades содержится данные по сделакам по одному тикеру, разделенные запятыми.
#   Первая строка - название колонок:
#       SECID - тикер
#       TRADETIME - время сделки
#       PRICE - цена сделки
#       QUANTITY - количество бумаг в этой сделке
#   Все последующие строки в файле - данные о сделках
#
# Подсказка: нужно последовательно открывать каждый файл, вычитывать данные, высчитывать волатильность и запоминать.
# Вывод на консоль можно сделать только после обработки всех файлов.
#
# Для плавного перехода к мультипоточности, код оформить в обьектном стиле, используя следующий каркас
#
# class <Название класса>:
#
#     def __init__(self, <параметры>):
#         <сохранение параметров>
#
#     def run(self):
#         <обработка данных>
import operator
import os
import time

path = 'trades'


def read_dir(path):
    files = os.listdir(path=path)
    return files


def next_file_name():
    list_files = read_dir(path=path)
    for name_files in list_files:
        yield str(name_files)


def sort_count_ticker(data):
    sorted_tuple = sorted(data.items(), key=operator.itemgetter(1))
    dict(sorted_tuple)
    return sorted_tuple


def output_data(dic):
    index = 0
    name_zero_tick = []
    volat_list = list(dic)
    max_volat = list(dic)[-1:-4:-1]
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


def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()

        result = func(*args, **kwargs)

        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'Функция работала {elapsed} секунд(ы)')
        return result

    return surrogate


class Ticker:
    def __init__(self, next_file):
        self.name_file = next_file
        self.min_price_tickers = 0
        self.max_price_tickers = 0
        self.half = 0
        self.volat = 0
        self.path = path

    def run(self):
        real_files = os.path.normpath(self.path) + '/' + self.name_file
        with open(real_files, 'r', encoding='utf8') as ft:
            # TODO В следующей строке присваивать переменную не нужно.
            line = ft.readline()
            line = next(ft)
            line = line[:-1]
            secid, tradetime, price, quantity = line.split(',')
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
        return secid, self.volat

@time_track
def start():
    files = next_file_name()
    tickers_data = {}
    for file in files:
        ticker = Ticker(file)
        data = ticker.run()
        tickers_data[data[0]] = data[1]
    res_1 = sort_count_ticker(tickers_data)
    output_data(res_1)

start()

# TODO Исправьте оформление кода и замечания среды разработки.
