def check_valid(row: int, col: int,) -> bool:
    return 0 <= row < 5 and 0 <= col < 5


def move(directions: tuple, steps: int, cur_row: int, cur_col: int) -> tuple:
    direction_row, direction_col = directions

    new_row, new_col = cur_row + \
        (direction_row * steps), cur_col + (direction_col * steps)

    if check_valid(new_row, new_col) and field[new_row][new_col] != "x":
        return new_row, new_col

    return cur_row, cur_col


def shoot(direction: tuple, cur_row: int, cur_col: int) -> list:
    new_row, new_col = direction
    targets_downed = []

    while check_valid(cur_row + new_row, cur_col + new_col):

        if field[cur_row + new_row][cur_col + new_col] == "x":
            targets_downed.append([cur_row + new_row, cur_col + new_col])
            field[cur_row + new_row][cur_col + new_col] = "."
            break

        cur_row, cur_col = new_row + cur_row, new_col + cur_col

    return targets_downed


total_targets = 0
player_row, player_col = 0, 0
field = []

moves = {
    "down": (1, 0),
    "up": (-1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(5):
    field_row = [el for el in input().split()]

    if "A" in field_row:
        player_row, player_col = row, field_row.index("A")
    total_targets += field_row.count("x")

    field.append(field_row)

shot_targets = []

for _ in range(int(input())):

    command, direction, *steps = input().split()

    if command == "move":
        field[player_row][player_col] = "."
        path = moves[direction]
        new_row, new_col = move(path, int(steps[0]), player_row, player_col)
        player_row, player_col = new_row, new_col
        field[new_row][new_col] = "A"

    elif command == "shoot":
        path = moves[direction]
        targets_hit = shoot(path, player_row, player_col)
        if targets_hit:
            shot_targets.extend(targets_hit)

    if len(shot_targets) == total_targets:
        print(f"Training completed! All {len(shot_targets)} targets hit.")
        break
else:
    print(f"Training not completed! "
          f"{total_targets - len(shot_targets)} targets left.")

print(*shot_targets, sep="\n")
