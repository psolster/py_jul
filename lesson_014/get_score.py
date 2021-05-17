# -*- coding: utf-8 -*-


import bowling

result = bowling.result


def get_score(game_result):
    count_stike = game_result.count('X')
    count_second_throw = game_result.count('/')
    # count_zero_throw = game_result.count('-')
    # print('страйков->', count_stike)
    # print('выбито со второго удара->', count_second_throw)
    # print('нулевых->', count_zero_throw)

    list_results = list(game_result)
    print(list_results)
    for i, symb in enumerate(list_results):
        if symb == 'X':
            print(i, symb)
            list_results[i] = '0'
        elif symb == '/':
            list_results[i-1] = '0'
            list_results[i] = '0'
        elif symb == '-':
            list_results[i] = '0'

    print(list_results)
    result = [int(item) for item in list_results]
    print('счет игры->', count_stike*20+count_second_throw*15+sum(result))





get_score(game_result=result)
