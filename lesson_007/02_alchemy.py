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

# TODO здесь ваш код


class Water:
    # def __init__(self, gift=None):
    #     self.content = []
    #     if gift:
    #         self.content.append(gift)

    # def __eq__(self, other):
    #     return self.content == other.content

    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        if other == Air:
            return 'Шторм'
        elif other == Fire:
            return 'Пар'
        elif other == Earth:
            return 'Грязь'
        else:
            return None


class Air:
    # def __init__(self, gift=None):
    #     self.content = []
    #     if gift:
    #         self.content.append(gift)

    # def __eq__(self, other):
    #     return self.content == other.content

    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if other == Fire:
            return 'Молния'
        elif other == Earth:
            return 'Пыль'
        else:
            return None


class Fire:
    def __init__(self, gift=None):
        self.content = []
        if gift:
            self.content.append(gift)

    def __eq__(self, other):
        return self.content == other.content

    def __str__(self):
        return 'Fire: ' + ', '.join(self.content)

    def __add__(self, other):
        new_obj = Fire()
        new_obj.content.extend(self.content)
        new_obj.content.extend(other.content)
        return new_obj


class Earth:
    def __init__(self, gift=None):
        self.content = []
        if gift:
            self.content.append(gift)

    def __eq__(self, other):
        return self.content == other.content

    def __str__(self):
        return 'Earth: ' + ', '.join(self.content)

    def __add__(self, other):
        new_obj = Earth()
        new_obj.content.extend(self.content)
        new_obj.content.extend(other.content)
        return new_obj


class Storm:
    def __init__(self, part1, part2 ):
        self.part1 = part1
        self.part2 = part2

    # def __eq__(self, other):
    #     return self.content == other.content

    def __str__(self):
        return 'Шторм'

    # def __add__(self, other):
    #     new_obj = Storm()
    #     new_obj.content.extend(self.content)
    #     new_obj.content.extend(other.content)
    #     return new_obj
#
#
# class Steam:
#     def __init__(self, gift=None):
#         self.content = []
#         if gift:
#             self.content.append(gift)
#
#     def __eq__(self, other):
#         return self.content == other.content
#
#     def __str__(self):
#         return 'Steam: ' + ', '.join(self.content)
#
#     def __add__(self, other):
#         new_obj = Steam()
#         new_obj.content.extend(self.content)
#         new_obj.content.extend(other.content)
#         return new_obj
#
#
# class Mud:
#     def __init__(self, gift=None):
#         self.content = []
#         if gift:
#             self.content.append(gift)
#
#     def __eq__(self, other):
#         return self.content == other.content
#
#     def __str__(self):
#         return 'Mud: ' + ', '.join(self.content)
#
#     def __add__(self, other):
#         new_obj = Mud()
#         new_obj.content.extend(self.content)
#         new_obj.content.extend(other.content)
#         return new_obj
#
#
# class Flash:
#     def __init__(self, gift=None):
#         self.content = []
#         if gift:
#             self.content.append(gift)
#
#     def __eq__(self, other):
#         return self.content == other.content
#
#     def __str__(self):
#         return 'Flash: ' + ', '.join(self.content)
#
#     def __add__(self, other):
#         new_obj = Flash()
#         new_obj.content.extend(self.content)
#         new_obj.content.extend(other.content)
#         return new_obj
#
#
# class Dust:
#     def __init__(self, gift=None):
#         self.content = []
#         if gift:
#             self.content.append(gift)
#
#     def __eq__(self, other):
#         return self.content == other.content
#
#     def __str__(self):
#         return 'Dust: ' + ', '.join(self.content)
#
#     def __add__(self, other):
#         new_obj = Dust()
#         new_obj.content.extend(self.content)
#         new_obj.content.extend(other.content)
#         return new_obj
#
#
# class Lava:
#     def __init__(self, gift=None):
#         self.content = []
#         if gift:
#             self.content.append(gift)
#
#     def __str__(self):
#         return 'Lava: ' + ', '.join(self.content)
#
#     def __eq__(self, other):
#         return self.content == other.content
#
#     def __add__(self, other):
#         new_obj = Lava()
#         new_obj.content.extend(self.content)
#         new_obj.content.extend(other.content)
#         return new_obj


# ferst = Water(gift='бутерброд')
# second = Mud(gift='банан')
# new = ferst + second
print(Water(), '+', Air(), '=', Water() + Air())

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
