def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def get_primes(integer_list: list) -> int:
    for integer in integer_list:
        if is_prime(integer):
            yield integer
