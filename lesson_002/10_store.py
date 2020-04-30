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

# TODO: Я вам честно скажу - такое оформление кода меня совершенно не радует.
# TODO: Особенно не радует перенос строки прямо при обращении к ключу словаря.
# TODO: На всякий случай ещё раз укажу как форматировать подобные выражения, ниже, отформатируйте по подобию:
table_cost = store[goods['Стол']][0]['quantity'] * store[goods['Стол']][0]['price'] + store[goods['Стол']][1][
    'quantity'] * store[goods['Стол']][1]['price']
print('Стол -', store[goods['Стол']][0]['quantity'] + store[goods['Стол']][1]['quantity'], 'шт, стоимость', table_cost,
      'руб')

sofa_cost = store[goods['Диван']][0]['quantity'] * store[goods['Диван']][0]['price'] + store[goods['Диван']][1][
    'quantity'] * store[goods['Диван']][1]['price']
print('Диван -', store[goods['Диван']][0]['quantity'] + store[goods['Диван']][1]['quantity'], 'шт, стоимость',
      sofa_cost, 'руб')

taburet_cost = store[goods['Стул']][0]['quantity'] * store[goods['Стул']][0]['price'] + store[goods['Стул']][1][
    'quantity'] * store[goods['Стул']][1]['price'] + store[goods['Стул']][2]['quantity'] * store[goods['Стул']][2][
                   'price']
print('Стул -',
      store[goods['Стул']][0]['quantity'] + store[goods['Стул']][1]['quantity'] + store[goods['Стул']][2]['quantity'],
      'шт, стоимость', taburet_cost, 'руб')

# TODO: Пример того о чём говорится. Обратите внимание что заметки преподавателя и примеры кода тоже нужно удалять.
# TODO: Поскольку должен оставаться только ваш код в файлах.
# NOTE: Т.е. как пример у нас есть подобные данные:
example_data = [
    ["some_data", 100],
    ["some_other_data", 200]
]

# NOTE: И мы вычисляем эти данные в столбик:
some_calculations = (
    example_data[0][1]
    + example_data[1][1]
)
print("Результат вычислений:", some_calculations)

# NOTE: Правила простые: открывающая скобка после оператора присваивания (=);
# NOTE: закрывающая скобка в начале строки;
# NOTE: скобки не должны быть на одной строке с операторами и операндами;
# NOTE: оператор должен идти перед операндом;
# NOTE: должно быть 4 пробела отступов.

# NOTE: Вот, пусть послужит вам примером и сделайте аналогично ваши вычисления выше.
