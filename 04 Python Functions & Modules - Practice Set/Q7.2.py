# 7. Bonus Challenges

# Write a function safe_divide(a, b) that returns the result of a / b , but returns "Cannot divide by zero" if b is 0 .

def safe_divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return (a/b)

print(safe_divide(10,2))
print(safe_divide(10,0))