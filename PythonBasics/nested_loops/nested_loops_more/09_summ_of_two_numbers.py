starting_number = int(input())
ending_number = int(input())
magic_number = int(input())
combinations_checked = 0
magic_number_found = False


for number_one in range(starting_number, ending_number + 1):
    for number_two in range(starting_number, ending_number + 1):
        combinations_checked += 1

        if number_one + number_two == magic_number:
            
            print(f"Combination N:{combinations_checked} "
                  f"({number_one} + {number_two} = {magic_number})")
            
            magic_number_found = True
            break

    if magic_number_found:
        break

if not magic_number_found:
    print(f"{combinations_checked} combinations - "
          f"neither equals {magic_number}")
