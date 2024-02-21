def math_operations(*args, **kwargs) -> str:
    index = 0
    keys = {
        "a": lambda x, j: x + j["a"],
        "s": lambda x, j: j["s"] - x,
        "d": lambda x, j: j["d"] / x,
        "m": lambda x, j: x * j["m"],
    }

    while len(args) > index:
        element = args[index]
        operator = tuple(keys)[index % len(keys)]

        index += 1

        if operator == "d" and element == 0:
            continue

        kwargs[operator] = keys[operator](element, kwargs)

    return "\n".join([f"{el}: {value:.1f}" for el, value in
                      sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))])
