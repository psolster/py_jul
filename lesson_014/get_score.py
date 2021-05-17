# -*- coding: utf-8 -*-


import bowling

result = bowling.result


def get_score(game_result):
    count_stike = game_result.count('X')
    count_second_throw = game_result.count('/')
    list_results = list(game_result)

    for i, symb in enumerate(list_results):
        if symb == 'X':

            list_results[i] = '0'
        elif symb == '/':
            list_results[i-1] = '0'
            list_results[i] = '0'
        elif symb == '-':
            list_results[i] = '0'

    result = [int(item) for item in list_results]
    total_count = count_stike*20+count_second_throw*15+sum(result)
    return total_count


start = get_score(game_result=result)
print(result, '-', start)
