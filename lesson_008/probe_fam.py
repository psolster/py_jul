from termcolor import cprint
from random import randint


class House:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.garbage = 0

        self.coat = 0
        self.all_money = 0
        self.all_food = 0

    def __str__(self):
        return cprint('В доме еды {}, денег в тумбочке осталось {}, мусор {}'.format(self.food, self.money,
                                                                                     self.garbage), color='red')


class Man:

    def __init__(self, name):
        self.satiety = 30
        self.satisfaction = 100
        self.house = None
        self.name = name

    def __str__(self):
        return '{} сытость {}, степень счастья {}'.format(self.name, self.satiety, self.satisfaction)

    def go_to_the_house(self, house, name):
        self.house = house
        self.name = name

    def eat(self):
        var = randint(0, 30)
        if self.house.food >= var:
            cprint('{} поел'.format(self.name), color='yellow')
            self.satiety += var
            self.house.food -= var
        else:
            cprint('{} нет еды'.format(self.name), color='red')
