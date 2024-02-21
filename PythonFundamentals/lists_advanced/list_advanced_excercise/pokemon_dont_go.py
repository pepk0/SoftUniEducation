def increment_decrement(control_num: int, sequence: list) -> None:
    for index in range(len(sequence)):
        if sequence[index] <= control_num:
            sequence[index] += control_num
        else:
            sequence[index] -= control_num


removed_elements_sum = 0
number_sequence = [int(i) for i in input().split()]

while number_sequence:
    index_to_remove = int(input())
    if index_to_remove < 0:
        removed_element = number_sequence[0]
        number_sequence[0] = number_sequence[-1]
    elif index_to_remove >= len(number_sequence):
        removed_element = number_sequence[-1]
        number_sequence[-1] = number_sequence[0]
    else:
        removed_element = number_sequence.pop(index_to_remove)

    removed_elements_sum += removed_element
    increment_decrement(removed_element, number_sequence)

print(removed_elements_sum)
