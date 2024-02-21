rows, cols = [int(i) for i in input().split()]
matrix = [[int(i) for i in input().split()] for _ in range(rows)]

best_sum_row, best_sum_col = 0, 0
best_sum = float("-inf")

for row in range(rows - 2):
    for col in range(cols - 2):

        cur_matrix_sum = 0

        for sub_matrix_row in range(row, row + 3):
            for sub_matrix_col in range(col, col + 3):

                cur_matrix_sum += matrix[sub_matrix_row][sub_matrix_col]

        if cur_matrix_sum > best_sum:
            best_sum = cur_matrix_sum
            best_sum_row, best_sum_col = row, col

print(f"Sum = {best_sum}")

for row in range(3):
    for col in range(3):

        print(matrix[best_sum_row + row][best_sum_col + col], end=" ")

    print()
