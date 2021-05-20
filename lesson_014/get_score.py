# -*- coding: utf-8 -*-


import bowling

result = bowling.result


class FormatError(Exception):
    pass


def get_score(game_result):
    err = error_control(game_result)
    try:
        if not err:

            count_stike = game_result.count('X')
            count_second_throw = game_result.count('/')
            list_results = list(game_result)
            for i, symb in enumerate(list_results):
                if symb == 'X':
                    list_results[i] = '0'
                elif symb == '/':
                    list_results[i - 1] = '0'
                    list_results[i] = '0'
                elif symb == '-':
                    list_results[i] = '0'
            result = [int(item) for item in list_results]
            total_count = count_stike * 20 + count_second_throw * 15 + sum(result)
    except FormatError:
        print('не те запси')
    return total_count


def error_control(game_result):
    try:
        if game_result in 'X/':
            raise FormatError
    except print('ошибка формата'):
        print('не прошло')

    return False



start = get_score(game_result=result)
print(result, '-', start)
