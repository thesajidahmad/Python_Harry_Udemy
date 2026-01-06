# 2. Read, Write, and Append Files

# Write a program that writes three lines of text to a file tasks.txt .

with open("tasks.txt", "w") as f:
    f.write("Line1\n")
    f.write("Line2\n")
    f.write("Line3\n")

f.close()