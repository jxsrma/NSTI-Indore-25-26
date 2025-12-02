li = [1, 2, 3, 4, 5]
n = 2
for i in range(n):
    last = li[len(li)-1]
    for j in range(len(li)-1,0,-1):
        li[j] = li[j-1]
    li[0] = last
    
print(li)
