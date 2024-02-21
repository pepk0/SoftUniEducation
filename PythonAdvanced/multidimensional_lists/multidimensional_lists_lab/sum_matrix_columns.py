rows, cols = [int(i) for i in input().split(", ")]
matrix = [[int(i) for i in input().split()] for _ in range(rows)]

for col in range(cols):
    cur_col_sum = 0
    for row in range(rows):

        cur_col_sum += matrix[row][col]

    print(cur_col_sum)
