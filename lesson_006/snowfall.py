import simple_draw as sd

_snowflake_data = []
# _down_snowflakes = []
sd.resolution = (1200, 600)


def create_snowfalls(numbers_sn):
    # TODO Не нужно разделять начальное создание снежинок с
    #  добавлением замены упавшим. В каждом из случаев
    #  должно быть достаточно сделать numbers_sn итераций
    #  добавления снежинок в список.
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
    # TODO Перенесите вызовы функций sd.start_drawing() и sd.finish_drawing()
    #  в основной модуль до и после вызовоы функции dr_snowflake.
    #  Это уменьшит мерцание во время анимации.
    # sd.start_drawing()
    for i, (x, y, length) in enumerate(_snowflake_data):
        center_point = sd.get_point(x, y)
        sd.snowflake(center=center_point, length=length, color=color)
    # sd.finish_drawing()


def move_snowflake():
    for i in range(0, len(_snowflake_data)):
        dr_snowflake(color=sd.background_color)
        _snowflake_data[i][1] = _snowflake_data[i][1] - 10

    return _snowflake_data


def get_number_down_snowflakes():
    #   Нужно обнулить список номеов снежинок, досьтгших дна, иначе трудно использовать функцию создания снежинок,
    # TODO Список упавших снежинок не должен влиять на добавление снежинок
    #  для замены снежинок новыми. Переменная _down_snowflakes не должна
    #  быть глобальной.
    # создавать новые все снежинки или только по индексам "удаленных" снежинок. Ведь реально их не удалили из списка
    # первоначального, а  только зарисовали цветом фона. Роэтому и global _down_snowflakes. иначе IDE выдает
    # предупреждение, что имена внутри функции и снаружи - пересекаются, но это разнык списки же? и пожтому с каждой
    # итерацией кол-во снежинок растес по экспоненте

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
