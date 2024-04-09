def store_in_file(text: str) -> None:
    with open("results.txt", "a") as out_file:
        out_file.write(text + "\n")


def store_results(function):
    def wrapper(*args, **kwargs):
        function_result = function(*args, **kwargs)
        function_info = (f"Function {function.__name__} was called. "
                         f"Result {function_result}")

        # store the result in a file
        store_in_file(function_info)

        return function_result

    return wrapper
