def convert(value):
    if type(value) == str:
        return ord(value)
    return chr(value)


start_interval_letter = input()
end_interval_letter = input()
exclude_letter = input()

start_number = convert(start_interval_letter)
end_number = convert(end_interval_letter)
exclude_number = convert(exclude_letter)
iterations = 0

for first_letter in range(start_number, end_number + 1): # type: ignore
    if first_letter == exclude_number:
        continue
    for second_letter in range(start_number, end_number + 1): # type: ignore
        if second_letter == exclude_number:
            continue
        for third_letter in range(start_number, end_number + 1): # type: ignore
            if third_letter == exclude_number:
                continue
            
            iterations += 1
            print(f"{convert(first_letter)}{convert(second_letter)}"
                f"{convert(third_letter)}", end = " ")

print(iterations)