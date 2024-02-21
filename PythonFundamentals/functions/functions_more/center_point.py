from math import sqrt, floor


def find_distance(point_one: float, point_two: float) -> float:
    total = (abs(point_one) ** 2 + abs(point_two) ** 2)
    distance = sqrt(total)
    return distance


def compare_points(point_x: list, point_y: list) -> str:
    result = ""
    distance_point_x = find_distance(point_x[0], point_x[1])
    distance_point_y = find_distance(point_y[0], point_y[1])
    if distance_point_x > distance_point_y:
        point_one, point_two = point_y
    else:
        point_one, point_two = point_x

    result = f"({floor(point_one)}, {floor(point_two)})"
    return result


point_x_as_list = [float(input()) for _ in range(2)]
point_y_as_list = [float(input()) for _ in range(2)]
print(compare_points(point_x_as_list, point_y_as_list))
