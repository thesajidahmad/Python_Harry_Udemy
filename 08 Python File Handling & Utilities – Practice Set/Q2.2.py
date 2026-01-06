# 2. Read, Write, and Append Files

# Open tasks.txt in append mode and add a new line "Task Completed!" .

with open("tasks.txt", "a") as f:
    f.write("Task Completed!")

f.close()

__a_ = 77