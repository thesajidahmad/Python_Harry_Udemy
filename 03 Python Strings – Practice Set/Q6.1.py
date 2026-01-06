# 6. Bonus Questions

# Write a program that counts how many vowels are in a given string.

text = "Coding in Python is fun"
sum = 0
vowels = ['a', 'e', 'i', 'o', 'u']

for char in text.lower():
    if(char in vowels):
        sum += 1

print(f"There is {sum} vowels in this sentence")