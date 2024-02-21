def check_valid(row: int, col: int, matrix: list) -> bool:
    return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])


def knight_challenges(row_, col_, matrix: list) -> set:
    knights_threatened = set()

    knight_moves = ((2, 1), (2, -1), (1, 2), (1, -2),
                    (-2, -1), (-2, 1), (-1, -2), (-1, 2))

    for knight_row, knight_col in knight_moves:
        if not check_valid(knight_row + row_, knight_col + col_, matrix):
            continue
        elif matrix[knight_row + row_][knight_col + col_] == "K":
            knights_threatened.add((knight_row + row_, knight_col + col_))

    return knights_threatened


chess_board = [[el for el in input()] for _ in range(int(input()))]
knight_attacks = {}

for row in range(len(chess_board)):
    for col in range(len(chess_board[0])):

        if chess_board[row][col] == "K":
            knight_attacks[(row, col)] = knight_challenges(
                row, col, chess_board)

removed = 0

while True:

    biggest_threat = 0
    attacking_knight = None

    for knight, numb_threats in knight_attacks.items():
        if len(numb_threats) > biggest_threat:
            biggest_threat = len(numb_threats)
            attacking_knight = knight

    if attacking_knight:
        knight_attacks.pop(attacking_knight)
        removed += 1

        for num_threats in knight_attacks.values():
            if attacking_knight in num_threats:
                num_threats.remove(attacking_knight)
    else:
        break

print(removed)
