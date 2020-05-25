# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)

point = sd.get_point(100, 100)
radius = 50
for _ in range(3):
    radius += 5
    sd.circle(center_position=point, radius=radius, width=2)


# TODO Обратите внимание на предупреждение среды разработки о том, что внутри функции используются те же имена
#  переменных, что и вне ее. Здесь это не критично но в других случаях может вызвать ошибки.
def buble(point, step, color):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, color=color, width=2)


point = sd.get_point(200, 200)
buble(point=point, step=10, color=(40, 120, 200))

for x in range(100, 1100, 100):
    point = sd.get_point(x, 100)
    buble(point=point, step=5, color=(40, 120, 200))


for y in range(100, 400, 100):
    for x in range(100, 1100, 100):
        point = sd.get_point(x, y)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        buble(point=point, step=5, color=color)

point = sd.get_point(200, 200)


for _ in range(100):
    point = sd.random_point()
    step = random.randint(2, 20)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    buble(point=point, step=step, color=color)

sd.pause()
