class Person():
    def __init__(self, fName, lName, city, state, country, phone, email):

        self.fName = fName
        self.lName = lName
        self.City = city
        self.State = state
        self.Country = country
        self.Phone = phone
        self.Email = email

    def __str__(self):
        return f"""              
Name: {self.fName} {self.lName}
Phone: {self.Phone} 
E-Mail: {self.Email}
Address: {self.City}, {self.State}, {self.Country}
               """

    def __add__(self, other):
        result = f"{self.fName} and {other.fName} are Friends and they live in"

        if str(self.City) == str(other.City):
            return result+f" {self.City}."
        else:
            return result + f" {self.City} & {other.City} respectivly."


Ram = Person("Ram", "Sharma", "Indore", "MP", "India",
             "+91-123-456-7890", "ram@gmail.com")

Rohan = Person("Rohan", "Verma", "Dewas", "MP", "India",
               "+91-123-456-1234", "rohan@gmail.com")

# Ram.printDetails()
# Rohan.printDetails()

print(Ram)
print(Rohan)

print(Ram+Rohan)

Shyam = Person("Shyam", "Mohan", "Indore", "MP", "India",
               "+91-123-456-5566", "shyam@gmail.com")

print(Ram+Shyam)
