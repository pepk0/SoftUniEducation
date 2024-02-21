rows, cols = [int(i) for i in input().split()]
matrix = [[el for el in input().split()] for _ in range(rows)]

identical_sub_matrixes = 0

for row in range(rows - 1):
    for col in range(cols - 1):

        cur_el = matrix[row][col]
        right_el = matrix[row][col + 1]
        bottom_el = matrix[row + 1][col]
        bottom_right = matrix[row + 1][col + 1]

        if cur_el == right_el == bottom_el == bottom_right:
            identical_sub_matrixes += 1

print(identical_sub_matrixes)
