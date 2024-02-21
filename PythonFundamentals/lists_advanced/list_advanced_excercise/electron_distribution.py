def electron_distribution(number: int) -> list:
    position = 1
    result = []
    while number:
        can_hold = 2 * position ** 2
        if can_hold < number:
            result.append(can_hold)
            number -= can_hold
        else:
            result.append(number)
            number = 0
        position += 1
    return result


number_electrons = int(input())
print(electron_distribution(number_electrons))
