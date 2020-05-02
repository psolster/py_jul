#!/usr/bin/env python3
# -*- coding: utf-8 -*-


my_family = ['я', 'аня', 'чигрыш']

my_family_height = [
    [my_family[0], 175],
    [my_family[1], 158],
    [my_family[2], 92]
]

print('рост ', my_family_height[0])


total_height = (
    my_family_height[0][1]
    + my_family_height[1][1]
    + my_family_height[2][1]
)

print('Общий рост семьи->', total_height)

# Зачёт!
