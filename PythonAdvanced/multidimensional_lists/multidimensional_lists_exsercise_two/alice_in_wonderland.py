def check_valid(row: int, col: int, matrix: list) -> bool:
    return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])


matrix_size = int(input())

field = []
alice_row, alice_col = 0, 0

for row in range(matrix_size):
    field_row = [int(i) if i.isdigit() else i for i in input().split()]

    if "A" in field_row:
        alice_row, alice_col = row, field_row.index("A")

    field.append(field_row)

moves = {
    "down": (1, 0),
    "up": (-1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

count_tea = 0
field[alice_row][alice_col] = "*"
finished = False

while count_tea < 10:

    move = input()
    next_row, next_col = moves[move]

    if check_valid(alice_row + next_row, alice_col + next_col, field):

        if type(field[alice_row + next_row][alice_col + next_col]) == int:
            count_tea += field[alice_row + next_row][alice_col + next_col]
        elif field[alice_row + next_row][alice_col + next_col] == "R":
            finished = True
    else:
        break

    field[alice_row + next_row][alice_col + next_col] = "*"

    if finished:
        break

    alice_row, alice_col = next_row + alice_row, alice_col + next_col

print("Alice didn't make it to the tea party." if count_tea <
      10 else "She did it! She went to the party.")

[print(*row, sep=" ") for row in field]
