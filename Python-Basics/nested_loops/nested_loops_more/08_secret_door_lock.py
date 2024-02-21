hundredths_boundry = int(input())
tenths_boundry = int(input())
ones_boundry = int(input())
prime_range = "2357"

for digit_one in range(1, hundredths_boundry + 1):
    for digit_two in range(1, tenths_boundry + 1):
        for digit_three in range(1, ones_boundry + 1):

            condition_one = digit_one % 2 == 0 and digit_three % 2 == 0
            condition_two = str(digit_two) in prime_range

            if condition_one and condition_two:
                print(f"{digit_one} {digit_two} {digit_three}") 