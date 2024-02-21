def add_to_sequence(sequence: set, numbers: list) -> None:
    sequence.update(numbers)


def remove_from_sequence(sequence: set, list_numbers) -> set:
    numbers = set(list_numbers)
    return sequence.difference(numbers)


def subset_either(sequence_one: set, sequence_two: set) -> bool:
    result = False
    if sequence_one.issubset(sequence_two):
        result = True
    elif sequence_two.issubset(sequence_one):
        result = True
    return result


first_sequence = {int(i) for i in input().split()}
second_sequence = {int(i) for i in input().split()}

for _ in range(int(input())):
    command, sequence, *numbers = input().split()
    numbers = [int(i) for i in numbers]
    if command == "Add":
        if sequence == "First":
            add_to_sequence(first_sequence, numbers)
        else:
            add_to_sequence(second_sequence, numbers)
    elif command == "Remove":
        if sequence == "First":
            first_sequence = remove_from_sequence(first_sequence, numbers)
        else:
            second_sequence = remove_from_sequence(second_sequence, numbers)
    else:
        print(subset_either(first_sequence, second_sequence))

print(*sorted(first_sequence), sep=", ")
print(*sorted(second_sequence), sep=", ")
