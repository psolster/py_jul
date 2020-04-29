#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов
from pprint import pprint
sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# TODO: Идеально было бы если бы строки так не лепились друг к другу.
# TODO: Желательно пустую строку поставить после определения словаря distances
# TODO: также как после определения переменных moscow, london, paris:
distances = {}
moscow=sites['Moscow']
london=sites['London']
paris=sites['Paris']
# TODO: по сторонам операторов, включая оператор возведения в степень, должны быть пробелы:
moscow_london=((moscow[0]-london[0])**2+(moscow[1]-london[1])**2)**.5
moscow_paris=((moscow[0]-paris[0])**2+(moscow[1]-paris[1])**2)**.5
london_paris=((london[0]-paris[0])**2+(london[1]-paris[1])**2)**.5

# TODO: пробелов между ключей не должно быть. Т.е. как пример между ключём ['Moscow'] u ['london']:
distances['Moscow'] = {}
distances['Moscow'] ['London'] = moscow_london
distances['Moscow'] ['Paris'] = moscow_paris
distances['London'] = {}
distances['London'] ['Moscow'] = moscow_london
distances['London'] ['Paris'] = london_paris

distances['Paris'] = {}
distances['Paris'] ['Moscow'] = moscow_paris
distances['Paris'] ['London'] = london_paris

pprint(distances)
