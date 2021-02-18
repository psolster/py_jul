# -*- coding: utf-8 -*-

import os
import time
import shutil

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени последней модификации файла
# (время создания файла берется по разному в разых ОС - см https://clck.ru/PBCAX - поэтому берем время модификации).
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником ОС в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит, см .gitignore в папке ДЗ)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4


from collections import defaultdict


class SortFilesInFolder:

    def __init__(self, path, target_path):
        self.voc_name_files_in_dir = defaultdict(str)
        self.voc_new_path = defaultdict(str)
        self.path = path
        self.target_path = target_path
        self.list_of_filename = []
        os.path.normpath(self.path)

    def work_plane(self):
        list_names = self.list_file_name()
        self.create_new_path_and_copy(list_names)

    def list_file_name(self):
        for dirpath, dirnames, filenames in os.walk(self.path):
            for filename in filenames:
                self.list_of_filename.append(filename)
            self.voc_name_files_in_dir[str(dirpath)] = self.list_of_filename
            self.list_of_filename = []
        return self.voc_name_files_in_dir

    def create_new_path_and_copy(self, enter_data):
        for path, names_list in enter_data.items():
            curent_path = path
            if len(names_list) != 0:
                for name_file in names_list:
                    # TODO Добавлять \\ к пути не нужно. os.path.join добавит разделитель,
                    #  подходящий к ОС, в которой запускается программа.
                    #  Нужно убрать '\\' здесь и ниже.
                    fulL_names = os.path.join(curent_path + '\\', name_file)
                    mtime = os.path.getmtime(fulL_names)
                    date_str = time.ctime(mtime)
                    added = date_str[20:24] + '\\' + date_str[4:7] + '\\'
                    path_for_copy_this_file = os.path.join(target_path + '\\', added)
                    if not os.path.isdir(path_for_copy_this_file):
                        os.makedirs(path_for_copy_this_file)
                        shutil.copy2(os.path.join(path + '\\', name_file), path_for_copy_this_file)
                    else:
                        shutil.copy2(os.path.join(path + '\\', name_file), path_for_copy_this_file)

# TODO Для корректной работы задания достаточно будет указать пити вида icons и icons_by_year.
path = "C:\\Users\\kampa\\PycharmProjects\\python_base\\lesson_009"
path = os.path.normpath(path)
target_path = "C:\\Users\\kampa\\PycharmProjects\\python_base\\lesson_009\\icons_by_year"
target_path = os.path.normpath(target_path)
sort = SortFilesInFolder(path=path, target_path=target_path)
sort.work_plane()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Это относится только к чтению файлов в архиве. В случае паттерна "Шаблонный метод" изменяется способ
# получения данных (читаем os.walk() или zip.namelist и т.д.)
# Документация по zipfile: API https://docs.python.org/3/library/zipfile.html
