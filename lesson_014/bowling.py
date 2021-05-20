# -*- coding: utf-8 -*-
from random import randint


class GameSet:
    def __init__(self):
        self._game_result = ''

    def ferst_throw(self):
        throw_result = randint(0, 10)
        return throw_result

    def run(self):
        print('вошли в фрейм игры')
        _frame_calc = 0.0
        while _frame_calc < 10:
            self.throw = self.ferst_throw()
            lost = 10 - int(self.throw)
            if 1 <= self.throw <= 9:
                _frame_calc += .5
                self._game_result += str(self.throw)
                second_throw = self.ferst_throw()
                if second_throw >= lost:
                    self._game_result += '/ '
                    _frame_calc += .5
                elif second_throw == 0:
                    self._game_result += '- '
                    _frame_calc += .5
                else:
                    self._game_result += str(second_throw) + ' '
                    _frame_calc += .5
            elif self.throw == 10:
                _frame_calc += 1
                self._game_result += 'X '
            elif self.throw == 0:
                _frame_calc += .5
                self._game_result += ' -'
        return self._game_result


game = GameSet()
result = game.run()
print(result)
