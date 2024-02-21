digits = input()

largest_number = ""
length_digits = len(digits)

while length_digits > len(largest_number):

    largest_index = 0
    for i in range(len(digits)):
        if digits[i] >= digits[largest_index]:
            largest_index = i

    largest_number += digits[largest_index]
    digits = digits[:largest_index] + digits[largest_index + 1:]
            

print(largest_number)