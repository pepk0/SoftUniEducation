def is_even(element) -> bool:
    if isinstance(element, int):
        return element % 2 == 0
    return False


def even_parameters(function):
    def wrapper(*args, **kwargs):
        for el in args:
            if not is_even(el):
                return "Please use only even numbers!"

        result = function(*args, **kwargs)

        return result

    return wrapper
