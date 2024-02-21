def is_palindrome(integer: int) -> int:
    if number < 0:
        return False
    devisor = 1
    while integer > devisor * 10:
        devisor *= 10

    while integer:
        first_digit = integer // devisor
        last_digit = integer % 10

        if first_digit != last_digit:
            return False

        integer = integer % devisor
        integer = integer // 10

        devisor //= 100
    return True


numbers = [int(i) for i in input().split(", ")]
for number in numbers:
    print(is_palindrome(number))
