def check_coordinate(row_, col_, matrix_size: int) -> bool:
    return 0 <= row_ < matrix_size and 0 <= col_ < matrix_size


matrix_size = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(matrix_size)]


command = input()

while command != "END":
    command, *values = [el for el in command.split()]
    row, col, value = int(values[0]), int(values[1]), int(values[2]) 

    if check_coordinate(row, col, matrix_size):

        if command == "Add":
            matrix[row][col] += value
        elif command == "Subtract":
            matrix[row][col] -= value

    else:
        print("Invalid coordinates")

    command = input()

[print(*row, sep=" ") for row in matrix]
