# 6. Bonus Challenges

# Write a program that takes a list of numbers and removes all duplicates using a set.


def remove_duplicate(num):
    return list(set(num))

num = [1,3,2,6,3,1,8,8,5,7,3]

print(remove_duplicate(num))