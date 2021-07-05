# -*- coding: utf-8 -*-


import os


def generate_tour(input_file, output_file):
    tour_data = {}
    file_whith_data = input_file
    file_for_data = output_file
    with open(file_whith_data, 'r', encoding='utf8') as rf:
        line = rf.readline()
        if line[4:8] == 'Tour':
            print('Началоо нового тура')
            while True:
                line_for_calc = rf.readline()
                if line_for_calc[0:6] != 'winner':
                    name, res_tour = line_for_calc.split('\t')
                    tour_data[name] = res_tour

                    with open(file_for_data, 'a', encoding='utf8') as rt:
                        rt.write(line_for_calc)
                        print('записали игрока')
                else:
                    print('Тур сформирован')
                    yield tour_data
                    # break
        else:
            print('Не верная структура файла')


input_file = 'tournament.txt'
output_file = 'tournament_out.txt'
start_read = generate_tour(input_file=input_file, output_file=output_file)
for line in start_read:
    print(line)
