house_height = float(input())
side_wall_width = float(input())
height_triangle_side = float(input())

side_walls_area = (house_height * side_wall_width - (1.5 * 1.5)) * 2
back_wall = house_height ** 2
front_wall = back_wall - 1.2 * 2 # door area
green_paint_liters = (side_walls_area + back_wall + front_wall) / 3.4

roof_sides = (house_height * side_wall_width) * 2
roof_front_back = house_height * height_triangle_side
red_paint_liters = (roof_sides + roof_front_back) / 4.3

print(f"{green_paint_liters:.2f}")
print(f"{red_paint_liters:.2f}")