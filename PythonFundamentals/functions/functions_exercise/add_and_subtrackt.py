def sum_numbers(num_one: int, num_two: int) -> int:
    return num_one + num_two


def subtract(num_one: int, num_two: int) -> int:
    return num_one - num_two


def add_and_subtract(num_one: int, num_two: int, num_three: int) -> int:
    result = sum_numbers(num_one, num_two)
    return subtract(result, num_three)


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(add_and_subtract(first_number, second_number, third_number))
