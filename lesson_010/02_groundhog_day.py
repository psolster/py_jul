# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.
from random import randint

ENLIGHTENMENT_CARMA_LEVEL = 777


#  Для исключений, созданных в этом задании лучше сделать общий родительский класс,
#  например MainException, унаследованный от Exception, от которого нужно
#  наследовать остальные а в except перехватывать общее исключение.
class MainException(Exception):
    def __init__(self):
        self.message = 'ошибка родительского класса'

    def __str__(self):
        return self.message


class IamGodError(MainException):

    def __init__(self):
        self.message = 'ошибка режима бог'


class DrunkError(MainException):

    def __init__(self):
        self.message = 'перепил - хуже, чем недопил'


class CarCrashError(MainException):

    def __init__(self):
        self.message = 'перепил - хуже, чем недопил'


class GluttonyError(MainException):

    def __init__(self):
        self.message = 'чревоугодие - это грех'


class SuicideError(MainException):

    def __init__(self):
        self.message = 'самоубийцы попадают в ад'


class DepressionError(MainException):

    def __init__(self):
        self.message = 'деперссия это отстой'


list_of_except = [IamGodError, DrunkError, CarCrashError, GluttonyError, DepressionError, SuicideError]


def one_day():
    devil_day = randint(1, 14)
    if devil_day == 13:
        choose_exep = randint(0, 5)
        raise list_of_except[choose_exep]
    carma = randint(1, 7)
    return carma


total = 0
day = 0
while ENLIGHTENMENT_CARMA_LEVEL >= total:
    try:
        res = one_day()
    except (MainException) as exc:
        print(exc)
        total += res
        day += 1
print(f'карму накопил {total} за {day} дней')
# https://goo.gl/JnsDqu
