import simple_draw as sd

_snowflake_data = []
# TODO Не нужно делать список упавших снежинок глобальной переменной.
#  Он меняется на каждой итерации основного цикла и сохранять его нет
#  никакой необходимости.
_down_snowflakes = []
_quo_down_snow = 0
sd.resolution = (1200, 600)


def create_snowfalls(numbers_sn):
    # TODO При изменении содержимого объекта из глобальной области видимости
    #  не нужно объявлять её глобальной. global нужно только в случае, когда вы
    #  вы меняете саму переменную. Например для my_list.append() global не нужен.
    #  А для my_list = [] без global не обойтись.

    # TODO В этой функции не меняется переменная _snowflake_data и global не нужен.

    global _snowflake_data, _down_snowflakes
    if not _down_snowflakes:
        for j in range(0, numbers_sn):
            _snowflake_data.append([sd.random_number(0, 1201), sd.random_number(450, 600), 10])
        return _down_snowflakes
    else:
        for index in _down_snowflakes:
            _snowflake_data[index][0] = sd.random_number(0, 1201)
            _snowflake_data[index][1] = sd.random_number(450, 600)
        return _snowflake_data


def dr_snowflake(color):
    # TODO В этой функции не меняется переменная _snowflake_data и global не нужен.
    global _snowflake_data
    sd.start_drawing()
    for i, (x, y, length) in enumerate(_snowflake_data):
        center_point = sd.get_point(x, y)
        sd.snowflake(center=center_point, length=length, color=color)
    sd.finish_drawing()
    # sd.sleep(0.001)
#  не логично выглядит работа перерисовки снежинок в ф-ии сдвижения снежинок несколько раз исует с задержками


def move_snowflake():
    # TODO В этой функции не меняется переменная _snowflake_data и global не нужен.
    global _snowflake_data
    for i in range(0, len(_snowflake_data)):
        dr_snowflake(color=sd.background_color)
        _snowflake_data[i][1] = _snowflake_data[i][1] - 20
        # TODO Функция рисования снежинок цветом должна вызываться из основного модуля
        #  после перемещения снежинок. Об этом было написано в условиях задания.
        dr_snowflake(color=sd.COLOR_WHITE)
    return _snowflake_data


def get_number_down_snowflakes():
    # TODO В этой функции не меняется переменная _snowflake_data и global не нужен.
    #  Список _down_snowflakes не нужно делать глобальной переменной.
    global _snowflake_data, _down_snowflakes
    _down_snowflakes = []
    for i in range(0, len(_snowflake_data)):
        if _snowflake_data[i][1] < 20:
            _down_snowflakes.append(i)
    return _down_snowflakes


def del_down_snowflakes(list_index):
    global _quo_down_snow, _snowflake_data
    # TODO Значение _quo_down_snow нигде не используется.
    #  Похоже эту переменную можно безболезненно убрать.
    _quo_down_snow = 0
    _quo_down_snow = len(list_index)

    for index in list_index:
        center = sd.get_point(_snowflake_data[index][0], _snowflake_data[index][1])
        sd.snowflake(center=center, length=10, color=sd.background_color)

    return _quo_down_snow
