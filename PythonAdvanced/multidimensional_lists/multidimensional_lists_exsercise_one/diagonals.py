number_rows = int(input())

primary_diagonal = []
secondary_diagonal = []

for index in range(number_rows):
    secondary_index = (number_rows - 1) - index

    matrix_row = [int(i) for i in input().split(", ")]

    primary_diagonal.append(matrix_row[index])
    secondary_diagonal.append(matrix_row[secondary_index])

print(f"Primary diagonal: {', '.join(str(el) for el in primary_diagonal)}. "
      f"Sum: {sum(primary_diagonal)}")

print(f"Secondary diagonal: {', '.join(str(el) for el in secondary_diagonal)}. "
      f"Sum: {sum(secondary_diagonal)}")
