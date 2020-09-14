import simple_draw as sd


def rainbow(start_point_rainbow(), end_point_rainbow[], step):
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)


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
        x_2 += 5
        start_point = sd.get_point(x_1, y_1)
        end_point = sd.get_point(x_2, y_2)

    sd.pause()
