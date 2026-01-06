# 3. OS and Shutil Modules

# Use the shutil module to:
# Copy a file from one folder to another

import os
import shutil

shutil.copy("tasks.txt", "my_folder/tasks.txt")

# Move a file to a new folder

shutil.move("notes.txt", "my_folder/")

# Delete a file (careful: irreversible!)

os.remove("tasks.txt")