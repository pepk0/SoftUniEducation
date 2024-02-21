def factorial(num: int) -> int:
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result


def factorial_division(num_one: int, num_two: int) -> str:
    first_factorial = factorial(num_one)
    second_factorial = factorial(num_two)
    return f"{first_factorial / second_factorial:.2f}"


first_number = int(input())
second_number = int(input())
print(factorial_division(first_number, second_number))