li = [4, 5, 1, 2, 3]

for index in range(len(li)):
    # li[index] = li[index]**2
    def square(a): return a**2
    li[index] = square(li[index])

print(li)
