# -*- coding: utf-8 -*-
from random import randint

import simple_draw as sd

# coordinats = []
sd.resolution = (1200, 600)


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

    def __init__(self):
        self.coordinats = []
        self.color = 'sd.COLOR_WHITE'

    def draw(self):
        for index, (x, y) in enumerate(flake.coordinats):
            center_point = sd.get_point(x, y)
            sd.snowflake(center=center_point, length=10, color=flake.color)

    def move(self):
        for index in range(0, len(flake.coordinats)):
            flake.coordinats[index][1] = flake.coordinats[index][1] - 10

    def clear_previous_picture(self):
        for index, (x, y) in enumerate(flake.coordinats):
            center_point = sd.get_point(x, y)
            sd.snowflake(center=center_point, length=10, color=sd.background_color)

    def can_fall(self):
        if flake.coordinats[1] > 20:
            return True

    def get_flakes(self, count=10):

        for i in range(0, count):
            flake.coordinats.append([sd.random_number(0, 1201), sd.random_number(250, 600)])
        return flake.coordinats

    def get_fallen_flakes(self):
        down_snowflakes = []
        for i in range(0, len(flake.coordinats)):
            if flake.coordinats[i][1] < 20:
                down_snowflakes.append(i)
        return down_snowflakes

    def append_flakes(self, count):
        count.sort(reverse=True)
        for j in count:
            center_point = sd.get_point(flake.coordinats[j][0], flake.coordinats[j][1])
            sd.snowflake(center=center_point, length=10, color=sd.background_color)
            flake.coordinats.pop(j)
            flake.coordinats.append([sd.random_number(0, 1201), sd.random_number(250, 600)])


# TODO Коасс снежинки должен реализовывать поведение одной снежинки: рисование
#  цветом и фоном, перемещение, упала ли снежинка. Класс снежинки не должен
#  содержать методов создания, добавления нескольких снежинок и подсчёт упавших.
#  Для организации снегоапда нужно или сделать отдельный класс или перенести
#  функции из класса в модуль.


flake = Snowflake()
flake.color = sd.COLOR_BLUE

# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
flakes = flake.get_flakes(count=5)  # создать список снежинок
while True:
    for _ in range(0, len(flakes)):
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
        fallen_flakes = flake.get_fallen_flakes()  # подчитать сколько снежинок уже упало
        if fallen_flakes:
            flake.append_flakes(count=fallen_flakes)  # добавить еще сверху
        sd.sleep(0.05)
        if sd.user_want_exit():
            break
sd.pause()
