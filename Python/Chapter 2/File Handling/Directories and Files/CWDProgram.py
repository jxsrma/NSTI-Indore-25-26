import os

cwd = os.getcwd()
print(cwd)

directories = os.listdir()

for folder in directories:
    print(folder)