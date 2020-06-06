# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)


sd.resolution = (1200, 600)
x_1 = 50
y_1 = 50
x_2 = 350
y_2 = 450

start_point = sd.get_point(x_1, y_1)
end_point = sd.get_point(x_2, y_2)
# TODO В условии задания, которое вы удалили можно было прочитать, что увеличивать координату y  не нужно.
for color in rainbow_colors:
    sd.line(start_point, end_point, color, 4)
    x_1 += 5
    y_1 += 5
    x_2 += 5
    y_2 += 5
    start_point = sd.get_point(x_1, y_1)
    end_point = sd.get_point(x_2, y_2)

# тут все и так понятно, не так интересно с примитивной графикой

sd.pause()
