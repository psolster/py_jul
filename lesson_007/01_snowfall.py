# -*- coding: utf-8 -*-
from random import randint

import simple_draw as sd

_coordinats = []
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
        global _coordinats

        center_point = sd.get_point(self.coordinats[0], self.coordinats[1])
        sd.snowflake(center=center_point, length=10, color=flake.color)

    def move(self):
        center_point = sd.get_point(self.coordinats[0], self.coordinats[1])
        sd.snowflake(center=center_point, length=10, color=sd.background_color)
        flake.coordinats[1] = flake.coordinats[1] - 10

    def clear_previous_picture(self):
        sd.clear_screen()

    def can_fall(self):
        if flake.coordinats[1] > 20:
            return True

    def get_flakes(self, count=10):
        flakes_data = []
        for i in range(0, count):
            flakes_data.append([sd.random_number(0, 1201), sd.random_number(250, 600)])
            return flakes_data





flake = Snowflake()
# flake.coordinats = [sd.random_number(0, 1201), sd.random_number(250, 600)]
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
flakes = flake.get_flakes(count=10)  # создать список снежинок
while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        append_flakes(count=fallen_flakes)  # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
