# Given a list of integers, write a function to find the second largest value without sorting the list.


li = [5, 4, 5, 6, 7, 5, 4, 13, 2, 3, 4, 6, 15, 20]

# Largest
max1 = -1
for i in li:
    max1 = max(i, max1)
print(max1)

# Second
max2 = -1
for i in li:
    if max1 > i:
        max2 = max(i, max2)

print(max2)
li.sort(reverse=True)
print(li[1])
print(li)