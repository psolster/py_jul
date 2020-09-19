
import simple_draw as sd


def wall(start, end):
    sd.resolution = (1200, 600)
    start_point = sd.get_point(*start)
    end_point = sd.get_point(*end)
    x_1 = start[0]
    x_2 = end[0]
    y_1 = start[1]
    y_2 = end[1]

    k = 0
    color = sd.COLOR_ORANGE

    for y in range(y_1, y_2+1, 50):
        y_1 = y
        y_2 = y+50
        k += 1
        if k % 2:
            r = 0
        else:
            r = 50
        for x in range(r, end_point+1, 100):
            x_1 = x
            x_2 = x+100
            start_point = sd.get_point(x_1, y_1)
            end_point = sd.get_point(x_2, y_2)
            sd.rectangle(start_point, end_point, color, 2)

    sd.pause()


wall(start=(300, 50), end=(600, 600))