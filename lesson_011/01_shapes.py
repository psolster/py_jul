# -*- coding: utf-8 -*-

import simple_draw as sd


# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):
    def draw_fig(point_zero, fig_angle, element_lenght):
        angle_fig = []
        next_angle = fig_angle
        for j in range(0, n):
            delta_angle = 360 / n
            angle_fig.append(next_angle)
            next_angle += delta_angle
        v = sd.get_vector(start_point=point_zero, angle=angle_fig[0], length=element_lenght, width=3)
        v.draw()
        for i in range(1, n):
            v = sd.get_vector(start_point=v.end_point, angle=angle_fig[i], length=element_lenght, width=3)
            v.draw()

    return draw_fig


draw_triangle = get_polygon(n=3)
draw_triangle(sd.get_point(200, 200), 30, 200)
sd.pause()
