# -*- coding: utf-8 -*-
from random import randint


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


if __name__ == "__main__":
    game = GameSet()
    result = game.run()

