# -*- coding: utf-8 -*-

# (определение функций)
import random

import simple_draw as sd


def smile(x: int, y: int, color):
    sd.resolution = (1200, 600)
    center = sd.get_point(x, y)
    left_eye = sd.get_point(x - 15, y + 10)
    right_eye = sd.get_point(x + 15, y + 10)
    x1 = x - 50
    y1 = y - 25
    x2 = x + 50
    y2 = y + 25
    left_bottom = sd.get_point(x1, y1)
    right_top = sd.get_point(x2, y2)
    right_top_mouth = sd.get_point(x - 15, y - 15)
    left_bottom_mouth = sd.get_point(x + 15, y - 10)

    sd.ellipse(left_bottom, right_top, color, 2)
    sd.circle(center, 5, color, 0)
    sd.circle(left_eye, 5, color, 1)
    sd.circle(right_eye, 5, color, 1)
    sd.rectangle(right_top_mouth, left_bottom_mouth, color, 1)


for _ in range(10):
    x = random.randint(100, 1200)
    y = random.randint(100, 600)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    smile(x, y, color)
sd.pause()
