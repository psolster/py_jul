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


class IamGodError(Exception):

    def __init__(self):
        self.message = 'ошибка режима бог'

    def __str__(self):
        return self.message


class DrunkError(Exception):

    def __init__(self):
        self.message = 'перепил - хуже, чем недопил'

    def __str__(self):
        return self.message


class CarCrashError(Exception):

    def __init__(self):
        self.message = 'перепил - хуже, чем недопил'

    def __str__(self):
        return self.message


class GluttonyError(Exception):

    def __init__(self):
        self.message = 'чревоугодие - это грех'

    def __str__(self):
        return self.message


class SuicideError(Exception):

    def __init__(self):
        self.message = 'самоубийцы попадают в ад'

    def __str__(self):
        return self.message


class DepressionError(Exception):

    def __init__(self):
        self.message = 'деперссия это отстой'

    def __str__(self):
        return self.message


def one_day():
    devil_day = randint(1, 14)
    if devil_day == 13:
        choose_exep = randint(1, 7)
        if choose_exep == 1:
            try:
                raise IamGodError
            except IamGodError as exc:
                print(f'Поймано исключение {exc}')
        elif choose_exep == 2:
            try:
                raise DrunkError
            except DrunkError as exc:
                print(f'Поймано исключение {exc}')
        elif choose_exep == 3:
            try:
                raise CarCrashError
            except CarCrashError as exc:
                print(f'Поймано исключение {exc}')
        elif choose_exep == 4:
            try:
                raise GluttonyError
            except GluttonyError as exc:
                print(f'Поймано исключение {exc}')
        elif choose_exep == 5:
            try:
                raise DepressionError
            except DepressionError as exc:
                print(f'Поймано исключение {exc}')
        else:
            try:
                raise SuicideError
            except SuicideError as exc:
                print(f'Поймано исключение {exc}')

    carma = randint(1, 8)
    return carma


total = 0
day = 0
while ENLIGHTENMENT_CARMA_LEVEL >= total:
    res = one_day()
    total += res
    day += 1
print(total, day)
# https://goo.gl/JnsDqu
