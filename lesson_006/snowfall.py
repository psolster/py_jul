import simple_draw as sd
_snowflake_data = []
sd.resolution = (1200, 600)


def create_snowfalls(numbers_sn):
    global _snowflake_data
    if not _snowflake_data:
        for j in range(0, numbers_sn):
            _snowflake_data.append([sd.random_number(0, 1201), sd.random_number(250, 600), 10])
    else:
        for i, (x, y, length) in enumerate(_snowflake_data):
            if y < 20:
                _snowflake_data.pop(i)
                _snowflake_data.append([sd.random_number(0, 1201), sd.random_number(450, 600), 10])
        return _snowflake_data


def dr_snowflake(color):
    for i, (x, y, length) in enumerate(_snowflake_data):
        center_point = sd.get_point(x, y)
        sd.snowflake(center=center_point, length=length, color=color)


def move_snowflake():
    for i in range(0, len(_snowflake_data)):
        dr_snowflake(color=sd.background_color)
        _snowflake_data[i][1] = _snowflake_data[i][1] - 10
    return _snowflake_data


def get_number_down_snowflakes():
    down_snowflakes = []
    for i in range(0, len(_snowflake_data)):
        if _snowflake_data[i][1] < 20:
            down_snowflakes.append(i)
    return down_snowflakes


def del_down_snowflakes(list_index):
    for index in list_index:
        center = sd.get_point(_snowflake_data[index][0], _snowflake_data[index][1])
        sd.snowflake(center=center, length=10, color=sd.background_color)
    return len(list_index)
