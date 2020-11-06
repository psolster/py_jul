import simple_draw as sd

_snowflake_data = []
_down_snowflakes = []
sd.resolution = (1200, 600)


def create_snowfalls(numbers_sn):
    if not _down_snowflakes:
        for j in range(0, numbers_sn):
            _snowflake_data.append([sd.random_number(0, 1201), sd.random_number(450, 600), 10])
        return _snowflake_data
    else:
        for index in _down_snowflakes:
            _snowflake_data[index][0] = sd.random_number(0, 1201)
            _snowflake_data[index][1] = sd.random_number(450, 600)
        return _snowflake_data


def dr_snowflake(color):
    sd.start_drawing()
    for i, (x, y, length) in enumerate(_snowflake_data):
        center_point = sd.get_point(x, y)
        sd.snowflake(center=center_point, length=length, color=color)
    sd.finish_drawing()


def move_snowflake():
    for i in range(0, len(_snowflake_data)):
        dr_snowflake(color=sd.background_color)
        _snowflake_data[i][1] = _snowflake_data[i][1] - 10

    return _snowflake_data


def get_number_down_snowflakes():
    global _down_snowflakes
    # TODO  Нужно обнулить список номеов снежинок, досьтгших дна, иначе трудно использовать функцию создания снежинок,
    # создавать новые все снежинки или только по индексам "удаленных" снежинок. Ведь реально их не удалили из списка
    # первоначального, а  только зарисовали цветом фона. Роэтому и global _down_snowflakes. иначе IDE выдает
    # предупреждение, что имена внутри функции и снаружи - пересекаются, но это разнык списки же? и пожтому с каждой
    # итерацией кол-во снежинок растес по экспоненте

    _down_snowflakes = []
    for i in range(0, len(_snowflake_data)):
        if _snowflake_data[i][1] < 20:
            _down_snowflakes.append(i)
    return _down_snowflakes


def del_down_snowflakes(list_index):
    for index in list_index:
        center = sd.get_point(_snowflake_data[index][0], _snowflake_data[index][1])
        sd.snowflake(center=center, length=10, color=sd.background_color)
