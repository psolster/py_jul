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

                line_for_analysis = next(rf)
                while 'winner' not in line_for_analysis:
                    name, res_set = line_for_analysis.split('\t')
                    tour_data[name] = res_set[:-1]
                    line_for_analysis = rf.readline()
                else:
                    yield tour_data
                    tour_data = {}
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
tour_number = 0
for line in start_read:
    tour_number += 1
    print('Тур номер - ', tour_number)
    rw = open(output_file, 'a', encoding='utf8')
    rw.write('### Tour ' + str(tour_number) + '\n')
    voc_result_tour = {}
    for name, res in line.items():
        res_for_gamer = calculate_tour_res(res)
        voc_result_tour[name] = res_for_gamer
    sorted_tuple = sorted(voc_result_tour.items(), key=lambda x: x[1])
    for name_pl, res_gam in line.items():
        rw.write(name_pl+'\t'+str(res_gam)+'\t'+str(voc_result_tour[name_pl])+'\n')
    rw.write('Winner is '+str(sorted_tuple[-1][0]+'\n'))

    rw.write('\n')
    rw.close()
