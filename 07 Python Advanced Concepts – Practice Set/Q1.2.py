# 1. Decorators in Python

# Write a decorator timer that calculates how long a function takes to execute.Test it with a function that sums numbers from 1 to 1,000,000.

import time


def timer(func):
    def wrappers():
        start = time.time()
        func()
        end = time.time()
        print(end-start)
    return wrappers

@timer
def sum():
    x = 0
    for i in range(1, 1000001):
        x = x+i
    print(x)

sum()