# -*- coding: utf-8 -*-

import simple_draw as sd

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
        center_point = sd.get_point(flake.coordinats[0], flake.coordinats[1])
        sd.snowflake(center=center_point, length=10, color=sd.COLOR_WHITE)

    def move(self):
        flake.coordinats[1] = flake.coordinats[1] - 10

    def clear_previous_picture(self):
        center_point = sd.get_point(flake.coordinats[0], flake.coordinats[1])
        sd.snowflake(center=center_point, length=10, color=sd.background_color)

    def can_fall(self):
        if flake.coordinats[1] > 20:
            return True

    def get_flakes(self):
        flake.coordinats = []
        flake.coordinats.append(sd.random_number(0, 1201))
        flake.coordinats.append(sd.random_number(250, 600))
        return flake.coordinats


class Snowfall:

    def __init__(self):
        self.all_flakes_coord = []

    def snowfall_data(self, counter):
        for _ in range(0, counter):
            self.all_flakes_coord.append(flake.get_flakes())

    def get_fallen_flakes(self):
        down_snowflakes = []
        for i in range(0, len(self.all_flakes_coord)):
            if self.all_flakes_coord[i][1] < 20:
                down_snowflakes.append(i)
        return down_snowflakes

    def append_flakes(self, counts):
        counts.sort(reverse=True)
        for j in counts:
            center_point = sd.get_point(self.all_flakes_coord[j][0], self.all_flakes_coord[j][1])
            sd.snowflake(center=center_point, length=10, color=sd.background_color)
            flakes.all_flakes_coord.pop(j)
            flakes.all_flakes_coord.append([sd.random_number(0, 1201), sd.random_number(250, 600)])


# flake = Snowflake()
# flake.color = sd.COLOR_WHITE
# flake.get_flakes()
# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break
#
# sd.pause()

flake = Snowflake()
flakes = Snowfall()
count = 5
flakes.snowfall_data(counter=count)
while True:
    for index, (x, y) in enumerate(flakes.all_flakes_coord):
        flake.coordinats = [x, y]
        flake.clear_previous_picture()
        flake.move()
        flakes.all_flakes_coord[index] = flake.coordinats
        flake.draw()
        fallen = flakes.get_fallen_flakes()
        flakes.append_flakes(counts=fallen)
        if not flake.can_fall():
            break
        sd.sleep(0.02)
    if sd.user_want_exit():
        break
