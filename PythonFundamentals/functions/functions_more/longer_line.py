from math import sqrt, floor


def calculate_length(side_a: int, side_b: int) -> float:
    total = side_a ** 2 + side_b ** 2
    distance = sqrt(total)
    return distance


def compare_lines(line_one: list, line_two: list) -> str:
    result = ""
    line_one_a, line_one_b = abs(sum(line_one[0])), abs(sum(line_one[1]))
    line_two_a, line_two_b = abs(sum(line_two[0])), abs(sum(line_two[1]))
    length_line_one = calculate_length(line_one_a, line_one_b)
    length_line_two = calculate_length(line_two_a, line_two_b)

    if length_line_one > length_line_two:
        distance_center_a = calculate_length(line_one[0][0], line_one[0][1])
        distance_center_b = calculate_length(line_one[1][0], line_one[1][1])
        if distance_center_a <= distance_center_b:
            point_one, point_two = line_one[0]
            point_three, point_four = line_one[1]
        else:
            point_one, point_two = line_one[1]
            point_three, point_four = line_one[0]
    else:
        distance_center_a = calculate_length(line_two[0][0], line_two[0][1])
        distance_center_b = calculate_length(line_two[1][0], line_two[1][1])
        if distance_center_a <= distance_center_b:
            point_one, point_two = line_two[0]
            point_three, point_four = line_two[1]
        else:
            point_one, point_two = line_two[1]
            point_three, point_four = line_two[0]

    result = (f"({floor(point_one)}, {floor(point_two)})"
              f"({floor(point_three)}, {floor(point_four)})")

    return result


line_one_list = [[float(input()) for _ in range(2)] for _ in range(2)]
line_two_list = [[float(input()) for _ in range(2)] for _ in range(2)]
print(compare_lines(line_one_list, line_two_list))
