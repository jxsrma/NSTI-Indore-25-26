str = "Given a string, count how many times each character appears, ignoring case."
str = str.lower()
result = {}

for i in str:
    if i in result.keys():
        result[i] = result[i]+1
    else:
        result[i] = 1
print(result)