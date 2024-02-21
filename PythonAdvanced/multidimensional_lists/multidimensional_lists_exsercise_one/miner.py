matrix_size = int(input())
commands = input().split()

total_coal = 0
miner_row, miner_col = 0, 0
collected_coal = 0
matrix = []

moves = {
    "left": lambda x, y: (x, y - 1),
    "right": lambda x, y: (x, y + 1),
    "up": lambda x, y: (x - 1, y),
    "down": lambda x, y: (x + 1, y),
}

for row in range(matrix_size):
    matrix_row = [el for el in input().split()]
    total_coal += matrix_row.count("c")
    if "s" in matrix_row:
        miner_row, miner_col = row, matrix_row.index("s")
    matrix.append(matrix_row)

matrix[miner_row][miner_col] = "*"
cur_row, cur_col = miner_row, miner_col
for command in commands:

    next_row, next_col = moves[command](cur_row, cur_col)

    if 0 <= next_row < matrix_size and 0 <= next_col < matrix_size:
        cur_row, cur_col = next_row, next_col

        if matrix[cur_row][cur_col] == "c":
            collected_coal += 1
            matrix[cur_row][cur_col] = "*"

        elif matrix[cur_row][cur_col] == "e":
            print(f"Game over! ({cur_row}, {cur_col})")
            break

        if collected_coal == total_coal:
            print(f"You collected all coal! ({cur_row}, {cur_col})")
            break

    else:
        continue

else:
    left_coal = total_coal - collected_coal
    print(f"{left_coal} pieces of coal left. ({cur_row}, {cur_col})")
