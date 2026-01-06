# 2. Function Arguments & Return Values

# Write a function full_name(first, last) that takes first name and last name as parameters and returns a single string in the format "First Last" .

def full_name(first, last):
    # x = first + last
    return f"{first} {last}"

a = str(input("Enter the first name: "))
b = str(input("Enter the last name: "))

print(full_name(a,b))