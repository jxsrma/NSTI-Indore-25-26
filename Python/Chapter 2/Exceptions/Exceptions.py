a = 5
b = 5
print("************Handling by IF and Else***************")
if b == 0:
    print("Cannot divide by zero")
else:
    c = a/b
    print(c)

print("Hello1")

print("************Handling by Try and Except***************")

try:
    c = a/b
    print(c)
except:
    print("Cannot divide by zero")

print("Hello2")
