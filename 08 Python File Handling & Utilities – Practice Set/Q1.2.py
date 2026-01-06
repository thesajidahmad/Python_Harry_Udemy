# 1. File I/O Basics

# Open notes.txt , read its content, and print it to the console.

f = open("notes.txt", "r")

context = f.read()

print(context)

f.close()