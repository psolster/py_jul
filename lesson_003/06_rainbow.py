# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)

sd.resolution = (1200, 600)
x_1 = 50
y_1 = 50
x_2 = 350
y_2 = 450

start_point = sd.get_point(x_1, y_1)
end_point = sd.get_point(x_2, y_2)
for color in rainbow_colors:
    sd.line(start_point, end_point, color, 4)
    x_1 += 5
    y_1 += 5
    x_2 += 5
    y_2 += 5
    start_point = sd.get_point(x_1, y_1)
    end_point = sd.get_point(x_2, y_2)

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код

sd.pause()
