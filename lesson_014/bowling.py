# -*- coding: utf-8 -*-
from random import randint

GAME_RESULT = ''


def throw():
    throw_result = randint(0, 10)
    return throw_result


def game_set():
    print('вошли в фрейм игры')
    global GAME_RESULT
    _frame_calc = 0.0
    _frame_stage = False
    while _frame_calc < 10:
        frame_throw = throw()
        lost = 10-frame_throw
        if frame_throw == 10:
            _frame_stage = True
            _frame_calc += 1
            GAME_RESULT += 'X'
        elif frame_throw == 0:
            GAME_RESULT += '-'
            _frame_calc += .5
        else:
            GAME_RESULT += str(frame_throw)
            _frame_calc += .5
        second_throw = throw()
        if second_throw < lost:
            GAME_RESULT += str(second_throw)
            _frame_calc += .5
        else:
            GAME_RESULT += '/'
            _frame_calc += .5

    return GAME_RESULT


start = game_set()
print(start)
