# -*- coding: utf-8 -*-
from random import randint
import sys


class GameSet:
    def __init__(self):
        self._game_result = ''
        self.all_frame_calc = 0
        self.frame_result = ''
        self.lost = 0

    def throw_now(self, n=10):
        max_ceg = n
        throw_result = randint(0, max_ceg)
        return throw_result

    def frame(self):
        # print('вошли в метод фрейма')
        throw_res = self.throw_now(n=10)
        _frame_calc = 0.0
        self.frame_result = ''
        if throw_res == 10:
            _frame_calc += 1
            self.frame_result += 'X'
        elif throw_res == 0:
            _frame_calc += .5
            self.frame_result += '-'
        else:
            _frame_calc += .5
            self.frame_result += str(throw_res)
            self.lost = 10 - throw_res
        if _frame_calc / 2 != 0.5:
            self.lost = 10 - throw_res
            do_throw = self.throw_now(self.lost)
            if do_throw == self.lost:
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
            else:
                return self.frame_result
        # self.all_frame_calc += 1
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


class Sum_Frame(Exception):
    def __init__(self):
        self.message = 'Не верное количество кеглей в фрейме'

    def __str__(self):
        return self.message


class GetScore:
    def __init__(self, ):
        self.total_count = 0

    def __str__(self):
        return str(self.total_count)

    def get_score(self, result_f_sc):
        try:
            self.error_control(result_f_sc)
        except FormatError as errr:
            print(f'Поймано исключение {str(errr)}')
            sys.exit()

        count_stike = result_f_sc.count('X')
        count_second_throw = result_f_sc.count('/')
        list_results = list(result_f_sc)
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

    def error_control(self, game_result):
        res_list = list(game_result)
        res_fram = []
        n = 0
        while n < len(res_list):
            symb = res_list[n]
            if symb == 'X':
                res_fram.append(symb)
                n += 1
            else:
                fram = res_list[n: n + 2]
                res_fram.append(fram)
                n += 2
        sum_each_fram = []
        for i in res_fram:
            if len(i) == 2:
                fram_sl = ''.join(i)
                if fram_sl.isdigit():
                    obr = list(fram_sl)
                    res_lst = [int(x) for x in obr]
                    sum_fram = sum(res_lst)
                elif '-' in i:
                    if i == ['-', '-']:
                        sum_fram = '0'
                    elif '/' in i:
                        sum_fram = 10
                    elif 'X' in i:
                        sum_fram = 10
                    else:
                        # print(i)
                        pos = i.index('-')
                        i[pos] = '0'
                        fram_sl = ''.join(i)
                        obr = list(fram_sl)
                        res_lst = [int(x) for x in obr]
                        sum_fram = sum(res_lst)
                else:
                    sum_fram = 10
                sum_each_fram.append(sum_fram)
            else:
                sum_each_fram.append(10)

        for sum_fr in sum_each_fram:
            try:
                if int(sum_fr) > 10:
                    raise Sum_Frame
            except Sum_Frame as exc_1:
                print(f'Исключение {exc_1}')

                try:
                    if len(res_fram) != 10:
                        raise FormatError
                except FormatError as exc:
                    print(f'Исключение {exc}')

                    continue

        for symb, i in enumerate(res_list):
            try:
                if i == '/':
                    if res_list[symb - 1].isdigit() or '-':
                        return False
                    else:
                        raise PosError()

            finally:
                continue
        return False

    def run(self, result_f_sc):
        result_gs = self.get_score(result_f_sc)
        return result_gs


if __name__ == "__main__":
    game = GameSet()
    result = game.run()
    start = GetScore()
    res = start.run(result)
    print(result, '-', res)
