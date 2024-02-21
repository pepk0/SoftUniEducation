from math import pi

figure = input()

area = 0

if figure == "square":
    square_side = float(input())
    area = square_side ** 2

elif figure == "rectangle":
    rectangle_width = float(input())
    rectangle_length = float(input())
    area = rectangle_length * rectangle_width

elif figure == "circle":
    circle_radius = float(input())
    area = pi * circle_radius ** 2

elif figure == "triangle":
    triangle_base = float(input())
    triangle_height = float(input())
    area = triangle_base * triangle_height / 2

print(f"{area:.3f}")
