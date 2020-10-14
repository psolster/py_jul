import simple_draw as sd

_snowflake_data = []
_down_snowflakes = []
sd.resolution = (1200, 600)


def create_snowfalls(numbers_sn):
    global _snowflake_data
    for j in range(0, numbers_sn):
        _snowflake_data.append([sd.random_number(0, 1201), sd.random_number(450, 600), 10])


def dr_snowflake(color):
    global _snowflake_data
    sd.start_drawing()
    for i, (x, y, length) in enumerate(_snowflake_data):
        point_background_color = sd.get_point(x, y)
        sd.snowflake(center=point_background_color, length=length, color=color)

    sd.finish_drawing()
    sd.sleep(0.1)


def move_snowflake():
    global _snowflake_data

    for i, (x, y, length) in enumerate(_snowflake_data):

        point_color_background = sd.get_point(x, y)
        sd.snowflake(center=point_color_background, length=length, color=sd.background_color)
        _snowflake_data[i][1] = _snowflake_data[i][1] - 10
        y = _snowflake_data[i][1]
        point_color_white = sd.get_point(x, y)
        sd.snowflake(center=point_color_white, length=length, color=sd.COLOR_WHITE)


def get_number_down_snowflakes():
    global _snowflake_data, _down_snowflakes

    for i, (x, y, length) in enumerate(_snowflake_data):
        if y < 10:
            _down_snowflakes.append([i, x, y, length])
    return _down_snowflakes


