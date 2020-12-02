# -*- coding: utf-8 -*-

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

# -*- coding: utf-8 -*-

from random import randint

from termcolor import cprint


class Man:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness,
        )

    def eat(self):
        if self.house.food >= 0:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 30
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_mtv(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 300
            self.house.food += 50
            self.fullness -= 10
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def shopping_for_cat(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой для кота'.format(self.name), color='magenta')
            self.house.money -= 100
            self.house.cat_food += 50
            self.fullness -= 10
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Въехал в дом'.format(self.name), color='cyan')

    def get_cat(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} подобрал кота'.format(self.name), color='cyan')

    def cleaning(self):
        if self.fullness <= 20:
            self.eat()
        cprint('{} убрал говно и обои за котом '.format(self.name), color='blue')
        self.house.garbage -= 5
        self.fullness -= 20

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 4)
        if self.fullness < 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.cat_food < 20:
            self.shopping_for_cat()
        elif self.house.money < 50:
            self.work()

        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        elif dice == 3:
            self.cleaning()
        else:
            self.watch_mtv()


class House:
    def __init__(self):
        self.food = 50
        self.money = 50
        self.cat_food = 0
        self.cat_plate = None
        self.house = None
        self.garbage = 0

    def __str__(self):
        return 'В доме еды осталось {}, для кота еды осталось {}, денег осталось {}, грязи дома {}'.format(
            self.food, self.cat_food, self.money, self.garbage
        )


class Cat:

    def __init__(self, name='КОТ'):
        self.name = name
        self.fullness = 10
        self.house = None
        self.cat_plate = None
        self.cat_friend = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness,
        )

    def cat_go_to_the_house(self, house, cat_friend):
        self.house = house
        self.fullness -= 5
        self.cat_plate = house
        self.cat_friend = cat_friend
        cprint('{} Въехал в дом. У кота появилась тарелка, но в ней {} еды'.format(self.name, self.house.cat_food),
               color='cyan')

    def eat(self):
        if self.house.cat_food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 20
            self.house.cat_food -= 10
            self.house.garbage += 2
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def sleep(self):
        cprint('{} завалился спать на диване'.format(self.name), color='blue')
        self.fullness -= 10

    def tear_wallpaper(self):
        cprint('{} подрал обои'.format(self.name), color='blue')
        self.house.garbage += 5
        self.fullness -= 10

    def clining_samself(self):
        cprint('{} очень много нагадил! {} заставил его убираться!'.format(self.name, self.cat_friend),
               color='green')

        self.fullness -= 100
        self.house.garbage -= 200

    def cat_act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 3)
        if self.fullness < 10:
            self.eat()
        elif self.house.cat_food < 10:
            self.tear_wallpaper()
        elif self.fullness >= 50:
            self.sleep()
        elif self.house.garbage > 300:
            self.clining_samself()
            cprint('Грязи стало {}, {} решил убить кота =)'.format(self.house.garbage, self.cat_friend), color='yellow')
            self.fullness = 0
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.tear_wallpaper()
        elif dice == 3:
            self.sleep()


citizens = [
    Man(name='Бивис'),
]
my_sweet_home = House()
me_cat = Cat()
for citisen in citizens:
    citisen.go_to_the_house(house=my_sweet_home)
    citisen.get_cat(house=my_sweet_home)
    me_cat.cat_go_to_the_house(house=my_sweet_home, cat_friend=citisen)

for day in range(1, 365):
    print('================ день {} =================='.format(day))
    for citisen in citizens:
        citisen.act()
        me_cat.cat_act()
    print('--- в конце дня ---')
    for citisen in citizens:
        print(citisen)
        print(me_cat)
    print(my_sweet_home)

# Создадим двух людей, живущих в одном доме - Бивиса и Батхеда
# Нужен класс Дом, в нем должн быть холодильник с едой и тумбочка с деньгами
# Еда пусть хранится в холодильнике в доме, а деньги - в тумбочке.


# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
