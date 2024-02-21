control_number_n = int(input())
control_number_l = int(input())
symbol_range = range(97, 97 + control_number_l)

for digit_one in range(1, control_number_n + 1):
    for digit_two in range(1, control_number_n + 1):
        for symbol_one in symbol_range:
            for symbol_two in symbol_range:
                for digit_three in range(1, control_number_n + 1):

                    if digit_three > digit_one and digit_three > digit_two:
                        
                        print(f"{digit_one}{digit_two}{chr(symbol_one)}"
                              f"{chr(symbol_two)}{digit_three}", end=" ")
