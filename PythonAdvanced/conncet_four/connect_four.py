import os


def in_matrix(row: int, col: int, matrix: list) -> bool:
    return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])


def create_game_board(rows: int, cols: int) -> list:
    return [[0] * cols for _ in range(rows)]


def print_matrix(matrix: list) -> None:
    print()
    [print("|" + "|".join(" " if el == 0 else str(el) for el in row) + "|")
     for row in matrix]
    # dynamically adjust bottom of game board for any length of columns
    print("-".join("+" * (len(matrix[0]) + 1)), "\n")


def get_int(pomp: str) -> int:
    while True:
        try:
            return int(input(pomp))
        except ValueError:
            print("Please enter a valid integer value!")


def get_valid_col(matrix: list, player: str, cols: int) -> int:
    col = get_int(f"{player}, chose a column: ") - 1  # off by one for index
    valid_col = False

    while not valid_col:

        while not 0 <= col < len(matrix[0]):
            col = get_int(
                f"Please enter a valid column in the range 1 - {cols}: ") - 1

        if matrix[0][col] == 0:
            valid_col = True
        else:
            col = -1
            print("Colum in full")
            continue

    return col


def place_player_move(col_to_place: int, matrix: list, player: str,
                      rows: int) -> tuple:

    player_number = 1 if player == "Player one (1)" else 2

    for row in range(rows):
        if matrix[row][col_to_place] == 0:
            continue
        else:
            matrix[row - 1][col_to_place] = player_number
            return (row - 1, col_to_place)
    else:
        matrix[rows - 1][col_to_place] = player_number
        return (rows - 1, col_to_place)


def check_for_winner(row: int, col: int, matrix: list, win_chain: int) -> int:
    directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]
    cur_row, cur_col = row, col
    checking = matrix[row][col]

    while directions:

        next_row, next_col = directions.pop()
        connected = 1

        for i in range((win_chain * 2) - 2):
            
            # after checking n - 1 elements in one direction,
            # we switch and look back
            if i == win_chain - 1:
                cur_row, cur_col = row, col
                next_row, next_col = next_row * -1, next_col * -1

            cur_row, cur_col = next_row + cur_row, next_col + cur_col

            if in_matrix(cur_row, cur_col, matrix):
                if matrix[cur_row][cur_col] == checking:
                    connected += 1

            if connected >= win_chain:
                return checking

        cur_row, cur_col = row, col

    return 0


def main() -> None:
    # you can chose any num for row or col, but keep in mind that big numbers
    # will look odd in the terminal, standard connect4 board => 6, 7
    ROWS, COLS = 6, 7
    # number of connections for winning, standard connect4 => 4
    CONNECT = 4

    game_board = create_game_board(ROWS, COLS)
    winner = None
    turn = 0

    while turn < ROWS * COLS:
        print_matrix(game_board)

        player_turn = "Player one (1)" if turn % 2 == 0 else "Player two (2)"

        to_place = get_valid_col(game_board, player_turn, COLS)
        row, col = place_player_move(to_place, game_board, player_turn, ROWS)

        winner = check_for_winner(row, col, game_board, CONNECT)

        if winner:
            break

        turn += 1

        os.system("cls")  # clears the terminal

    os.system("cls")
    print_matrix(game_board)

    player_won = "Player one (1)" if winner == 1 else "Player two (2)"
    print(f"Winner ==> {player_won}" if winner else "Game Over! - DRAW!", "\n")


if __name__ == "__main__":
    main()
