integer_list = [int(i) for i in input().split(", ")]

non_zero_pointer = 0
for index in range(len(integer_list)):
    if integer_list[index] != 0:
        integer_list[non_zero_pointer], integer_list[index] \
        = integer_list[index], integer_list[non_zero_pointer]
        non_zero_pointer += 1

print(integer_list)
