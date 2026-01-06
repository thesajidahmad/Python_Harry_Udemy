# 4. While Loops

# Write a program that keeps asking the user to enter a password until they enter the correct one.

a = int(input("Enter the password: "))

while(a != (1234)):
    a = int(input("Sorry!! Enter the correct password: "))

print("Password is Correct!!")