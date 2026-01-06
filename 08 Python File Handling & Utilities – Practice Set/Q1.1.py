# 1. File I/O Basics

# Create a text file notes.txt using Python and write "Learning Python is fun!" into it.

f = open("notes.txt", "w")

f.write("Learning Python is fun!")

f.close()