from math import pi

circle_radius = float(input())

area_circle = pi * (circle_radius ** 2)
perimeter_circle = (pi * 2) * circle_radius

print(f"{area_circle:.2f}")
print(f"{perimeter_circle:.2f}")