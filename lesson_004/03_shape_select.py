# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg
COLOR_RED = sd.COLOR_RED
COLOR_ORANGE = sd.COLOR_ORANGE
COLOR_YELLOW = sd.COLOR_YELLOW
COLOR_GREEN = sd.COLOR_GREEN
COLOR_CYAN = sd.COLOR_CYAN
COLOR_BLUE = sd.COLOR_BLUE
COLOR_PURPLE = sd.COLOR_PURPLE

# TODO Обратите внимание на предупреждение среды разработки о том, что внутри функции используются те же имена
#  переменных, что и вне ее. Здесь это не критично но в других случаях может вызвать ошибки.


def trianlge(point_zero, angle, lenght_tri, color='5'):
    angle_fig = [angle + 0, angle + 120, angle + 240]
    v = sd.get_vector(start_point=point_zero, angle=angle_fig[0], length=lenght_tri, width=3)
    v.draw(color_maps[color])
    for i in range(1, 3):
        v = sd.get_vector(start_point=v.end_point, angle=angle_fig[i], length=lenght_tri, width=3)
        v.draw(color_maps[color])


def kub(point_zero, angle, lenght, color="5"):
    angle_fig = [angle + 0, angle + 90, angle + 180, angle + 270]
    v = sd.get_vector(start_point=point_zero, angle=angle_fig[0], length=lenght, width=3)
    v.draw(color_maps[color])
    for i in range(1, 4):
        v = sd.get_vector(start_point=v.end_point, angle=angle_fig[i], length=lenght, width=3)
        v.draw(color_maps[color])


def pentakl(point_zero, angle, lenght, color="5"):
    angle_fig = [angle + 0, angle + 72, angle + 144, angle + 144 + 72, angle + 144 + 72 + 72]
    v = sd.get_vector(start_point=point_zero, angle=angle_fig[0], length=lenght, width=3)
    v.draw(color_maps[color])
    for i in range(1, 5):
        v = sd.get_vector(start_point=v.end_point, angle=angle_fig[i], length=lenght, width=3)
        v.draw(color_maps[color])


def hexagon(point_zero, angle, lenght, color="5"):
    angle_fig = [angle + 0, angle + 60, angle + 120, angle + 180, angle + 240, angle + 300]
    v = sd.get_vector(start_point=point_zero, angle=angle_fig[0], length=lenght, width=3)
    v.draw(color_maps[color])
    for i in range(1, 6):
        v = sd.get_vector(start_point=v.end_point, angle=angle_fig[i], length=lenght, width=3)
        v.draw(color_maps[color])


sd.resolution = (600, 600)
point_zero = sd.get_point(300, 300)
lenght = 120
angle = 0


color_maps = {'1': COLOR_RED,
              '2': COLOR_ORANGE,
              '3': COLOR_YELLOW,
              '4': COLOR_GREEN,
              '5': COLOR_CYAN,
              '6': COLOR_BLUE,
              '7': COLOR_PURPLE
              }

# TODO Преобразуйте список all_forms в словарь с номерами фигур в ключах и
#  названиями фигур и ссылками на функции в значениях.

draw_function = {'1': trianlge, '2': kub, '3': pentakl, '4': hexagon}
a = input('''Укажите № желаемой фигуры. Фигуры на выбор:
      1. Трегольник
      2. Квадрат
      3. 5-ти угольник
      4. 6-ти угольник
      
Ваш выбор-> ''')


if a in draw_function:
    start_function = draw_function[a]
    start_function(point_zero, angle, lenght)
else:
    print('ну не попал в нужный')
    exit()
sd.pause()
