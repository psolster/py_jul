# ####################################################### Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умирает от депрессии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.

from termcolor import cprint
from random import randint


class House:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.garbage = 0
        self.food_cat = 30
        self.coat = 0
        self.all_money = 0
        self.all_food = 0

    def __str__(self):
        return 'В доме еды {}, для кота еды {}, денег в тумбочке осталось {}, мусор {}'.format(
            self.food,
            self.food_cat,
            self.money,
            self.garbage
        )


class Man:

    def __init__(self, name, house):
        self.satiety = 10
        self.satisfaction = 100
        self.house = house
        self.name = name
        self.go_to_the_house_message_h = 'въехал'
        self.go_to_the_house_message_w = 'въехала'
        self.death_message_h = 'умер'
        self.eat_message_h = 'поел'
        self.death_message_w = 'умерла'
        self.eat_message_w = 'поела'

    def __str__(self):
        return '{} сытость {}, степень счастья {}'.format(self.name, self.satiety, self.satisfaction)

    def go_to_the_house(self, house, name):
        self.house = house
        self.name = name
        if self.name == serge.name:
            cprint('{} {}  в дом'.format(self.name, self.go_to_the_house_message_h), color='cyan')
        else:
            cprint('{} {}  в дом'.format(self.name, self.go_to_the_house_message_w), color='cyan')

    def eat(self):
        var = randint(10, 30)
        if self.house.food >= var:
            if self.name == serge.name:
                cprint('{} {} {} еды'.format(self.name, self.eat_message_h, var), color='yellow')
            else:
                cprint('{} {} {} еды'.format(self.name, self.eat_message_w, var), color='yellow')
            self.satiety += var
            self.house.food -= var
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def game_with_cat(self):
        self.satiety -= 5
        self.satisfaction += 10
        cprint('Игра с киской сделала счастливей, уровень счатья {} '.format(self.satisfaction), color='cyan')

    def act(self):

        if self.satiety <= 0:
            if self.name == serge.name:
                cprint('{} {}...от голода'.format(self.name, self.death_message_h), color='red')
            else:
                cprint('{} {}...от голода'.format(self.name, self.death_message_w), color='red')
            return True
        elif self.satisfaction < 10:
            if self.name == serge.name:
                cprint('{} {}...от депрессии'.format(self.name, self.death_message_h), color='red')
            else:
                cprint('{} {}...от депрессии'.format(self.name, self.death_message_w), color='red')
            return True

        if self.satiety < 20:
            self.eat()
        elif self.house.food < 10 or self.house.food_cat < 10:
            self.satisfaction -= 5
            cprint('Придется посетить магазин, жрать нечего, {} расстроился, уровень счасья упал и стал {}'
                   .format(self.name, self.satisfaction), color='blue')


class Husband(Man):

    def __init__(self, name):
        super().__init__(name=name, house=home)

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.satiety -= 10
        self.house.all_money += 150

    def gaming(self):
        cprint('{} гамал в WoT весь день'.format(self.name), color='green')
        self.satiety -= 10
        self.satisfaction += 20

    def act(self):
        dice = randint(1, 4)
        if super().act():
            cprint(' {} выбывает из игры, не сраслось=)'.format(self.name), color='green')
            quit()

        elif dice == 1:
            self.work()
        elif dice == 2:
            super().eat()
        elif dice == 3:
            self.gaming()
        else:
            self.game_with_cat()


