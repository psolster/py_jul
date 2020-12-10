import simple_draw as sd

sd.resolution = (1200, 600)


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку

class Snowflake:

    def __init__(self):
        self.coordinats = []
        self.color = sd.COLOR_WHITE

    def get_snowflake(self):
        self.coordinats.append(sd.random_number(0, 1201))
        self.coordinats.append(sd.random_number(450, 601))
        return self.coordinats

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
        self.all_flakes = []

    def snowfall_generate(self, quantity):
        it = 0
        while it < quantity:
            snowflake = Snowflake.get_snowflake(self=Snowflake())
            self.all_flakes.append(snowflake)
            it += 1
        return self.all_flakes

    def get_fallen_flakes(self):
        down_snowflakes = []
        for i in range(0, len(self.all_flakes)):
            if self.all_flakes[i][1] < 20:
                down_snowflakes.append(i)
        return down_snowflakes

    def append_flakes(self, counts):
        if isinstance(counts, int) and len(self.all_flakes) == 0:
            for _ in range(0, counts):
                self.all_flakes.append([(sd.random_number(0, 1201)), (sd.random_number(500, 601))])
            return self.all_flakes
        else:
            counts.sort(reverse=True)
            for j in counts:
                center_point = sd.get_point(self.all_flakes[j][0], self.all_flakes[j][1])
                sd.snowflake(center=center_point, length=10, color=sd.background_color)
                self.all_flakes.pop(j)
                self.all_flakes.append([sd.random_number(0, 1201), sd.random_number(250, 600)])

    def snowfall_step(self):
        from_snowflake = Snowflake()
        for flake in self.all_flakes:
            from_snowflake.coordinats = flake
            from_snowflake.clear_previous_picture()
            from_snowflake.move()
            from_snowflake.draw()
            fallen = self.get_fallen_flakes()
            self.append_flakes(counts=fallen)
            if not from_snowflake.can_fall():
                break


# Задача 1
# flake = Snowflake()
#
# flake.get_snowflake()
# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

# sd.pause()

now = Snowfall()
now.snowfall_generate(quantity=10)
while True:
    now.snowfall_step()
    sd.sleep(0.05)
    if sd.user_want_exit():
        break

# Зачёт!
