
import simple_draw as sd
sd.resolution = (1200, 800)


def house(center_of_house, width_house):
    color = sd.COLOR_ORANGE

    k = 0
    x1_house = center_of_house[0] - width_house // 2
    y1_house = center_of_house[1] - width_house // 2
    x2_house = center_of_house[0] + width_house // 2
    y2_house = center_of_house[1] + width_house // 2
    left_corner_house = sd.get_point(x1_house, y1_house)
    right_corner_house = sd.get_point(x2_house+100, y2_house+50)
    line_1_start = sd.get_point(x1_house, y2_house+50)
    line_1_stop = sd.get_point(center_of_house[0]+50, y2_house+125)
    line_2_start = sd.get_point(center_of_house[0]+50, y2_house+125)
    line_2_stop = sd.get_point(x2_house+100, y2_house+50)
    window_left_bottom = sd.get_point(center_of_house[0]-50, center_of_house[1]-50)
    window_right_top = sd.get_point(center_of_house[0]+125, center_of_house[1]+125)
    window_left_bottom_1 = sd.get_point(center_of_house[0] - 40, center_of_house[1] - 40)
    window_right_top_1 = sd.get_point(center_of_house[0] + 115, center_of_house[1] + 115)

    sd.rectangle(left_bottom=left_corner_house, right_top=right_corner_house, width=3, color=sd.COLOR_ORANGE)

    sd.line(line_1_start, line_1_stop, width=3, color=sd.COLOR_ORANGE)
    sd.line(line_2_start, line_2_stop, width=3, color=sd.COLOR_ORANGE)
    for y in range(y1_house, y2_house+1, 50):
        y_1_brick = y
        y_2_brick = y+50
        k += 1
        if k % 2:
            r = x1_house
        else:
            r = x1_house+50
        for x in range(r, x2_house+1, 100):
            x_1_brick = x
            x_2_brick = x+100
            start_point_rect = sd.get_point(x_1_brick, y_1_brick)
            end_point_rect = sd.get_point(x_2_brick, y_2_brick)
            sd.rectangle(start_point_rect, end_point_rect, color, 2)

    sd.rectangle(left_bottom=window_left_bottom, right_top=window_right_top, width=0, color=sd.COLOR_ORANGE)
    sd.rectangle(left_bottom=window_left_bottom_1, right_top=window_right_top_1, width=0, color=sd.COLOR_BLUE)

    sd.pause()


if __name__ == "__main__":
    center = (300, 300)
    house(center_of_house=center, width_house=250)
