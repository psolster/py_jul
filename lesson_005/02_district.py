# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join


from lesson_005.district.central_street.house1 import room1 as r1_cs_h1
from lesson_005.district.central_street.house1 import room2 as r2_cs_h1
from lesson_005.district.central_street.house2 import room1 as r1_cs_h2
from lesson_005.district.central_street.house2 import room2 as r2_cs_h2
from lesson_005.district.soviet_street.house1 import room1 as r1_ss_h1
from lesson_005.district.soviet_street.house1 import room2 as r2_ss_h1
from lesson_005.district.soviet_street.house2 import room1 as r1_ss_h2
from lesson_005.district.soviet_street.house2 import room2 as r2_ss_h2
all_people = (
        r1_cs_h1.folks + r2_cs_h1.folks +
        r1_cs_h2.folks + r2_cs_h2.folks +
        r1_ss_h1.folks + r2_ss_h1.folks +
        r1_ss_h2.folks + r2_ss_h2.folks)
print('На районе живут:')
print(', '.join(all_people))
