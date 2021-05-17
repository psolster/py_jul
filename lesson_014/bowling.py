# -*- coding: utf-8 -*-
from random import randint

GAME_RESULT = ''


def ferst_throw():
    throw_result = randint(0, 10)
    return throw_result


def game_set():
    print('вошли в фрейм игры')
    global GAME_RESULT
    _frame_calc = 0.0
    while _frame_calc < 10:
        throw = ferst_throw()
        lost = 10 - throw
        if 1 <= throw <= 9:
            _frame_calc += .5
            GAME_RESULT += str(throw)
            second_throw = ferst_throw()
            if second_throw >= lost:
                GAME_RESULT += '/'
                _frame_calc += .5
            elif second_throw == 0:
                GAME_RESULT += '-'
                _frame_calc += .5
            else:
                GAME_RESULT += str(second_throw)
                _frame_calc += .5
        elif throw == 10:
            _frame_calc += 1
            GAME_RESULT += 'X'
        elif throw == 0:
            _frame_calc += .5
            GAME_RESULT += '-'
    return GAME_RESULT


start = game_set()
print(start)
