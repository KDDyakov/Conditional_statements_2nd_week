from math import pi

figure = input()

if figure == "square":
    square_side = float(input())
    S = square_side * square_side
elif figure == "rectangle":
    rectangle_side_first = float(input())
    rectangle_side_second = float(input())
    S = rectangle_side_first * rectangle_side_second
elif figure == "circle":
    circle_radius = float(input())
    S = pi * (circle_radius * circle_radius)
elif figure == "triangle":
    triangle_length = float(input())
    triangle_height = float(input())
    S = (triangle_height * triangle_length) / 2
print(f'{S:.3f}')