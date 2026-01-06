# 1. Defining Functions

# Write a function square(num) that returns the square of a given number. Test it with different numbers.

num = int(input("Enter a Number: "))

def square(num):
    print(f"Square of the {num} is:",num**2)
    return num*num

square(num)