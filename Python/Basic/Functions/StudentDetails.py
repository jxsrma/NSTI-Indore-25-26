def printDetails(name, cls, roll, sec, contact):
    print("Trainee's Name\t\t:", name)
    print("Trainee's Class\t\t:", cls)
    print("Trainee's Roll\t\t:", roll)
    print("Trainee's Section\t:", sec)
    print("Trainee's Contact\t:", contact)
    print("**********************")


printDetails("ram", 10, 38, 'A', 9087654321)
printDetails(9087654321, 10, "ram", 38, 'A')
printDetails(contact=9087654321, cls=10, name="ram", roll=38, sec='A')

print(list(range(10)))
print(list(range(1,10)))
print(list(range(10,1)))
print(list(range(1,10,2)))

printDetails("Shyam",10,contact=9987654321,roll=40,sec='A')