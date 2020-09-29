import random

import simple_draw as sd


def smile(coordinat_centr, color_smile):

    sd.resolution = (1200, 600)
    center = sd.get_point(*coordinat_centr)
    left_eye = sd.get_point(coordinat_centr[0] - 15, coordinat_centr[1] + 10)
    right_eye = sd.get_point(coordinat_centr[0] + 15, coordinat_centr[1] + 10)
    x1 = coordinat_centr[0] - 50
    y1 = coordinat_centr[1] - 25
    x2 = coordinat_centr[0] + 50
    y2 = coordinat_centr[1] + 25
    left_bottom = sd.get_point(x1, y1)
    right_top = sd.get_point(x2, y2)
    right_top_mouth = sd.get_point(coordinat_centr[0] - 15, coordinat_centr[1] - 15)
    left_bottom_mouth = sd.get_point(coordinat_centr[0] + 15, coordinat_centr[1] - 10)

    sd.ellipse(left_bottom, right_top, color_smile, 2)
    sd.circle(center, 5, color_smile, 0)
    sd.circle(left_eye, 5, color_smile, 1)
    sd.circle(right_eye, 5, color_smile, 1)
    sd.rectangle(right_top_mouth, left_bottom_mouth, color_smile, 1)


if __name__ == "__main__":
    for _ in range(10):
        coordin = (random.randint(0, 1200), random.randint(0, 600))
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        smile(coordinat_centr=coordin, color_smile=color)
    sd.pause()
