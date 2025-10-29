for i in range(1, 10):
    if i == 3:
        pass
    if i == 5:
        continue
    if i == 7:
        break
    print(i, "Hello")

print("********Odd Numbers************")
for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i)

print("********Even Numbers************")
for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i)
