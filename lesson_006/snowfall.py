import simple_draw as sd

_snowflake_data = []
_down_snowflakes = []
_quo_down_snow = 0
sd.resolution = (1200, 600)


def create_snowfalls(numbers_sn):
    global _snowflake_data
    for j in range(0, numbers_sn):
        _snowflake_data.append([sd.random_number(0, 1201), sd.random_number(450, 600), 10])


def dr_snowflake(color):
    global _snowflake_data
    sd.start_drawing()
    for i, (x, y, length) in enumerate(_snowflake_data):
        center_point = sd.get_point(x, y)
        sd.snowflake(center=center_point, length=length, color=color)
    sd.finish_drawing()
    sd.sleep(0.1)


def move_snowflake():
    global _snowflake_data
    for i in range(0, len(_snowflake_data)):
        dr_snowflake(color=sd.background_color)
        _snowflake_data[i][1] = _snowflake_data[i][1] - 10
        dr_snowflake(color=sd.COLOR_WHITE)
    return _snowflake_data


def get_number_down_snowflakes():

    global _snowflake_data, _down_snowflakes
    _down_snowflakes = []
    for i in range(0, len(_snowflake_data)):
        if _snowflake_data[i][1] < 50:
            _down_snowflakes.append(i)
    return _down_snowflakes


def del_down_snowflakes(list_index):
    global _quo_down_snow
    _quo_down_snow = 0
    for index in list_index:
        _quo_down_snow += 1
        center = sd.get_point(_snowflake_data[index][0], _snowflake_data[index][1])
        sd.snowflake(center=center, length=10, color=sd.background_color)
        # _snowflake_data.pop(index)
    return _quo_down_snow
