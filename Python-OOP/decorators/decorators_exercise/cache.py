def cache(func):
    log = {}

    def wrapper(*args):
        if args[0] not in log:
            log[args[0]] = func(*args)

        wrapper.log = log

        return log[args[0]]

    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
