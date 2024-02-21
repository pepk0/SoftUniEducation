def out_of_bonds(row_: int, col_: int, matrix_size_: int) -> tuple:
    if row_ < 0:
        return matrix_size_ - 1, col_
    elif row_ >= matrix_size_:
        return 0, col_
    elif col_ >= matrix_size_:
        return row_, 0
    elif col_ < 0:
        return row_, matrix_size_ - 1

    return row_, col_


matrix_size = int(input())
boat_row, boat_col = 0, 0
ocean = []
catch = 0
sunk = False

for row in range(matrix_size):
    matrix_row = [int(el) if el.isdigit() else el for el in input()]
    if "S" in matrix_row:
        boat_row, boat_col = row, matrix_row.index("S")
    ocean.append(matrix_row)

ocean[boat_row][boat_col] = "-"

moves = {
    "down": (1, 0),
    "up": (-1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

command = input()

while command != "collect the nets":
    new_row, new_col = moves[command]

    boat_row, boat_col = out_of_bonds(new_row + boat_row, boat_col + new_col,
                                      matrix_size)

    if isinstance(ocean[boat_row][boat_col], int):
        catch += ocean[boat_row][boat_col]
    elif ocean[boat_row][boat_col] == "W":
        catch = 0
        sunk = True

    ocean[boat_row][boat_col] = "-"

    if sunk:
        break

    command = input()

ocean[boat_row][boat_col] = "S"

if sunk:
    print("You fell into a whirlpool! The ship sank and you lost the fish you "
          f"caught. Last coordinates of the ship: [{boat_row},{boat_col}]")
elif catch >= 20:
    print("Success! You managed to reach the quota!")
elif catch < 20:
    left_over = 20 - catch
    print(f"You didn't catch enough fish and didn't reach the "
          f"quota! You need {left_over} tons of fish more.")

if catch:
    print(f"Amount of fish caught: {catch} tons.")

if not sunk:
    [print(*row, sep="") for row in ocean]
