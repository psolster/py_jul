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
voc_name_files_in_dir = defaultdict(str)
path = "C:\\Users\\kampa\\PycharmProjects\\python_base\\lesson_009\\icons\\"
os.path.normpath(path)
list_of_filename = []
if not os.path.isdir("icons_by_year"):
     os.mkdir("icons_by_year")
for dirpath, dirnames, filenames in os.walk(path):
    current_file = os.path.join(str(dirpath), str(filenames))
    # print(current_file)
    for filename in filenames:

        list_of_filename.append(filename)
    voc_name_files_in_dir[str(dirpath)] = list_of_filename
    list_of_filename = []

for path, names_list in voc_name_files_in_dir.items():
    curent_path = path
    if len(names_list) != 0:
        for name_file in names_list:
            fulL_names = curent_path + '\\'+name_file
            mtime = os.path.getmtime(fulL_names)
            print(time.ctime(mtime))

for key, list in voc_name_files_in_dir.items():
    print(key, ': ', list)



# real_path = os.getcwd()
# mtime = os.path.getmtime(real_path)
# print(time.ctime(mtime))

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Это относится только к чтению файлов в архиве. В случае паттерна "Шаблонный метод" изменяется способ
# получения данных (читаем os.walk() или zip.namelist и т.д.)
# Документация по zipfile: API https://docs.python.org/3/library/zipfile.html
