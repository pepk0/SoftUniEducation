def happy_santa(presents: int, presents_given: int):
    for new_row, new_col in moves.values():

        if matrix[new_row + santa_row][new_col + santa_col] in "XV":
            if matrix[new_row + santa_row][new_col + santa_col] == "V":
                presents_given += 1

            matrix[new_row + santa_row][new_col + santa_col] = "-"
            presents -= 1

        if not presents:
            break

    return presents, presents_given


moves = {
    "down": (1, 0),
    "up": (-1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

presents = int(input())
matrix = []
santa_row, santa_col = 0, 0
nice_kids = 0
nice_kids_presents = 0

for row in range(int(input())):
    matrix_row = [el for el in input().split()]
    if "S" in matrix_row:
        santa_row, santa_col = row, matrix_row.index("S")
    nice_kids += matrix_row.count("V")
    matrix.append(matrix_row)

while presents > 0:

    command = input()
    if command == "Christmas morning":
        break

    new_row, new_col = moves[command]

    matrix[santa_row][santa_col] = "-"
    santa_row, santa_col = new_row + santa_row, new_col + santa_col

    if matrix[santa_row][santa_col] == "V":
        presents -= 1
        nice_kids_presents += 1
    elif matrix[santa_row][santa_col] == "C":
        presents, nice_kids_presents = happy_santa(presents, nice_kids_presents)

    matrix[santa_row][santa_col] = "S"

    if nice_kids_presents == nice_kids:
        break

else:
    print("Santa ran out of presents!")

[print(*row, sep=" ") for row in matrix]

if nice_kids == nice_kids_presents:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids - nice_kids_presents} nice kid/s.")
