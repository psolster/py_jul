import simple_draw as sd


def rainbow(start_rainbow_point, end_rainbow_point):
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
    start_point = sd.get_point(*start_rainbow_point)
    end_point = sd.get_point(*end_rainbow_point)
    x1 = start_rainbow_point[0]
    x2 = end_rainbow_point[0]
    for color in rainbow_colors:
        sd.line(start_point, end_point, color, 4)

        x1 += 5
        x2 += 5
        start_point = sd.get_point(x1, start_rainbow_point[1])
        end_point = sd.get_point(x2, end_rainbow_point[1])


if __name__ == "__main__":
    sd.resolution = (1200, 600)
    rainbow(start_rainbow_point=(50, 50), end_rainbow_point=(300, 300))
    sd.pause()
