import simple_draw as sd

sd.resolution = (1200, 600)


def draw_branches(start_point_branch, angle_branch, length_branch):
    if length_branch < 2:
        return

    v1 = sd.get_vector(start_point_branch, angle_branch, length_branch, width=1)
    v1.draw()
    deviation_size = 30 - (30 * (sd.random_number(0, 40) / 100))
    deviation_size_length = .75 - (.75 * (sd.random_number(0, 40) / 100))
    delta_angle_1 = angle_branch - deviation_size
    delta_angle_2 = angle_branch + deviation_size
    next_length_branches = length_branch * deviation_size_length
    draw_branches(start_point_branch=v1.end_point, angle_branch=delta_angle_1, length_branch=next_length_branches)
    draw_branches(start_point_branch=v1.end_point, angle_branch=delta_angle_2, length_branch=next_length_branches)


if __name__ == '__main__':
    start_point = sd.get_point(600, 30)
    draw_branches(start_point_branch=start_point, angle_branch=90, length_branch=100)
    sd.pause()
