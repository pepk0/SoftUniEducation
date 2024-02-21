def find_el(input_matrix: list, symbol) -> str:
    for row in range(len(input_matrix)):
        for col in range(len(input_matrix[0])):

            if input_matrix[row][col] == symbol:
                return f"({row}, {col})"

    return f"{symbol} does not occur in the matrix"


matrix = [[el for el in input()] for _ in range(int(input()))]
symbol_quire = input()

print(find_el(matrix, symbol_quire))
