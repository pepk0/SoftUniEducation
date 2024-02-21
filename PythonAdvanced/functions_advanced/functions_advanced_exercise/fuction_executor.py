def func_executor(*args) -> str:
    result = ""

    for functions, arguments in args:
        result += f"{functions.__name__} - {functions(*arguments)}\n"

    return result
