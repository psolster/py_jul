#!/usr/bin/env python
# -*- coding: utf-8 -*-

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}


store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
print('Лампа -', store[goods['Лампа']][0]['quantity'], 'шт, стоимость', lamps_cost, 'руб')


table_cost = (
    store[goods['Стол']][0]['quantity']
    * store[goods['Стол']][0]['price']
    + store[goods['Стол']][1]['quantity']
    * store[goods['Стол']][1]['price']
)
kolvo_stolov = (

    store[goods['Стол']][0]['quantity']
    + store[goods['Стол']][1]['quantity']
)
print('Стол -', kolvo_stolov, 'шт, стоимость', table_cost, 'руб')

sofa_cost = (
    store[goods['Диван']][0]['quantity']
    * store[goods['Диван']][0]['price']
    + store[goods['Диван']][1]['quantity']
    * store[goods['Диван']][1]['price']
)

kolvo_sofa = (
    store[goods['Диван']][0]['quantity']
    + store[goods['Диван']][1]['quantity']
)

print('Диван -', kolvo_sofa, 'шт, стоимость', sofa_cost, 'руб')

taburet_cost = (
    store[goods['Стул']][0]['quantity']
    * store[goods['Стул']][0]['price']
    + store[goods['Стул']][1]['quantity']
    * store[goods['Стул']][1]['price']
    + store[goods['Стул']][2]['quantity']
    * store[goods['Стул']][2]['price']
)

kolvo_taburet = (
    store[goods['Стул']][0]['quantity']
    + store[goods['Стул']][1]['quantity']
    + store[goods['Стул']][2]['quantity']
)

print('Стул -', kolvo_taburet, 'шт, стоимость', taburet_cost, 'руб')

# Зачёт!
