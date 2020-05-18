# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

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

for name in goods:
    art = goods[name]
    total_quon = 0
    total_cost = 0
    inform = store[art]
    for soder in enumerate(inform):
        soder_vok = soder[1]
        total_cost += soder_vok["quantity"] * soder_vok["price"]
        total_quon += soder_vok["quantity"]
    print(name, total_quon, "шт", "стоимость", total_cost)









