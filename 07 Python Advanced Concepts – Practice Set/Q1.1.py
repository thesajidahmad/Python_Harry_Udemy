# 1. Decorators in Python

# Write a decorator logger that prints "Function is being called" before the function runs. Use it to decorate a function say_hello() that prints "Hello!" .

def logger(func):
    def wrappers():
        print("Function is being called")
        func()

    return wrappers

@logger
def say_hello():
    print("hello")

say_hello()