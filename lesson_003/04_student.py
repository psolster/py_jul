# -*- coding: utf-8 -*-

educational_grant, expenses = 10000, 12000

i = 0
sum_expenses = 0
while i < 10:

    sum_expenses = sum_expenses + expenses - educational_grant
    expenses *= 1.03

    i += 1
print("Студенту надо попросить", sum_expenses )
