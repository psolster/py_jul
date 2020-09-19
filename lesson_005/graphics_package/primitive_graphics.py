import simple_draw as sd


def primitivs(point_zero_fig, start_angle_figura, lenght_line, number_of_sides):
    sd.resolution = (1200, 600)
    step_angle = 360 / number_of_sides
    angle_figura = [start_angle_figura]
    for i in range(1, number_of_sides + 1):
        angle_figura.append(angle_figura[i - 1] + step_angle)

    v = sd.get_vector(start_point=point_zero_fig, angle=angle_figura[0], length=lenght_line, width=3)
    v.draw()
    for i in range(1, number_of_sides - 1):
        v = sd.get_vector(start_point=v.end_point, angle=angle_figura[i], length=lenght_line, width=3)
        v.draw()
    l = sd.line(start_point=v.end_point, end_point=point_zero_fig, width=3)


point_zero = sd.get_point(600, 300)
length = 120
angle = 30

primitivs(point_zero_fig=point_zero, start_angle_figura=angle, lenght_line=length, number_of_sides=7)
sd.pause()
