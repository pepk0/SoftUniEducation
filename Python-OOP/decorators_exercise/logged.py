def logged(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        function_name = function.__name__
        return f"you called {function_name}{args}\nit returned {result}"

    return wrapper
