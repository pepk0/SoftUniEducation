rows, cols = [int(i) for i in input().split()]

start_range = ord("a")

for row in range(rows):
    for col in range(row, cols + row):

        first_letter = f"{chr(start_range + row)}"
        second_letter = f"{chr(start_range + col)}"
        third_letter = f"{chr(start_range + row)}"

        palindrome = first_letter + second_letter + third_letter

        print(palindrome, end=" ")

    print()
