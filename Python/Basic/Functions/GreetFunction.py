print("***********Method 1*************")
# Method 1


def greet(name: str):
    """This function will print a name"""
    print("Hello " + name)


for i in range(5):
    greet("Ram")

# Method 2
# A
print("***********Method 2A*************")


def greet2A(name: str):
    """This function will print a name"""
    print("Hello " + name)


names = ["Ram", "Shyam", 'Gauri', 'Meher', 'Jash']

for name in names:
    greet2A(name)

# B
print("***********Method 2B*************")


def greet2B(names: list):
    """This function will print a name by taking list as input"""
    for name in names:
        print("Hello " + name)


AITrainee_names = ['Sona', 'Mehek', 'Jyoti', 'Anjali', 'Karishma']

greet2B(AITrainee_names)


TraineeROll1 = 8
greet("ram")
greet2A("ram")
greet2B(['A', 'B', 'C'])

greet2B()