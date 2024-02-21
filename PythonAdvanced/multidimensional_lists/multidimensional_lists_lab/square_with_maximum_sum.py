rows, cols = [int(i) for i in input().split(", ")]

matrix = [[int(i) for i in input().split(", ")] for _ in range(rows)]
best_sum = float("-inf")
best_matrix_row, best_matrix_col = 0, 0

for row in range(rows - 1):
    for col in range(cols - 1):

        sub_matrix_sum = matrix[row][col] + matrix[row + 1][col] + \
            matrix[row][col + 1] + matrix[row + 1][col + 1]

        if sub_matrix_sum > best_sum:
            best_sum = sub_matrix_sum
            best_matrix_row, best_matrix_col = row, col

for next_row in range(2):
    for next_col in range(2):

        print(matrix[best_matrix_row + next_row]
              [best_matrix_col + next_col], end=" ")

    print()

print(best_sum)
