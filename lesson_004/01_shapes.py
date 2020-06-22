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
sd.resolution = (1200, 800)
point_zer_triangle = sd.get_point(300, 300)
point_zer_kub = sd.get_point(80, 80)
point_zer_pent = sd.get_point(200, 200)
point_zer_hex = sd.get_point(400, 400)
dlinna = 80
angle = 0


def trianlge(point_zero_triangle, angle_tr, lenght_tri):
    v1 = sd.get_vector(start_point=point_zero_triangle, angle=angle_tr, length=lenght_tri, width=3)
    v1.draw()
    angle_tr += 120
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle_tr, length=lenght_tri, width=3)
    v2.draw()
    angle_tr += 120
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle_tr, length=lenght_tri, width=3)
    v3.draw()


def kub(point_zer_kub, angle, lenght):
    v1_kub = sd.get_vector(start_point=point_zer_kub, angle=angle, length=lenght, width=3)
    v1_kub.draw()
    angle += 90
    v2_kub = sd.get_vector(start_point=v1_kub.end_point, angle=angle, length=lenght, width=3)
    v2_kub.draw()
    angle += 90
    v3_kub = sd.get_vector(start_point=v2_kub.end_point, angle=angle, length=lenght, width=3)
    v3_kub.draw()
    angle += 90
    v4_kub = sd.get_vector(start_point=v3_kub.end_point, angle=angle, length=lenght, width=3)
    v4_kub.draw()


def pentakl(point_zer_pentakl, angle, lenght):
    v1_pentakl = sd.get_vector(start_point=point_zer_pentakl, angle=angle, length=lenght, width=3)
    v1_pentakl.draw()
    angle += 72
    v2_pentakl = sd.get_vector(start_point=v1_pentakl.end_point, angle=angle, length=lenght, width=3)
    v2_pentakl.draw()
    angle += 72
    v3_pentakl = sd.get_vector(start_point=v2_pentakl.end_point, angle=angle, length=lenght, width=3)
    v3_pentakl.draw()
    angle += 72
    v4_pentakl = sd.get_vector(start_point=v3_pentakl.end_point, angle=angle, length=lenght, width=3)
    v4_pentakl.draw()
    angle += 72
    sd.line(start_point=v4_pentakl.end_point, end_point=v1_pentakl.start_point, width=3)


def hexagon(point_zer_hex, angle, lenght):
    v1_hex = sd.get_vector(start_point=point_zer_hex, angle=angle, length=lenght, width=3)
    v1_hex.draw()
    angle += 60
    v2_hex = sd.get_vector(start_point=v1_hex.end_point, angle=angle, length=lenght, width=3)
    v2_hex.draw()
    angle += 60
    v3_hex = sd.get_vector(start_point=v2_hex.end_point, angle=angle, length=lenght, width=3)
    v3_hex.draw()
    angle += 60
    v4_hex = sd.get_vector(start_point=v3_hex.end_point, angle=angle, length=lenght, width=3)
    v4_hex.draw()
    angle += 60
    v5_hex = sd.get_vector(start_point=v4_hex.end_point, angle=angle, length=lenght, width=3)
    v5_hex.draw()
    angle += 60
    sd.line(start_point=v5_hex.end_point, end_point=v1_hex.start_point, width=3)


trianlge(point_zer_triangle, angle, dlinna)
kub(point_zer_kub, angle, dlinna)
pentakl(point_zer_pent, angle, dlinna)
hexagon(point_zer_hex, angle, dlinna)
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

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
