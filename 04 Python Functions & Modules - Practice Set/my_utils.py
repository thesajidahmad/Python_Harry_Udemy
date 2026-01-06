# 7. Bonus Challenges

# Create a small module my_utils.py with a function is_even(n) that returns True if n is even. Import and use it in another Python file.

# its used in Q7.3

def is_even(n):
    if (n == 0):
        return "N is 0"
    elif (n%2==0):
        return True
    else:
        return False