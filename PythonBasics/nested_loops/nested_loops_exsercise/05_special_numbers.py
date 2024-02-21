condition_number = int(input())

for number in range(1111, 10000):
    string_number = str(number)
    special_number = True
    
    for deviser in string_number:
        if deviser == "0" or condition_number % int(deviser) != 0:
            special_number = False
            break

    if special_number:
        print(number, end=" ")