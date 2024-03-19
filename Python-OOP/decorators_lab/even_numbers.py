def even_numbers(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return [i for i in result if i % 2 == 0]

    return wrapper


@even_numbers
def get_numbers(numbers: list) -> list:
    return numbers
