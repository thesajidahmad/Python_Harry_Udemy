# Problem 1: Timing Function Execution
# Problem: Write a decorator that measures the time a function takes to execute.

import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        x = print(end-start)
        return x
    return wrapper

@timer
def hello():
    print("Hello World!!")
    time.sleep(6)

hello()