from pathlib import Path

# Absolute path - from the root of the hard disk e.g /home/user/file.py
# Relative path - starting from the current directory

# path = Path("ecommerce")
# print(path.exists())
# print(path.mkdir())

this_dir = Path()
# prints all the file in the current directory
for file in this_dir.glob("*.py"):
    print(file)



