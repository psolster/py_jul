import random

import simple_draw as sd
from lesson_005.graph_pack import smile

sd.resolution = (1200, 600)


def human(center_body, color_human):
    smile.smile(coordinat_centr=center_body, color_smile=color_human)
    left_bottom_body = sd.get_point(center_body[0] - 20, center_body[1] - 100)
    right_top_body = sd.get_point(center_body[0] + 20, center_body[1] - 22)
    sd.ellipse(left_bottom=left_bottom_body, right_top=right_top_body, color=color_human, width=0)
    sd.line(start_point=sd.get_point(center_body[0] - 5, center_body[1] - 100),
            end_point=sd.get_point(center_body[0] - 50, center_body[1] - 150),
            color=color_human, width=3)
    sd.line(start_point=sd.get_point(center_body[0] + 30, center_body[1] - 150),
            end_point=sd.get_point(center_body[0] - 5, center_body[1] - 100),
            color=color_human, width=3)
    sd.line(start_point=sd.get_point(center_body[0] + 100, center_body[1] - 40),
            end_point=sd.get_point(center_body[0] - 100, center_body[1] - 40),
            color=color_human, width=3)


if __name__ == "__main__":
    for _ in range(10):
        position = (random.randint(0, 1200), random.randint(0, 600))
        human(center_body=position, color_human=sd.COLOR_WHITE)
    sd.pause()
