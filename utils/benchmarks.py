from functools import wraps
from time import time


def call_counter(func):
    def helper(*args, **kwargs):
        helper.calls += 1
        return func(*args, **kwargs)

    helper.calls = 0
    return helper


def benchmark(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        execution_time = time() - start_time
        print(
            "Function {} executed in {} milliseconds".format(
                func.__name__, round(execution_time * 1000, 6)
            )
        )
        return result

    return wrapper
