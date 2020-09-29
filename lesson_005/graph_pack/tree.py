import simple_draw as sd
sd.resolution = (1200, 600)


def draw_branches(start_point_brench, angle_brench, lenght_brench):
    if lenght_brench < 2:
        return

    v1 = sd.get_vector(start_point_brench, angle_brench, lenght_brench, width=1)
    v1.draw()
    deviation_size = 30-(30 * (sd.random_number(0, 40) / 100))
    deviation_size_lenght = .75 - (.75 * (sd.random_number(0, 40) / 100))
    delta_angle_1 = angle_brench - deviation_size
    delta_angle_2 = angle_brench + deviation_size
    next_lenght_branches = lenght_brench * deviation_size_lenght
    draw_branches(start_point_brench=v1.end_point, angle_brench=delta_angle_1, lenght_brench=next_lenght_branches)
    draw_branches(start_point_brench=v1.end_point, angle_brench=delta_angle_2, lenght_brench=next_lenght_branches)


if __name__ == '__main__':

    start_point = sd.get_point(600, 30)
    draw_branches(start_point_brench=start_point, angle_brench=90, lenght_brench=100)

# Пригодятся функции
# sd.random_number()

sd.pause()
