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

    def __init__(self, name, house):
        self.satiety = 30
        self.satisfaction = 100
        self.house = house
        self.name = name

    def __str__(self):
        return '{} сытость {}, степень счастья {}'.format(self.name, self.satiety, self.satisfaction)

    def go_to_the_house(self, house):
        self.house = house
        # self.name = name

    def eat(self):
        var = randint(0, 30)
        if self.house.food >= var:
            cprint('{} поел'.format(self.name), color='yellow')
            self.satiety += var
            self.house.food -= var
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.satiety -= 10
        self.house.all_money += 150

    def gaming(self):
        cprint('{} гамал в WoT весь день'.format(self.name), color='green')
        self.satiety -= 10
        self.satisfaction += 20

    def shopping(self):
        if self.house.money >= 50:
            if self.satiety <= 15:
                self.eat()
            cprint('{} сходила в магазин за едой'.format(self.name), color='magenta')
            var_shop = randint(10, 50)
            cprint('{} купила еды на {} единиц'.format(self.name, var_shop), color='magenta')
            self.house.money -= var_shop
            self.house.food += var_shop
            self.satiety -= 10
            self.house.all_food += var_shop
            self.satisfaction += 5
        else:
            cprint('деньги кончились! Нужно работать', color='red')

    def buy_fur_coat(self):
        if self.house.money >= 400:
            cprint('{} сходила в магазин за ШУБОЙ'.format(self.name), color='white')
            var_shop = randint(10, self.house.money)
            self.house.money -= var_shop
            self.house.coat += 1
            self.satiety -= 10
            self.satisfaction += 60
        else:
            self.satisfaction -= 5
            cprint('{} не смогла выпросить шубу! Уровень счастья упал и стал {}, пошла заедать горе.'
                   .format(self.name, self.satisfaction), color='white')
            self.eat()

    def clean_house_general(self):
        if self.satiety <= 50:
            self.eat()
        cprint('{} генерально убрала мусор '.format(self.name), color='white')

        self.house.garbage -= 150
        self.satiety -= 45
        self.satisfaction += 5

    def clean_house(self):
        if self.satiety <= 20:
            self.eat()
        cprint('{} убрала мусор '.format(self.name), color='blue')
        var_clin = randint(2, 100)
        self.house.garbage -= var_clin
        self.satiety -= var_clin // 10
        self.satisfaction += 5


class Husband(Man):

    def __init__(self, name):

        super().__init__(name=name, house=home)
        self.death_message = 'умер'

    def act(self):

        if self.satiety <= 0:
            cprint('{} {}...от голода'.format(self.name, self.death_message), color='red')
            return
        if self.satisfaction < 10:
            cprint('{} умер...от депрессии'.format(self.name), color='red')
            return
        dice = randint(1, 3)
        if self.satiety < 20:
            self.eat()
        elif self.house.food < 10:
            self.satisfaction -= 5
            cprint('Придется пнуть жену, жрать нечего, {} расстроился, уровень счасья упал и стал {}'
                   .format(self.name, self.satisfaction), color='blue')

            if Wife.satiety <= 0 or Wife.satisfaction < 10:
                cprint('{} уже ничего не может, у нее сытость {} и счастье {}'
                       .format(Man(Wife), Wife.satiety, Wife.satisfaction), color='red')

            else:
                Wife.eat(masha)
                Wife.shopping(masha)
        elif self.house.money < 50:
            self.work()

        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        elif dice == 3:
            self.gaming()
        else:
            self.gaming()

    def eat(self):
        if self.house.food >= 0:
            cprint('{} поел'.format(self.name), color='yellow')
            var = randint(0, 30)
            self.satiety += var
            self.house.food -= var
        else:
            cprint('{} нет еды'.format(self.name), color='red')


class Wife(Man):
    pass


home = House()
serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
serge.go_to_the_house(house=home)
# masha.go_to_the_house(house=home)
for day in range(3):

    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    # masha.act()
    home.garbage += 5
    if home.garbage > 100:
        serge.degree_of_happiness -= 5
        masha.degree_of_happiness -= 5
    if home.garbage < 00:
        serge.degree_of_happiness += 5
        masha.degree_of_happiness += 5
        home.garbage = 0
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(home, color='cyan')
print('денег всего было заработано ', home.all_money)
print('еды куплено ', home.all_food)
print('шуб куплено ', home.coat)
