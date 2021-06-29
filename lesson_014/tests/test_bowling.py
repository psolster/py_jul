# -*- coding: utf-8 -*-
import unittest
import bowling

_test_date = '4152442234528-26-125'
_result_test_date = 62


class Get_Score_From_bowling_Test(unittest.TestCase):
    def test_get_score(self):
        count = bowling.GetScore()
        res = count.run(_test_date)
        self.assertEqual(res, _result_test_date)

    def test_error_control(self):
        count = bowling.GetScore()
        res = count.error_control(_test_date)
        self.assertEqual(res, False)


if __name__ == '__main__':
    unittest.main()
