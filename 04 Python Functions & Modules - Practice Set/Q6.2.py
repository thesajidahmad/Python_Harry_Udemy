# 6. Variable Scope and Docstrings

# Write a function multiply(a, b) that has a proper docstring explaining what it does. Then use help(multiply) to display the docstring.

def multiply(a,b):
    '''
    Docstring for multiply
    
    :param a: (int or float) The first number
    :param b: (int or float) The second number

    returns : Product of a and b
    '''
    return a*b

print(multiply(12,5))
print(multiply(10,15.25))
help(multiply)