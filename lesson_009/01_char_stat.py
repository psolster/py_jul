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
        self.sorted_alpha_count = {}
        self.alpha_count = {}

    def step_by_step(self):
        self.lenght_file()
        while self.count_lines != 0:
            symb_line = self.get_data(self.filename)
            self.count_symb_in_line(symb_line)
        self.sorted_alpha_count = self.sorter()

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
                count_dict = defaultdict(int)
                for char in data:
                    count_dict[char] += 1


            # # TODO Чтобы проверить является ли символ буквой лучше использовать
            # #  метод isalpha строковых объектов. Это позволит убрать повторяющиеся проверки.
            # #  Чтобы не делать проверку наличия ключа: if char in alpha_count.keys()
            # #  нужно заменить простой словарь alpha_count на collections.defaultdict.

    def sorter(self, revers=False):
        sorted_list = sorted(self.alpha_count.items(), key=operator.itemgetter(1), reverse=revers)
        # TODO Можно не собирать словарь через цикл, а использовать функцию dict, заменив
        #  self.sorted_alpha_count = dict(sorted(...))
        return {k: v for k, v in sorted_list}

    def print_rezults(self, norm_voc):
        print('+---------------+')
        print('|{mes1:^7}|{mes2:^7}|'.format(mes1='Буква', mes2='Кол-во'))
        print('+---------------+')
        for letter, count in norm_voc.items():
            print('|{letter:^6} | {count:6d}|'.format(letter=letter, count=count))
        print('+---------------+')
        print('|{mes1:^7}|{mes2:^7}|'.format(mes1='Итого', mes2=sum(norm_voc.values())))
        print('+---------------+')


file_name = 'voyna-i-mir.txt'
start = CountSymbol(file_name)
start.step_by_step()
res = start.sorter(revers=True)  # без аргумента - будет сортировка по возрастанию
start.print_rezults(res)

# TODO После исправления замечаний переходите ко второй части задания.
#  Постарайтесь сделать разные способы упорядояить статистику в виде
#  отдельных классов и не дублировать код.
# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
