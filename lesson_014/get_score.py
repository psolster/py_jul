# -*- coding: utf-8 -*-


import bowling

result = bowling.result


def get_score(game_result):
    count_stike = game_result.count('X')
    count_second_throw = game_result.count('/')
    count_zero_throw = game_result.count('-')
    print('страйков->', count_stike)
    print('выбито со второго удара->', count_second_throw)
    print('нулевых->', count_zero_throw)


get_score(game_result=result)
