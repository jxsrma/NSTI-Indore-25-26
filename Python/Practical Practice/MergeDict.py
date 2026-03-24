A = {'a': 10, 'b': 20}
B = {'b': 5, 'c': 7}


result = {}

for key, value in A.items():
    if key in B.keys():
        # print("Yes",key)
        result[key] = A[key]+B[key]
    else:
        # print("No",key)
        result[key] = A[key]

for key, value in B.items():
    if key not in result.keys():
        result[key] = B[key]

print(result)
