A = [1, 2, 3, 4]
B = [2, 3, 5]
C = [3, 2, 6]

result = []

for i in A:
    if i in B and i in C:
        result.append(i)
print(result)
