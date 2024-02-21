range_start = int(input())
range_end = int(input())

for first_digit in range(range_start, range_end + 1):
    for second_digit in range(range_start, range_end + 1):
        for third_digit in range(range_start, range_end + 1):
            for fourth_digit in range(range_start, range_end + 1):

                condition_one = first_digit % 2 == 0 and fourth_digit % 2 != 0
                condition_two = first_digit % 2 != 0 and fourth_digit % 2 == 0
                condition_three = first_digit > fourth_digit
                condition_four = (second_digit + third_digit) % 2 == 0

                if ((condition_one or condition_two) 
                    and condition_three and condition_four):

                    print(f"{first_digit}{second_digit}"
                          f"{third_digit}{fourth_digit}", end=" ")