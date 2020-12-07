# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())


class Water:

    def __str__(self):
        return 'Вода'

    def __add__(self, other):

        if isinstance(other, Air):
            return Storm(part1=self, part2=other)
        elif isinstance(other, Fire):
            return Steam(part1=self, part2=other)
        elif isinstance(other, Earth):
            return Mud(part1=self, part2=other)
        else:
            return None


class Air:

    def __init__(self):
        self.type = 'Воздух'

    def __str__(self):
        return 'Воздух'

    def __add__(self, other):

        if isinstance(other, Fire):
            return Flash(part1=self, part2=other)
        elif isinstance(other, Earth):
            return Dust(part1=self, part2=other)
        else:
            return None


class Fire:
    def __init__(self):
        self.type = 'Огонь'

    def __str__(self):
        return 'Огонь'

    def __add__(self, other):

        if isinstance(other, Earth):
            return Lava(part1=self, part2=other)
        else:
            return None


class Earth:
    def __init__(self):
        self.type = 'Земля'

    def __str__(self):
        return 'Земля'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Flash(part1=self, part2=other)
        elif isinstance(other, Earth):
            return Dust(part1=self, part2=other)
        else:
            return None


class Frost:
    def __init__(self):
        self.type = 'Мороз'

    def __str__(self):
        return 'Мороз'

    def __add__(self, other):
        if isinstance(other, Water):
            return Ice(part1=self, part2=other)
        elif isinstance(other, Air):
            return Snow(part1=self, part2=other)
        else:
            return None


class Storm:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Шторм, состою из ' + str(self.part1) + ' и ' + str(self.part2)


class Steam:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Пар, состою из ' + str(self.part1) + ' и ' + str(self.part2)


class Mud:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Грязь, состою из ' + str(self.part1) + ' и ' + str(self.part2)


class Flash:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Молния, состою из ' + str(self.part1) + ' и ' + str(self.part2)


class Dust:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Пыль, состою из ' + str(self.part1) + ' и ' + str(self.part2)


class Lava:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Лава, состою из ' + str(self.part1) + ' и ' + str(self.part2)


class Ice:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Гололед, состою из ' + str(self.part1) + ' и ' + str(self.part2)


class Snow:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Снег, состою из ' + str(self.part1) + ' и ' + str(self.part2)


print(Water(), '+', Air(), '=', Water() + Air())
print(Water(), '+', Fire(), '=', Water() + Fire())
print(Water(), '+', Earth(), '=', Water() + Earth())
print(Air(), '+', Earth(), '=', Air() + Earth())
print(Air(), '+', Fire(), '=', Air() + Fire())
print(Fire(), '+', Earth(), '=', Fire() + Earth())
# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
print(Frost(), '+', Water(), '=', Frost() + Water())
print(Frost(), '+', Air(), '=', Frost() + Air())

# Зачёт!
