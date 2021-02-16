# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shзыщдandrinov/python_base_snippets/snippets/4
import operator
from collections import defaultdict


class CountSymbol:

    def __init__(self, filename):
        self.filename = filename
        self.count_lines = 0
        self.position_on_files = 0
        self.count_dict = defaultdict(int)

    def step_by_step(self):
        self.lenght_file()
        while self.count_lines != 0:
            symb_line = self.get_data(self.filename)
            self.count_symb_in_line(symb_line)
        self.count_dict = self.sorter()

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

    def count_symb_in_line(self, data):
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


# TODO  Задание получилось хорошо. Давайте сделаем одну небольшую оптимизацию.
#  Методы сортировки у всех классов сортировки отличаются
#  только двумя параметрами:
#  - индекс в operator.itemgetter 0 или 1
#  - порядок сортировки reverse True или False.
#  Можно сделать эти параметры переменными класса и использовать
#  их внутри функции сортировки, а саму функцию сортировки перенести в общий класс.
#  Тогда в классах наследниках достаточно будет менять только
#  две переменные для реализации всех типов сортировки.

# TODO Пример с демонстрацией отличия переменных класса от переменных экземпляра:
#
#  class MainClass:
#     variable1 = 0  # Это переменная класса
#
#      def __init__():
#           variable2 = 1  #  Это переменная экземпляра.
#
#      def run(self):
#          print(self.variable1)  # Обращаться к переменным класса можно через self
#
#  В результате должно получиться что-то подобное:
# class MainClass:
#     variable1 = 1
#
#     def __init__()
#         ...
#
# class Aggregation1(MainClass):
#     variable1 = 2
#
# class Aggregation2(MainClass):
#     variable1 = 3


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


# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
