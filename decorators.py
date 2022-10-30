import functools
import time

def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

def debug(func):
    """Print the function signature and return value."""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                       # 1
        kwargs_repr = [f"{k} = {v!r}" for k,v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)            # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")            # 4
        return value
    return wrapper_debug

def slow_down(func):
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        # do something before
        time.sleep(1)
        value = func(*args, **kwargs)
        # do something after
        return value
    return wrapper_slow_down

def printer(func):
    """Print something when the function is defined"""
    def wrapper_print():
        print(f'hello')
    return wrapper_print

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    #  1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer


def repeat(func, num_times=1):
    def wrapper_repeat(*args, **kwargs):
        for _ in range(num_times):
            value = func(*args, **kwargs)
        return value
    return wrapper_repeat


def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
        return func(*args, **kwargs)
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls
