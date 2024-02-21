def concatenate(*args, **kwargs) -> str:
    result_string = "".join(args)

    for element, substitute_element in kwargs.items():

        while element in result_string:
            result_string = result_string.replace(element, substitute_element)

    return result_string

