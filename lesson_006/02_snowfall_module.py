# -*- coding: utf-8 -*-

import simple_draw as sd

from snowfall import create_snowfalls, dr_snowflake, move_snowflake, get_number_down_snowflakes, del_down_snowflakes

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
# снежинки хранить в глобальных переменных модуля snowfall
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

# создать_снежинки(N)

create_snowfalls(numbers_sn=2)
while True:
    dr_snowflake(color=sd.COLOR_WHITE)
    move_snowflake()
    number_out_snowflakes = get_number_down_snowflakes()
    quo_new_snowflakes = del_down_snowflakes(list_index=number_out_snowflakes)
    create_snowfalls(numbers_sn=quo_new_snowflakes)
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
