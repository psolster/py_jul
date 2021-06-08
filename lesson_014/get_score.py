# -*- coding: utf-8 -*-


import bowling

result = bowling.GameSet.run


class FormatError(Exception):

    def __init__(self):
        self.message = 'Ошибка количества фреймов'

    def __str__(self):
        return self.message


class PosError(Exception):

    def __init__(self):
        self.message = 'Символ / не на своем месте'

    def __str__(self):
        return self.message


def get_score(game_result):
    try:
        error_control(game_result)
    except FormatError as errr:
        print(f'Поймано исключение {str(errr)}')

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

    return total_count


def error_control(game_result):
    result_for_control = list(game_result)
    strike = result_for_control.count('X')
    all_lenght = len(result_for_control) + strike * 2
    try:
        if all_lenght != 20:
            raise FormatError()
        else:
            return False
    finally:

        for symb, i in enumerate(result_for_control):
            try:
                if symb == '/':
                    if result_for_control[i - 1].isdigit():
                        return False
                    else:
                        raise PosError()
            finally:
                pass


if __name__ == "__main__":
    start = get_score(game_result=result)
    print(result, '-', start)
