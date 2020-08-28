# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# TODO Удобнее хранить координаты и параметры снежинок в одной структуре данных.
#  Так работать с ними будет проще:
#  список со списками:
#  snowflakes = [[0, 2, 4], [5, 6, 7], ...]
#  for x, y, length in snowflakes:
#      point = Point(x, y)
#      snowflake(point, length)
#  или список со словарями:
#  snowflakes = [{"x": 0, "y": 2, "length": 4}, {"x": 5, "y": 6, "length": 7}, ]
#  for snowflake in snowflakes:
#      point = Point(snowflake['x'], snowflake['y'])
#      snowflake(point, snowflake["length"])
#  или словарь со словарями:
#  snowflakes = {1: {"x": 0, "y": 2, "length": 4}, {"x": 5, "y": 6, "length": 7}, }
#  for i, snowflake in snowflakes.items():
#      point = Point(snowflake['x'], snowflake['y'])
#      snowflake(point, snowflake["length"])
#  Или с использованием enumerate, если нужен индекс элемента в списке:
#  for i, (x, y, length) in enumerate(snowflake_param):
#  Пример для словаря, содержащего список параметров снежинки:
#  for i, (x, y, length) in snowflake_param.items():

# coordin_x = {}
# lenght_snowflake_line = {}
# for key_x_coordinat in range(0, 1201, 60):
#     coordin_x[key_x_coordinat] = sd.random_number(300, 600)
#
# for i in range(0, 1201, 60):
#     lenght_snowflake_line[i] = sd.random_number(10, 100)
# while True:
#     sd.clear_screen()
#     for x in coordin_x:
#         y = coordin_x[x]
#         point = sd.get_point(x, y)
#         sd.snowflake(center=point, length=lenght_snowflake_line[x])
#         coordin_x[x] -= 10
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break
# sd.pause()

# Примерный алгоритм отрисовки снежинок
#   навсегда
#     очистка экрана
#     для индекс, координата_х из списка координат снежинок
#       получить координата_у по индексу
#       создать точку отрисовки снежинки
#       нарисовать снежинку цветом фона
#       изменить координата_у и запомнить её в списке по индексу
#       создать новую точку отрисовки снежинки
#       нарисовать снежинку на новом месте белым цветом
#     немного поспать
#     если пользователь хочет выйти
#       прервать цикл
# TODO Переходите ко второй части задания.


# Часть 2 (делается после зачета первой части)
#
# Ускорить отрисовку снегопада
# - убрать clear_screen() из цикла
# в начале рисования всех снежинок вызвать sd.start_drawing()
# - на старом месте снежинки отрисовать её же, но цветом sd.background_color
# - сдвинуть снежинку
# - отрисовать её цветом sd.COLOR_WHITE на новом месте
# - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()

# Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg

snowflake_data = []
for j in range(0, N):
    snowflake_data.append([sd.random_number(0, 1201), sd.random_number(450, 600), sd.random_number(10, 100)])

while True:
    sd.start_drawing()
    # TODO Снегопад должен продолжаться до тех пор пока пользователь его не прервёт.
    #  Снежинки, достигшие нижней части экрана, нужно перемещать наверх или заменять новые.
    for i, (x, y, lenght) in enumerate(snowflake_data):

        point_background_color = sd.get_point(x, y)
        sd.snowflake(center=point_background_color, length=lenght, color=sd.background_color)
        y = y - 10
        snowflake_data[i][1] = y
        # TODO Названия переменных принято записывать строчными буквами.
        point_COLOR_WHITE = sd.get_point(x, y)
        sd.snowflake(center=point_COLOR_WHITE, length=lenght, color=sd.COLOR_WHITE)
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break
sd.pause()
