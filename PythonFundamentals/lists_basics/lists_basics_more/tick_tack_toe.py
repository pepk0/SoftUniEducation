def check_horizontal(matrix: list) -> int:
    element = 0
    for row in range(3):
        element = matrix[row][0]
        for column in range(1, 3):
            if matrix[row][column] != element:
                element = 0
                break
        # if the break is not triggered, this means the row is 
        # filled with the same elements, and that is the winner
        else:
            break
    return element


def check_vertical(matrix: list) -> int:
    element = 0
    for column in range(3):
        element = matrix[0][column]
        for row in range(1, 3):
            if matrix[row][column] != element:
                element = 0
                break
        # if the break is not triggered, this means the column is 
        # filled with same elements, and that is the winner
        else:
            break
    return element


def check_diagonal(matrix: list) -> int:
    element = 0
    middle = matrix[1][1]
    if (matrix[0][0] == matrix[1][1] == matrix[-1][-1] or
            matrix[2][0] == matrix[1][1] == matrix[0][2]):
        element = middle
    return element


game_board = [[int(s) for s in input().split()] for _ in range(3)]
checks = [check_diagonal, check_horizontal, check_vertical]
result = 0
for check in checks:
    result += check(game_board)

winner = "Draw!"
if result:
    if result == 1:
        winner = "First player"
    else:
        winner = "Second player"
    print(f"{winner} won")
else:
    print(winner)
