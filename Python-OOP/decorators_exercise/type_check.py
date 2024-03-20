def type_check(_type):
    def decorator(function):
        def wrapper(*args):
            if isinstance(*args, _type):
                return function(*args)

            return "Bad Type"

        return wrapper

    return decorator
