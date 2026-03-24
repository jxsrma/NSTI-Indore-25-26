# Implicit
a = 7.5
b = 5

print(a+b)

# Explicit
a = 5
b = "10"
# print(a+b)
# a. 5+10 b. 510 c. 5 10 d. 5"10" E. (Correct) TypeError: unsupported operand type(s) for +: 'int' and 'str'
print("Type of b Before:", type(b))
b = int(b)
print("Type of b After:", type(b))
print(a+b)
