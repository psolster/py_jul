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
from collections import defaultdict


class Treader:
    def __init__(self, path):
        self.path = path
        self.count_ticker = defaultdict(str)

    def run(self):
        list_files = self.read_names_of_files(self.path)
        data = self.read_each_files(list_files)
        res = self.res_calc(data)
        res_sort = self.sort_count_ticker(res)
        self.output_data(res_sort)

    def read_names_of_files(self, path):
        files = os.listdir(path=path)
        return files

    def read_each_files(self, list_files):
        for tikcer in list_files:
            list_price = []
            files_for_open = self.path + '/' + tikcer
            # TODO Можно воспользоваться знанием о том, что файл является итерируемым объектом
            #  и сначала считать не сохраняя первую строку с заголовками, а потом
            #  первую строку с данными, из которой можно получить название тикера и начальное
            #  значение цены для price_min и price_max. Получить следующий элемент итерируемого
            #  объекта можно, используя функцию next:
            #  line = next(file)
            with open(files_for_open, 'r', encoding='utf8') as ff:
                for line in ff:
                    prov = line[:5]
                    if prov.isalpha():
                        continue
                    else:
                        self.secid, self.tradetime, self.price, self.quantity = line.split(',')
                        list_price.append(float(self.price))
                if len(list_price) <= 1:
                    print(f'По тикеру {self.secid} недостаточно данных')
                else:
                    list_price.sort()
                half_sum = (list_price[0] + list_price[-1]) / 2
                volatility = ((list_price[-1] - list_price[0]) / half_sum) * 100
                yield self.secid, volatility

    def res_calc(self, data):
        self.number_ticker = 1
        for ticer, volat in data:
            self.number_ticker += 1
            self.count_ticker[ticer] = volat
        return self.count_ticker

    def sort_count_ticker(self, data):
        sorted_tuple = sorted(data.items(), key=operator.itemgetter(1))
        dict(sorted_tuple)
        return sorted_tuple

    def output_data(self, dic):
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


path = 'trades'
start = Treader(path=path)
start.run()

# TODO Класс тикера должен отвечать за обработку одного файла и в нём обязательно
#  должен быть метод run().
#  Получение списка файлов и цикл по ним нужно сделать либо в ещё одном классе,
#  либо в функции. Должно получиться что-то подобное:
#  tickers_data = {}
#  for file in files:
#      ticker = Ticker(file)
#      ticker.run()
#      tickers_data[ticker.name] = ticker.volatility
