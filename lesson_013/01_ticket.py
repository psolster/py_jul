# -*- coding: utf-8 -*-


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru
from PIL import Image, ImageDraw, ImageFont, ImageColor
import os

path = 'images'
file_name = 'ticket_template.png'


def make_ticket(fio, from_, to_, data_):
    path_n = os.getcwd()
    real_path = os.path.join(path_n, path)
    font_path_r = os.path.join(path_n, '_J_EKR.ttf')
    os.chdir(real_path)
    my_ticket_templ = Image.open(file_name)
    my_ticket_templ.load()
    draw = ImageDraw.Draw(my_ticket_templ)
    font = ImageFont.truetype(font_path_r, size=26)
    message_fio = f'{fio}'
    message_from_ = f'{from_}'
    message_to_ = f'{to_}'
    message_data_ = f'{data_}'
    draw.text((45, 122), message_fio, font=font, fill=ImageColor.colormap['black'])
    draw.text((45, 190), message_from_, font=font, fill=ImageColor.colormap['black'])
    draw.text((45, 258), message_to_, font=font, fill=ImageColor.colormap['black'])
    draw.text((270, 258), message_data_, font=font, fill=ImageColor.colormap['black'])
    my_ticket_templ.show()


make_ticket('Ястребов Л.Б.', 'Moscow', 'Prostokvasheno', '30.04')

# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля argparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.
