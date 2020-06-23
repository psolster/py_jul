# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

sd.resolution = (600, 600)
point_zer_triangle = sd.get_point(300, 300)
point_zer_kub = sd.get_point(300, 300)
point_zer_pent = sd.get_point(300, 300)
point_zer_hex = sd.get_point(300, 300)
dlinna_vector = 120
angle = 0

color_maps = {1: (255, 0, 0),
              2: (255, 127, 0),
              3: (255, 255, 0),
              4: (0, 255, 0),
              5: (0, 255, 255),
              6: (0, 0, 255),
              7: (255, 0, 255)
              }


def trianlge(point_zero, angle_tr, lenght_tri, line_color):
    color = color_maps[line_color]
    v1 = sd.get_vector(start_point=point_zero, angle=angle_tr, length=lenght_tri, width=3)
    v1.draw(color=color)
    angle_tr += 120
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle_tr, length=lenght_tri, width=3)
    v2.draw(color=color)
    angle_tr += 120
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle_tr, length=lenght_tri, width=3)
    v3.draw(color=color)


def kub(point_zer, angle_kub, lenght, line_color):
    color = color_maps[line_color]
    v1_kub = sd.get_vector(start_point=point_zer, angle=angle_kub, length=lenght, width=3)
    v1_kub.draw(color=color)
    angle_kub += 90
    v2_kub = sd.get_vector(start_point=v1_kub.end_point, angle=angle_kub, length=lenght, width=3)
    v2_kub.draw(color=color)
    angle_kub += 90
    v3_kub = sd.get_vector(start_point=v2_kub.end_point, angle=angle_kub, length=lenght, width=3)
    v3_kub.draw(color=color)
    angle_kub += 90
    v4_kub = sd.get_vector(start_point=v3_kub.end_point, angle=angle_kub, length=lenght, width=3)
    v4_kub.draw(color=color)


def pentakl(point_zer, angle_pent, lenght, line_color):
    color = color_maps[line_color]
    v1_pentakl = sd.get_vector(start_point=point_zer, angle=angle_pent, length=lenght, width=3)
    v1_pentakl.draw(color=color)
    angle_pent += 72
    v2_pentakl = sd.get_vector(start_point=v1_pentakl.end_point, angle=angle_pent, length=lenght, width=3)
    v2_pentakl.draw(color=color)
    angle_pent += 72
    v3_pentakl = sd.get_vector(start_point=v2_pentakl.end_point, angle=angle_pent, length=lenght, width=3)
    v3_pentakl.draw(color=color)
    angle_pent += 72
    v4_pentakl = sd.get_vector(start_point=v3_pentakl.end_point, angle=angle_pent, length=lenght, width=3)
    v4_pentakl.draw(color=color)
    angle_pent += 72
    sd.line(start_point=v4_pentakl.end_point, end_point=v1_pentakl.start_point, width=3, color=color)


def hexagon(point_zer, angle_hex, lenght, line_color):
    color = color_maps[line_color]
    v1_hex = sd.get_vector(start_point=point_zer, angle=angle_hex, length=lenght, width=3)
    v1_hex.draw(color=color)
    angle_hex += 60
    v2_hex = sd.get_vector(start_point=v1_hex.end_point, angle=angle_hex, length=lenght, width=3)
    v2_hex.draw(color=color)
    angle_hex += 60
    v3_hex = sd.get_vector(start_point=v2_hex.end_point, angle=angle_hex, length=lenght, width=3)
    v3_hex.draw(color=color)
    angle_hex += 60
    v4_hex = sd.get_vector(start_point=v3_hex.end_point, angle=angle_hex, length=lenght, width=3)
    v4_hex.draw(color=color)
    angle_hex += 60
    v5_hex = sd.get_vector(start_point=v4_hex.end_point, angle=angle_hex, length=lenght, width=3)
    v5_hex.draw(color=color)
    angle_hex += 60
    sd.line(start_point=v5_hex.end_point, end_point=v1_hex.start_point, width=3, color=color)


a = int(input('''Укажите № желаемой фигуры. Фигуры на выбор:
      1. Трегольник
      2. Квадрат
      3. 5-ти угольник
      4. 6-ти угольник
      
Ваш выбор-> '''))
if a == 1:
    trianlge(point_zero=point_zer_triangle, angle_tr=angle, lenght_tri=dlinna_vector, line_color=a)
elif a == 2:
    kub(point_zer=point_zer_kub, angle_kub=angle, lenght=dlinna_vector, line_color=a)
elif a == 3:
    pentakl(point_zer=point_zer_pent, angle_pent=angle, lenght=dlinna_vector, line_color=a)
elif a == 4:
    hexagon(point_zer=point_zer_hex, angle_hex=angle, lenght=dlinna_vector, line_color=a)
else:
    print('ну не попал в нужный')
    exit()
sd.pause()


