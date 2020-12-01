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
        # TODO Используйте функцию isinstance, которая позволяет
        #  определить является ли объект экземпляром определённого класса.
        #  list1 = [1, 2, 3]
        #  isinstance(list1, list) вернёт True
        #  isinstance(list1, str) вернёт False

        prov = str(other)
        if prov == 'Воздух':
            return Storm(part1=self, part2=other)
        elif prov == 'Огонь':
            return Steam(part1=self, part2=other)
        elif prov == 'Земля':
            return Mud(part1=self, part2=other)
        else:
            return None


class Air:

    def __init__(self):
        self.type = 'Воздух'

    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        prov = str(other)
        if prov == "Огонь":
            return Flash(part1=self, part2=other)
        elif prov == "Земля":
            return Dust(part1=self, part2=other)
        else:
            return None


class Fire:
    def __init__(self):
        self.type = 'Огонь'

    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        prov = str(other)
        if prov == 'Земля':
            return Lava(part1=self, part2=other)
        else:
            return None


class Earth:
    def __init__(self):
        self.type = 'Земля'

    def __str__(self):
        return 'Земля'

    def __add__(self, other):
        if other == Fire:
            return 'Молния'
        elif other == Earth:
            return 'Пыль'
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


print(Water(), '+', Air(), '=', Water() + Air())
print(Water(), '+', Fire(), '=', Water() + Fire())
print(Water(), '+', Earth(), '=', Water() + Earth())
print(Air(), '+', Earth(), '=', Air() + Earth())
print(Air(), '+', Fire(), '=', Air() + Fire())
print(Fire(), '+', Earth(), '=', Fire() + Earth())
# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
