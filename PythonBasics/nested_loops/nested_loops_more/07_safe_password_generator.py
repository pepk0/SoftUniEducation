digit_x_boundary = int(input())
digit_y_boundary = int(input())
max_passwords = int(input())
symbol_a = 35
symbol_b = 64
max_passwords_reached = False
passwords_generated =  0

for digit_one in range(1, digit_x_boundary + 1):
    for digit_two in range(1, digit_y_boundary + 1):

        if passwords_generated == max_passwords:
            max_passwords_reached = True
            break
        passwords_generated += 1

        print(f"{chr(symbol_a)}{chr(symbol_b)}{digit_one}"
              f"{digit_two}{chr(symbol_b)}{chr(symbol_a)}", end="|")

        symbol_a += 1
        symbol_b += 1
        
        if symbol_a > 55:
            symbol_a = 35
        
        if symbol_b > 96:
            symbol_b = 64

    if max_passwords_reached:
        break   