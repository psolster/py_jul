# -*- coding: utf-8 -*-
from random import randint
import sys


class GameSet:
    def __init__(self):
        self._game_result = ''
        self.all_frame_calc = 0
        self.frame_result = ''
        self.lost = 0

    def throw_now(self):
        throw_result = randint(0, 10)
        return throw_result

    def frame(self):

        # print('вошли в метод фрейма')
        throw_res = self.throw_now()
        _frame_calc = 0.0
        self.frame_result = ''
        if throw_res == 10:
            _frame_calc += 1
            self.frame_result = 'X'
        elif throw_res == 0:
            _frame_calc += .5
            self.frame_result += '-'
        else:
            _frame_calc += .5
            self.frame_result += str(throw_res)
            self.lost = 10 - throw_res
        if _frame_calc < 1:
            do_throw = self.throw_now()
            if do_throw >= self.lost:
                self.frame_result += '/'
                _frame_calc += .5
                return self.frame_result
            elif do_throw == 0:
                self.frame_result += '-'
                _frame_calc += .5
                return self.frame_result
            elif do_throw < self.lost:
                self.frame_result += str(do_throw)
                _frame_calc += .5
                return self.frame_result
        self.all_frame_calc += 1
        # print(self.frame_result)
        return self.frame_result

    def game(self):
        # print('начинаем перебирать фреймы')
        while self.all_frame_calc < 10:
            # print('фрейм', self.all_frame_calc)
            game_res = self.frame()
            self._game_result += str(game_res)
            self.all_frame_calc += 1
        return self._game_result

    def run(self):
        print('вошли в запуск игры')
        start = self.game()
        return start


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
        sys.exit()

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
    game = GameSet()
    result = game.run()
    start = get_score(result)
    print(result, '-', start)
