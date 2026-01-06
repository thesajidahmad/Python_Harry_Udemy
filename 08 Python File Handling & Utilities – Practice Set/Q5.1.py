# 5. Bonus Challenges

# Write a program that reads a file and creates another file with all words converted to uppercase.

with open("my_folder/tasks.txt", "r") as f:
    context = f.read()
    print(context)
    cap_context = context.upper()
    print(cap_context)