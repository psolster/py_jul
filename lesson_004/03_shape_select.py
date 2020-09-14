# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg



def trianlge(point_zero_fig, angle_figu, lenght_tri_fig, color='5'):
    angle_fig = [angle_figu + 0, angle + 120, angle + 240]
    v = sd.get_vector(start_point=point_zero_fig, angle=angle_fig[0], length=lenght_tri_fig, width=3)
    v.draw(color_maps[color])
    for i in range(1, 3):
        v = sd.get_vector(start_point=v.end_point, angle=angle_fig[i], length=lenght_tri_fig, width=3)
        v.draw(color_maps[color])


def kub(point_zero_fig, angle_figu, lenght_tri_fig, color="5"):
    angle_fig = [angle_figu + 0, angle + 90, angle + 180, angle + 270]
    v = sd.get_vector(start_point=point_zero_fig, angle=angle_fig[0], length=lenght_tri_fig, width=3)
    v.draw(color_maps[color])
    for i in range(1, 4):
        v = sd.get_vector(start_point=v.end_point, angle=angle_fig[i], length=lenght_tri_fig, width=3)
        v.draw(color_maps[color])


def pentakl(point_zero_fig, angle_figu, lenght_tri_fig, color="5"):
    angle_fig = [angle_figu + 0, angle + 72, angle + 144, angle + 144 + 72, angle + 144 + 72 + 72]
    v = sd.get_vector(start_point=point_zero_fig, angle=angle_fig[0], length=lenght_tri_fig, width=3)
    v.draw(color_maps[color])
    for i in range(1, 5):
        v = sd.get_vector(start_point=v.end_point, angle=angle_fig[i], length=lenght_tri_fig, width=3)
        v.draw(color_maps[color])


def hexagon(point_zero_fig, angle_figu, lenght_tri_fig, color="5"):
    angle_fig = [angle_figu + 0, angle + 60, angle + 120, angle + 180, angle + 240, angle + 300]
    v = sd.get_vector(start_point=point_zero_fig, angle=angle_fig[0], length=lenght_tri_fig, width=3)
    v.draw(color_maps[color])
    for i in range(1, 6):
        v = sd.get_vector(start_point=v.end_point, angle=angle_fig[i], length=lenght_tri_fig, width=3)
        v.draw(color_maps[color])


sd.resolution = (600, 600)
point_zero = sd.get_point(300, 300)
lenght = 120
angle = 0


color_maps = {'1': sd.COLOR_RED,
              '2': sd.COLOR_ORANGE,
              '3': sd.COLOR_YELLOW,
              '4': sd.COLOR_GREEN,
              '5': sd.COLOR_CYAN,
              '6': sd.COLOR_BLUE,
              '7': sd.COLOR_PURPLE
              }


draw_function = {'1': ['треугольник', trianlge],
                 '2': ['Куб', kub],
                 '3': ['Пятиугольник', pentakl],
                 '4': ['Шестиугольник', hexagon]}

for key, value in draw_function.items():
    print(key, value[0])

a = input('Укажите № желаемого цвета фигуры. Цвета на выбор: Ваш выбор-> ')

if a in draw_function:
    start_function = draw_function[a][1]
    start_function(point_zero_fig=point_zero, angle_figu=angle, lenght_tri_fig=lenght)
else:
    print('ну не попал в нужный')
    exit()
sd.pause()

# Зачёт!
