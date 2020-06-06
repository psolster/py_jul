# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)

point = sd.get_point(100, 100)
radius = 50
for _ in range(3):
    radius += 5
    sd.circle(center_position=point, radius=radius, width=2)


def buble(central_point, step_radius, color_bubl):
    start_radius = 50
    for _ in range(3):
        start_radius += step_radius
        # TODO Пузырьки рисуются неправильно. Они должны состоять из 3 окружностей.
        #  Для исправления передавайте в аргумент radius функции рисования окржности
        #  start_radius вместо radius.
        sd.circle(center_position=central_point, radius=radius, color=color_bubl, width=2)


point = sd.get_point(200, 200)
buble(central_point=point, step_radius=10, color_bubl=(40, 120, 200))

for x in range(100, 1100, 100):
    point = sd.get_point(x, 100)
    buble(central_point=point, step_radius=5, color_bubl=(40, 120, 200))


for y in range(100, 400, 100):
    for x in range(100, 1100, 100):
        point = sd.get_point(x, y)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        buble(central_point=point, step_radius=5, color_bubl=color)

point = sd.get_point(200, 200)


for _ in range(100):
    point = sd.random_point()
    step = random.randint(2, 20)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    buble(central_point=point, step_radius=step, color_bubl=color)

sd.pause()
