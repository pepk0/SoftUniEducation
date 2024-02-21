def find_connected_areas(row: int, col: int, matrix: list) -> int:
    # recursive base case
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return 0
    if matrix[row][col] != ".":
        return 0
    # We set the current position to "1" so we don't search for it again,
    # and so we can visualize it better when we print the matrix
    matrix[row][col] = "1"
    result = 1
    result += find_connected_areas(row + 1, col, matrix)
    result += find_connected_areas(row - 1, col, matrix)
    result += find_connected_areas(row, col + 1, matrix)
    result += find_connected_areas(row, col - 1, matrix)
    return result


def get_longest_area(matrix: list) -> int:
    result = 0
    for cur_row in range(len(maze)):
        for cur_col in range(len(maze[0])):
            connected_area = find_connected_areas(cur_row, cur_col, matrix)
            if connected_area > result:
                result = connected_area
    return result


maze = [[el for el in input().split()] for _ in range(int(input()))]
print(get_longest_area(maze))
# visualize maze
# for row in maze:
#     print(*row, sep=" ")
