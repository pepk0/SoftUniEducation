def multiply(number: int):
    def decorator(func):
        def wrapper(*args):
            result = func(*args)
            return result * number

        return wrapper

    return decorator
