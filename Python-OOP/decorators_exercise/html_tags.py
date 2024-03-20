def tags(tag: str):
    def decorator(function):
        def wrapper(*args):
            result = function(*args)
            return f"<{tag}>{result}</{tag}>"

        return wrapper

    return decorator
