import simple_draw as sd

sd.resolution = (1200, 600)


def snow_module(left_bottom, right_top, length_snow_line, number_snowflake):
    sd.resolution = (1200, 600)
    n = number_snowflake
    snowflake_data = []
    for j in range(0, n):
        snowflake_data.append([sd.random_number(left_bottom[0], right_top[0]),
                               sd.random_number(left_bottom[1], right_top[1]), length_snow_line])

    while True:
        sd.start_drawing()
        for i, (x, y, length) in enumerate(snowflake_data):
            point_background_color = sd.get_point(x, y)
            sd.snowflake(center=point_background_color, length=length, color=sd.background_color)
            y = y - 10
            snowflake_data[i][1] = y
            point_color_white = sd.get_point(x, y)
            sd.snowflake(center=point_color_white, length=length, color=sd.COLOR_WHITE)
            if snowflake_data[i][1] <= 20:
                snowflake_data[i][1] = sd.random_number(right_top[1]-50, right_top[1])
                snowflake_data[i][0] = sd.random_number(left_bottom[0], right_top[0])
        sd.finish_drawing()
        sd.sleep(0.1)
        if sd.user_want_exit():
            break


if __name__ == "__main__":
    left_corner = (200, 80)
    right_top_corner = (750, 800)
    snow_module(left_bottom=left_corner, right_top=right_top_corner, length_snow_line=20, number_snowflake=40)
