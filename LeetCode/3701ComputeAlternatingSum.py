li = [1, 3, 5, 7]

for i in range(len(li)):
    if i%2 != 0:
        li[i] = li[i]*(-1)

sum = 0

for i in li:
    sum+=i
print(sum)
