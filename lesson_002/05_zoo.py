#!/usr/bin/env python
# -*- coding: utf-8 -*-

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

zoo.insert(1, 'bear')
print(zoo)

birds = ['rooster', 'ostrich', 'lark', ]

zoo.extend(birds)

print(zoo)

zoo.remove('elephant')
print(zoo)


print('Лев в клетке->', zoo.index('lion') + 1)
print('Жаворонок в клетке->', zoo.index('lark') + 1)

# Зачёт!
