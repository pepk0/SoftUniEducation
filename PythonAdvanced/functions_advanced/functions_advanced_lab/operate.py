def operate(*args) -> int:
    operators = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "/": lambda x, y: x / y,
        "*": lambda x, y: x * y,
    }

    operation = operators[args[0]]
    result = args[1]

    for i in range(2, len(args)):
        result = operation(result, args[i])

    return result

# print(operate("/", 3, 1, 2))
