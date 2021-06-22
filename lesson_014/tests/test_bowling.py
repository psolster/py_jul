# -*- coding: utf-8 -*-


import unittest
from unittest.mock import Mock

import bowling
from bowling import GetScore as GS

_test_date = '1--/418/22527/41243/'
_result_test_date = 88


class Get_Score_From_bowling_Test(unittest.TestCase):
    def test_get_score(self):
        count = bowling.GetScore()
        res = count.run(_test_date)
        self.assertEqual(res, _result_test_date)


if __name__ == '__main__':
    unittest.main()
