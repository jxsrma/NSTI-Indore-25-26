def allTask():
    Connection
    Cursor
    query select
    execute
    pretty table
    print


print("Welcome to TODO List")

print("1. View Task\n2. Add\n3. Delete")


mainOp = int(input("Select Option:: "))

if mainOp == 1:
    print("All Task: ")
    allTask()
        
elif mainOp == 2:
    print("Add Task: ")
elif mainOp == 3:
    print("Delete: ")
else:
    print("Please select valid option")
