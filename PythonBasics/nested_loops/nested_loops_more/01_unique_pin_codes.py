first_number_boundary = int(input())
second_number_boundary = int(input())
third_number_boundary = int(input())
prime_nums = (2,3,5,7)

for first_digit in range(1, first_number_boundary + 1):
    for second_digit in range(1, second_number_boundary + 1):
        for third_digit in range(1, third_number_boundary + 1):

            if (first_digit % 2 == 0 and third_digit % 2 == 0 
                and second_digit in prime_nums):
                print(first_digit, second_digit, third_digit)