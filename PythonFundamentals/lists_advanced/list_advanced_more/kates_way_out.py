def find_kate(matrix: list) -> tuple:
    kate_position = (0, 0)
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == "k":
                # third value used for moves count
                kate_position = (row, col, 1)
                return kate_position
    return kate_position


def mark_maze_moves(matrix: list) -> None:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    kate_position = find_kate(matrix)
    matrix[kate_position[0]][kate_position[1]] = 1
    queue = [kate_position]

    while queue:
        row, col, moves = queue.pop()
        for move in directions:
            new_row, new_col = move
            new_row = row + new_row
            new_col = col + new_col

            if (new_row < 0 or new_row >= len(matrix)) \
                    or (new_col < 0 or new_col >= len(matrix[0])):
                continue
            if matrix[new_row][new_col] == " ":
                matrix[new_row][new_col] = moves + 1
                queue.append((new_row, new_col, moves + 1))


def check_exits(matrix: list) -> str:
    mark_maze_moves(maze)
    cur_row = 0
    cur_col = 0
    longest_path = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for direction in directions:
        next_row, next_col = direction
        while True:
            new_row = cur_row + next_row
            new_col = cur_col + next_col
            if (new_row < 0 or new_row >= len(matrix)) \
                    or (new_col < 0 or new_col >= len(matrix[0])):
                break
            if type(matrix[new_row][new_col]) is int:
                if matrix[new_row][new_col] > longest_path:
                    longest_path = matrix[new_row][new_col]
            cur_row, cur_col = new_row, new_col
    if longest_path:
        return f"Kate got out in {longest_path} moves"
    return "Kate cannot get out"


maze = [[el for el in input()] for _ in range(int(input()))]
print(check_exits(maze))
# visualize maze
# for row in maze:
#     print(*row, sep=" ")
