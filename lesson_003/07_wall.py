# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

sd.resolution = (1200, 600)
x_1 = 0
y_1 = 0
x_2 = 0
y_2 = 0
k = 0
color = sd.COLOR_ORANGE
start_point = sd.get_point(x_1, y_1)
end_point = sd.get_point(x_2, y_2)
for y in range(0, 551, 50):
    y_1 = y
    y_2 = y+50
    k += 1
    if k % 2:
        r = 0
    else:
        r = 50
    for x in range(r, 1251, 100):
        x_1 = x
        x_2 = x+100
        start_point = sd.get_point(x_1, y_1)
        end_point = sd.get_point(x_2, y_2)
        sd.rectangle(start_point, end_point, color, 2)



sd.pause()

# Зачёт!