class Wife(Man):
    def __init__(self, name):
        super().__init__(name=name, house=home)

    def shopping(self):
        if self.house.money >= 50:
            if self.satiety <= 20:
                super().eat()
            cprint('{} сходила в магазин за едой'.format(self.name), color='magenta')
            var_shop = randint(20, 50)
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
            super().eat()

    def clean_house_general(self):
        if self.satiety <= 50:
            super().eat()
        cprint('{} генерально убрала мусор '.format(self.name), color='white')

        self.house.garbage -= 150
        self.satiety -= 45
        self.satisfaction += 5

    def clean_house(self):
        if self.satiety <= 20:
            super().eat()
        cprint('{} убрала мусор '.format(self.name), color='blue')
        var_clin = randint(2, 100)
        self.house.garbage -= var_clin
        self.satiety -= var_clin // 10
        self.satisfaction += 5

    def shopping_for_cat(self):
        if self.house.money >= 50 and self.house.food_cat < 10:
            cprint('{} сходила в магазин за едой для кота'.format(self.name), color='green')
            self.house.food_cat += 10
            self.house.money -= 10
            self.satiety -= 10

        else:
            cprint('деньги кончились! Нужно работать', color='red')

    def act(self):
        dice = randint(1, 6)
        if super().act():
            cprint(' {} выбывает из игры, не сраслось=)'.format(self.name), color='green')
            quit()

        elif self.house.food < 20:
            self.satisfaction -= 2
            cprint('Придется бегом бежать в магаз за едой, {} расстроилась, уровень счасья упал и стал {}'
                   .format(self.name, self.satisfaction), color='blue')
            self.shopping()
        elif self.house.food_cat < 10:
            cprint('Котик голодает, это п....хо, {} расстроилась, уровень счасья упал и стал {}'
                   .format(self.name, self.satisfaction), color='blue')
            self.shopping_for_cat()

        elif dice == 1:
            self.shopping()
        elif dice == 2:
            self.clean_house()
        elif dice == 3:
            self.buy_fur_coat()
        elif dice == 4:
            super().eat()
        elif dice == 5:
            self.game_with_cat()
        else:
            self.shopping_for_cat()


class Cat(Man):

    def __init__(self, name):
        super().__init__(name=name, house=home)
        self.satiety = 30
        self.satisfaction = 50
        self.name = name

    def tear_wallpaper(self):
        self.satisfaction += 5
        self.satiety -= 10
        self.house.garbage += 5
        cprint('{} решила подрать обои! Уровень счастья стал {}, но уровень голода {}'.format(self.name,
                                                                                              self.satisfaction,
                                                                                              self.satiety),
               color='blue')

    def act(self):
        dice = randint(1, 3)
        if super().act():
            cprint(' {} выбывает из игры, не сраслось=)'.format(self.name), color='green')
            quit()

        elif self.house.food_cat < 10:
            self.satisfaction -= 2
            cprint('Жратвы нет", {} расстроилась, уровень счасья упал и стал {}. Пошла вредить людям'
                   .format(self.name, self.satisfaction), color='blue')
            self.tear_wallpaper()

        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.tear_wallpaper()
        elif dice == 3:
            self.sleep()

    def eat(self):
        var = randint(1, 10)
        cprint('{} съела {} еды, сытость стала {}'.format(self.name, var, self.satiety), color='yellow')
        self.satiety += var * 2
        self.house.food_cat -= var

    def sleep(self):
        self.satisfaction += 10
        self.satiety -= 5
        cprint('{} поспала уровень счастья {}, сытость стала {}'.format(self.name, self.satisfaction, self.satiety),
               color='green')


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
murka = Cat(name='Мурка')
serge.go_to_the_house(house=home, name=serge.name)
masha.go_to_the_house(house=home, name=masha.name)
murka.go_to_the_house(house=home, name=murka.name)
for day in range(1, 365):

    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    murka.act()
    home.garbage += 5
    if home.garbage > 100:
        serge.satisfaction -= 5
        masha.satisfaction -= 5
        murka.satisfaction += 5
    else:
        serge.satisfaction += 5
        masha.satisfaction += 5
        murka.satisfaction -= 5
        home.garbage = 0
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(murka, color='cyan')
    cprint(home, color='cyan')
print('денег всего было заработано ', home.all_money)
print('еды куплено ', home.all_food)
print('шуб куплено ', home.coat)


# ####################################################### Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


# ####################################################### Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child:

    def __init__(self):
        pass

    def __str__(self):
        return super().__str__()

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass

#  после реализации второй части - отдать на проверку учителем две ветки

# TODO Переходите ко второй части задания.


# ####################################################### Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
