def recursive_power(num: int, power: int) -> int:
    if power == 1:
        return num

    return num * recursive_power(num, power - 1)

# print(recursive_power(2, 10))
