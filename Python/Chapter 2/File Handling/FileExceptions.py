try:
    with open('asdlsjdn.py', 'r') as file:
        print(file.read())
except FileNotFoundError:
    print("No file with this name")
else:
    print("Unknow Error")

print("Program executed Successully")

print("सभी को नमस्कार")
