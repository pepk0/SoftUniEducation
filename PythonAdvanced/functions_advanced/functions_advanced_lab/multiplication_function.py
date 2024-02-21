def multiply(*args) -> int:
    result = 1

    for i in range(len(args)):
        result *= args[i]

    return result
