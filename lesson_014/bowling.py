# -*- coding: utf-8 -*-
from random import randint

GAME_RESULT = ''


def throw():
    throw_result = randint(0, 10)
    return throw_result


def game_set():
    print('вошли в фрейм игры')
    global GAME_RESULT
    global _frame_calc
    _frame_calc = 0.0
    full_frame = True

    while _frame_calc < 10:
        ferst_throw = throw()
        lost_numder = 10 - ferst_throw
        _frame_calc += .5
        if ferst_throw == 10:
            full_frame = True
            _frame_calc += 1
            GAME_RESULT += 'X'
        elif ferst_throw == 0:
            full_frame = False
            _frame_calc = .5
            GAME_RESULT += str(ferst_throw)
        else:
            GAME_RESULT += str(ferst_throw)
            second_throw = throw()
            if second_throw == 0:
                GAME_RESULT += '-'
                _frame_calc = .5
                full_frame = True
            else:
                if second_throw >= lost_numder:
                    GAME_RESULT += '/'
                    _frame_calc = .5
                    full_frame = True
                else:
                    GAME_RESULT += str(second_throw)
                    _frame_calc += .5

    return GAME_RESULT


start = game_set()
print(start)
