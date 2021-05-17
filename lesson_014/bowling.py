# -*- coding: utf-8 -*-
from random import randint


class GameSet:
    def __init__(self):
        self.GAME_RESULT = ''

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
                self.GAME_RESULT += str(self.throw)
                second_throw = self.ferst_throw()
                if second_throw >= lost:
                    self.GAME_RESULT += '/'
                    _frame_calc += .5
                elif second_throw == 0:
                    self.GAME_RESULT += '-'
                    _frame_calc += .5
                else:
                    self.GAME_RESULT += str(second_throw)
                    _frame_calc += .5
            elif self.throw == 10:
                _frame_calc += 1
                self.GAME_RESULT += 'X'
            elif self.throw == 0:
                _frame_calc += .5
                self.GAME_RESULT += '-'
        return self.GAME_RESULT


game = GameSet()
result = game.run()
print(result)
