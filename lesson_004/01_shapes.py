# -*- coding: utf-8 -*-

import simple_draw as sd


# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Примерный алгоритм внутри функции:
#   # будем рисовать с помощью векторов, каждый следующий - из конечной точки предыдущего
#   текущая_точка = начальная точка
#   для угол_наклона из диапазона от 0 до 360 с шагом XXX
#      # XXX подбирается индивидуально для каждой фигуры
#      составляем вектор из текущая_точка заданной длины с наклоном в угол_наклона
#      рисуем вектор
#      текущая_точка = конечной точке вектора
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg


# def trianlge(point_zero, angle_tr, lenght_tri):
#     angle_fig = [angle_tr + 0, angle_tr + 120, angle_tr + 240]
#     v = sd.get_vector(start_point=point_zero, angle=angle_fig[0], length=lenght_tri, width=3)
#     v.draw()
#     for i in range(1, 3):
#         v = sd.get_vector(start_point=v.end_point, angle=angle_fig[i], length=lenght_tri, width=3)
#         v.draw()
#
#
# def kub(point_zero, angle_kub, lenght):
#     angle_fig = [angle_kub + 0, angle_kub + 90, angle_kub + 180, angle_kub + 270]
#     v = sd.get_vector(start_point=point_zero, angle=angle_fig[0], length=lenght, width=3)
#     v.draw()
#     for i in range(1, 4):
#         v = sd.get_vector(start_point=v.end_point, angle=angle_fig[i], length=lenght, width=3)
#         v.draw()
#
#
# def pentakl(point_zero, angle_pent, lenght):
#     angle_fig = [angle_pent + 0, angle_pent + 72, angle_pent + 144, angle_pent + 144 + 72, angle_pent + 144 + 72 + 72]
#     v = sd.get_vector(start_point=point_zero, angle=angle_fig[0], length=lenght, width=3)
#     v.draw()
#     for i in range(1, 5):
#         v = sd.get_vector(start_point=v.end_point, angle=angle_fig[i], length=lenght, width=3)
#         v.draw()
#
#
# def hexagon(point_zero, angle_hex, lenght):
#     angle_fig = [angle_hex + 0, angle_hex + 60, angle_hex + 120, angle_hex + 180, angle_hex + 240, angle_hex + 300]
#     v = sd.get_vector(start_point=point_zero, angle=angle_fig[0], length=lenght, width=3)
#     v.draw()
#     for i in range(1, 6):
#         v = sd.get_vector(start_point=v.end_point, angle=angle_fig[i], length=lenght, width=3)
#         v.draw()
#
#
sd.resolution = (1200, 800)
# point_zer_triangle = sd.get_point(300, 300)
# point_zer_kub = sd.get_point(80, 80)
# point_zer_pent = sd.get_point(200, 200)
# point_zer_hex = sd.get_point(400, 400)
# dlinna_vector = 80
# angle = 45
#
# trianlge(point_zero=point_zer_triangle, angle_tr=angle, lenght_tri=dlinna_vector)
# kub(point_zero=point_zer_kub, angle_kub=angle, lenght=dlinna_vector)
# pentakl(point_zero=point_zer_pent, angle_pent=angle, lenght=dlinna_vector)
# hexagon(point_zero=point_zer_hex, angle_hex=angle, lenght=dlinna_vector)
# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв в начальной/конечной точках рисуемой фигуры
# (если он есть. подсказка - на последней итерации можно использовать линию от первой точки)


def draw_fig(point_zero, fig_angle, element_lenght, number_vectors):
    angle_fig = []
    next_angle = fig_angle
    for j in range(0, number_vectors):
        delta_angle = 360/number_vectors

        angle_fig.append(next_angle)
        next_angle += delta_angle

    v = sd.get_vector(start_point=point_zero, angle=angle_fig[0], length=element_lenght, width=3)
    v.draw()
    for i in range(1, number_vectors):
        v = sd.get_vector(start_point=v.end_point, angle=angle_fig[i], length=element_lenght, width=3)
        v.draw()


def triangle(point_zero, angle_dir, lenght):
    n = 3
    draw_fig(point_zero=point_zero, fig_angle=angle_dir, element_lenght=lenght, number_vectors=n)


def kub(point_zero, angle_dir, lenght):
    n = 4
    draw_fig(point_zero=point_zero, fig_angle=angle_dir, element_lenght=lenght, number_vectors=n)


def pent(point_zero, angle_dir, lenght):
    n = 5
    draw_fig(point_zero=point_zero, fig_angle=angle_dir, element_lenght=lenght, number_vectors=n)


def hexagon(point_zero, angle_dir, lenght):
    n = 6
    draw_fig(point_zero=point_zero, fig_angle=angle_dir, element_lenght=lenght, number_vectors=n)


point_zer_triangle = sd.get_point(300, 300)
point_zer_kub = sd.get_point(80, 80)
point_zer_pent = sd.get_point(200, 200)
point_zer_hex = sd.get_point(400, 400)
dlinna_vector = 80
angle = 0

triangle(point_zero=point_zer_triangle, angle_dir=angle, lenght=dlinna_vector)
kub(point_zero=point_zer_kub, angle_dir=angle, lenght=dlinna_vector)
pent(point_zero=point_zer_pent, angle_dir=angle, lenght=dlinna_vector)
hexagon(point_zero=point_zer_hex, angle_dir=angle, lenght=dlinna_vector)


# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()

# Зачёт!
