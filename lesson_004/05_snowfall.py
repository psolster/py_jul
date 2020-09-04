# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

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

    for i, (x, y, lenght) in enumerate(snowflake_data):

        point_background_color = sd.get_point(x, y)
        sd.snowflake(center=point_background_color, length=lenght, color=sd.background_color)
        y = y - 10
        snowflake_data[i][1] = y
        point_color_white = sd.get_point(x, y)
        sd.snowflake(center=point_color_white, length=lenght, color=sd.COLOR_WHITE)
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break
    elif snowflake_data[i][1] <= 20:
        for j in range(0, N):
            snowflake_data.append([sd.random_number(0, 1201), sd.random_number(450, 600), sd.random_number(10, 100)])
sd.pause()
