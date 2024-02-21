def even_odd(*args) -> list:
    functionality = {
        "even": lambda x: x % 2 == 0,
        "odd": lambda x: x % 2 != 0,
    }

    return [i for i in args[:-1] if functionality[args[-1]](i)]


# print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
