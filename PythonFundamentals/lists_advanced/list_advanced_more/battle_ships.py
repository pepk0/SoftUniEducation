def attack_position(row: int, col: int, matrix: list) -> int:
    result = 0
    if matrix[row][col] == 0:
        return result
    else:
        if matrix[row][col] - 1 == 0:
            result = 1
        matrix[row][col] -= 1
    return result


def attack_ships(coordinates: list, matrix: list) -> int:
    sunken_ships = 0
    for cur_row, cur_col in coordinates:
        sunken_ships += attack_position(cur_row, cur_col, matrix)
    return sunken_ships


battlefield = [[int(i) for i in input().split()] for _ in range(int(input()))]
attack_coordinates = [tuple(int(i) for i in el.split("-"))
                      for el in input().split()]
print(attack_ships(attack_coordinates, battlefield))
# visualize the battlefield matrix
# for row in battlefield:
#     print(*row, sep=" ")
