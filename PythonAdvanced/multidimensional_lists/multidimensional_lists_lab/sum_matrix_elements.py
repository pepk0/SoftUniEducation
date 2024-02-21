rows, _ = [int(i) for i in input().split(", ")]

matrix = []
matrix_sum = 0

for _ in range(rows):
    row = [int(i) for i in input().split(", ")]
    matrix_sum += sum(row)
    matrix.append(row)

print(matrix_sum, matrix, sep="\n")
