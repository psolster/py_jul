
import simple_draw as sd


def wall(start, end):
    color = sd.COLOR_ORANGE
    sd.resolution = (1200, 600)

    x_1 = start[0]
    x_2 = end[0]
    y_1 = start[1]
    y_2 = end[1]

    k = 0

    for y in range(y_1, y_2+1, 50):
        y_1_brick = y
        y_2_brick = y+50
        k += 1
        if k % 2:
            r = x_1
        else:
            r = x_1+50
        for x in range(r, x_2+1, 100):
            x_1_brick = x
            x_2_brick = x+100
            start_point_rect = sd.get_point(x_1_brick, y_1_brick)
            end_point_rect = sd.get_point(x_2_brick, y_2_brick)
            sd.rectangle(start_point_rect, end_point_rect, color, 2)
        # sd.line(start_point=(x_1, y_1), end_point=(x_1, y_2))
        # sd.line(start_point=(x_2, y_1), end_point=(x_2, y_2))

    sd.pause()


start_wall = (0, 0)
end_wall = (600, 600)
wall(start=start_wall, end=end_wall)
