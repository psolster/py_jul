# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку

class Snowflake:

    def __init__(self):
        self.coordinats = []
        self.coordinats.append(sd.random_number(0, 1201))
        self.coordinats.append(sd.random_number(0, 601))
        self.color = sd.COLOR_WHITE

    def draw(self):
        center_point = sd.get_point(self.coordinats[0], self.coordinats[1])
        sd.snowflake(center=center_point, length=10, color=self.color)

    def move(self):
        self.coordinats[1] = self.coordinats[1] - 10

    def clear_previous_picture(self):
        center_point = sd.get_point(self.coordinats[0], self.coordinats[1])
        sd.snowflake(center=center_point, length=10, color=sd.background_color)

    def can_fall(self):
        return self.coordinats[1] > 20


class Snowfall:

    def __init__(self):
        # TODO В снегопаде нужно создавать не список координат, а список
        #  снежинок. При добавлении снежинки её начальные координаты создаются автоматически.
        self.all_flakes_coord = []




    def get_fallen_flakes(self):
        down_snowflakes = []
        for i in range(0, len(self.all_flakes_coord)):
            if self.all_flakes_coord[i][1] < 20:
                down_snowflakes.append(i)
        return down_snowflakes

    def append_flakes(self, counts):
        # TODO Для добавления снежинок нужно counts раз создать объект типа Snowflake
        #  и добавить его в список.
        if isinstance(counts, int) and len(self.all_flakes_coord) == 0:
            for _ in range(0, counts):
                self.all_flakes_coord.append([(sd.random_number(0, 1201)), (sd.random_number(0, 1201))])
            return self.all_flakes_coord
        else:
            counts.sort(reverse=True)
            for j in counts:
                center_point = sd.get_point(self.all_flakes_coord[j][0], self.all_flakes_coord[j][1])
                sd.snowflake(center=center_point, length=10, color=sd.background_color)
                self.all_flakes_coord.pop(j)
                self.all_flakes_coord.append([sd.random_number(0, 1201), sd.random_number(250, 600)])


# Задача 1
# flake = Snowflake()
#
# # flake.get_flakes()
# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break
#
# sd.pause()


# Задача 2

flake = Snowflake()
flakes = Snowfall()
count = 5
flakes.append_flakes(counts=count)
while True:
    # TODO Учитывая наличие класса снегопада стоит максимально скрыть
    #  механизм работы снегопада в классе Snowfall.
    #  Для этого цикл по списку снежинок должен быть в одном из методов
    #  класса Snowfall. В результате код снегопада должен быть примерно как основной
    #  цикл в снегопаде шестого модля:
    #  while True:
    #      flakes.draw(...)
    #      flakes.move()
    #      flakes.draw(...)
    #      flakes.get_fallen()
    #      flakes.append...
    #      ...
    #  Вся логика должна быть реалищована в методах класса снегопада.
    #  Можно даже пойти ещё немного дальше и сделать метод, в котором будут
    #  вызываться остальные методы и основной цикл станет ещё проще:
    #  while True:
    #      flakes.step()
    #      sd.sleep(...)
    #      if sd.user_want_exit():
    #         break
    #  Тогда в методе step можно сделать один цикл по списку снежинок:
    #  for flake in self.flakes:
    #      flake.draw()
    #      flake.move()
    #      flake.draw()
    #      if not flake.can_fall:
    #           ...
    for index, (x, y) in enumerate(flakes.all_flakes_coord):
        # TODO Не нужно менять координаты отдельных снежинок внешним кодом.
        #  После создания каждая снежинка должна быть отдельным независимым
        #  объектом и управляться вызовами методов.
        flake.coordinats = [x, y]
        flake.clear_previous_picture()
        flake.move()
        flakes.all_flakes_coord[index] = flake.coordinats
        flake.draw()
        fallen = flakes.get_fallen_flakes()
        flakes.append_flakes(counts=fallen)
        if not flake.can_fall():
            break
        sd.sleep(0.02)
    if sd.user_want_exit():
        break
