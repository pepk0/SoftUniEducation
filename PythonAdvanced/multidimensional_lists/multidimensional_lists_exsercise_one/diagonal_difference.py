matrix_size = int(input())

primary_diagonal = 0
secondary_diagonal = 0

for primary_index in range(matrix_size):
    index_diagonal = (matrix_size - 1) - primary_index

    matrix_row = [int(i) for i in input().split()]

    primary_diagonal += matrix_row[primary_index]
    secondary_diagonal += matrix_row[index_diagonal]

print(abs(primary_diagonal - secondary_diagonal))
