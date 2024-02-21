first_sting, second_string = input().split()
index = 0

result = 0
while index < len(first_sting) or index < len(second_string):
    if index >= len(first_sting):
        to_multiply_one = 1
    else:
        to_multiply_one = ord(first_sting[index])
    if index >= len(second_string):
        to_multiply_two = 1
    else:
        to_multiply_two = ord(second_string[index])

    result += to_multiply_one * to_multiply_two
    index += 1

print(result)
