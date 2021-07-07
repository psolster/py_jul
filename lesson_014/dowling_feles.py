# -*- coding: utf-8 -*-


import os
import bowling


def generate_tour(input_file, output_file):
    tour_data = {}
    file_whith_data = input_file
    file_for_data = output_file
    with open(file_whith_data, 'r', encoding='utf8') as rf:
        while True:
            line_for_analysis = rf.readline()
            if line_for_analysis == '':
                break
            elif '#' in line_for_analysis:
                print('start tour')
                line_for_analysis = next(rf)
                while 'winner' not in line_for_analysis:

                    name, res_set = line_for_analysis.split('\t')
                    tour_data[name] = res_set[:-1]
                    line_for_analysis = rf.readline()
                else:
                    print('Tour over')
                    yield tour_data

            else:
                continue


def calculate_tour_res(res_previous_tour):
    res_for_calc = res_previous_tour
    start = bowling.GetScore()
    result = start.run(res_for_calc)

    return result


input_file = 'tournament.txt'
output_file = 'tournament_out.txt'
start_read = generate_tour(input_file=input_file, output_file=output_file)
for line in start_read:

    for name, res in line.items():
        res_for_gamer = calculate_tour_res(res)
        print(name, res, res_for_gamer)



