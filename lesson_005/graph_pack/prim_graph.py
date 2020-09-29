import simple_draw as sd
sd.resolution = (1200, 600)


def primitivs(point_zero_fig, start_angle_figura, lenght_line, number_of_sides):
    start_fig = sd.get_point(*point_zero_fig)
    step_angle = 360 / number_of_sides
    angle_figura = [start_angle_figura]
    for i in range(1, number_of_sides+1):
        angle_figura.append(angle_figura[i - 1] + step_angle)
    v = sd.get_vector(start_point=start_fig, angle=angle_figura[0], length=lenght_line, width=3)
    v.draw()
    for i in range(1, number_of_sides):
        v = sd.get_vector(start_point=v.end_point, angle=angle_figura[i], length=lenght_line, width=3)
        v.draw()
    # sd.line(start_point=v.end_point, end_point=sd.get_point(*point_zero_fig), width=3)


if __name__ == "__main__":
    point_zero = (600, 300)
    length = 100
    angle = 45
    primitivs(point_zero_fig=point_zero, start_angle_figura=angle, lenght_line=length, number_of_sides=5)
    sd.pause()
