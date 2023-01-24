import time
from functools import wraps

def timer(func):
    """
    prints the run time of decorated function
    """

    @wraps(func)
    def wrapper(*args, **kwards):
        start_time = time.perf_counter()
        value = func(*args, **kwards)
        end_time = time.perf_counter()
        runtime = end_time - start_time
        print(f'Runtime: {runtime:.2f}')
        return value
    return wrapper

