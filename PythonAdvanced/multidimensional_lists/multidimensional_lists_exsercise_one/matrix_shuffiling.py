def valid_indices(input_indices: list) -> bool:
    if len(input_indices) != 4:
        return False

    return (0 <= input_indices[0] < rows and 0 <= input_indices[2] < rows
            and 0 <= input_indices[1] < cols and 0 <= input_indices[3] < cols)


rows, cols = [int(i) for i in input().split()]
matrix = [[el for el in input().split()] for _ in range(rows)]

while True:
    command, *indices = [int(el) if el.isdigit()
                         else el for el in input().split()]

    if command == "END":
        break

    if command == "swap" and valid_indices(indices):
        idx_one, idx_two, idx_tree, idx_four, = indices

        matrix[idx_one][idx_two], matrix[idx_tree][idx_four] = \
            matrix[idx_tree][idx_four], matrix[idx_one][idx_two]

        for row in matrix:
            print(*row, sep=" ")
    else:
        print("Invalid input!")
