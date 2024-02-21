number = int(input())
current = 1
is_current_bigger_than_n = False

for row in range(1, number + 1):
    for column in range(1, row + 1):

        if current > number:
            is_current_bigger_than_n = True
            break
        print(f"{current}", end=" ")
        current += 1
    if is_current_bigger_than_n:
            break
    print()
