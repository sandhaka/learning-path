import functools


def log_function(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Log the function input parameters
        input_str = f"{func.__name__} called with inputs: {args}, {kwargs}"
        print(input_str)
        # Call the function
        result = func(*args, **kwargs)
        # Log the function output
        output_str = f"{func.__name__} returned: {result}"
        print(output_str)
        return result

    return wrapper
