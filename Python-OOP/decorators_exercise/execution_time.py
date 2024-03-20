import time


def exec_time(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        function(*args, **kwargs)
        end_time = time.time()

        execution_time = end_time - start_time

        return execution_time

    return wrapper
