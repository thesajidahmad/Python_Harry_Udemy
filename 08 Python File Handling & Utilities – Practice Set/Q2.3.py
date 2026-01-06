# 2. Read, Write, and Append Files

# Read the file and print all lines as a list using readlines() .

with open("tasks.txt", "r") as f:
    # context = f.readlines()
    # print(context)

    for line in f.readlines():
        print(line)

f.close()