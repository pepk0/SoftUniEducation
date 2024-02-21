def even_odd_filter(**kwargs) -> dict:
    result = {}
    number_filter = {
        "even": lambda x: x % 2 == 0,
        "odd": lambda x: x % 2 != 0,
    }

    for type_number, numbers in kwargs.items():
        result[type_number] = [el for el in numbers if
                               number_filter[type_number](el)]

    return dict(sorted(result.items(), key=lambda x: -len(x[1])))
