# Problem 2: Debugging Function Calls
# Problem: Create a decorator to print the function name and the values of its arguments every time the function is called.

def Func_name(func):
    def wrapper():
        func()
        x = print(f"Method name is {func.__name__}")
        return x
    return wrapper

@Func_name
def hello():
    print("Hello Test")

hello()