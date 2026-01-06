# 1. If-Else Conditional Statements

# Write a program that asks the user for a number and prints whether it is positive, negative, or zero.

a = int(input("Enter a number: "))

if a>0:
    print(a,"is a positive number")
elif a<0:
    print(a,"is a negative number")
else:
    print(a,"is a zero")