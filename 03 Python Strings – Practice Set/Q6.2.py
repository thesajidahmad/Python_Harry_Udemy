# 6. Bonus Questions

# Take a user input string and check if it is a palindrome (same forwards and backwards).

a = str(input("Enter a string: "))

b = a[::-1]

if(a==b):
    print("It is a palindrome")
else:
    print("It is not a palindrome")