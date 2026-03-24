trainees = ["Shyam", "ram", "Mohan", "Sohan", "Priti"]

try:  # Try the execution
    index = int(input("Enter index of an item:  "))
    print(trainees[index])
    print(index/0)
except ValueError:  # Handle ValueError Exception
    print("Invalid Input for roll number")
except IndexError:  # Handle IndexError Exception
    print("No trainee from this roll")
except Exception as e:  # Handle All Exception
    print("There is a Problem:", e)
else:  # Runs when No Exception
    print("No Error In the code")
finally:  # Runs Everytime
    print("Program Run Successfully")
# index = int(input("Enter index of an item:  "))
# print(trainees[index])
