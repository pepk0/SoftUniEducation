end_range_number = int(input())

for number in range(1, end_range_number + 1):

    is_special = False
    digit_sum = sum([int(el) for el in str(number)])

    if digit_sum == 7 or digit_sum == 11 or digit_sum == 5:
        is_special = True

    print(f"{number} -> {is_special}")
