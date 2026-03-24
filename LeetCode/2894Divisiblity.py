n = 10
m = 3

num1 = 0

for i in range(1,n+1):
    if i%m!=0:
        num1 +=i
    
num2 = 0
for i in range(1,n+1):
    if i%m==0:
        num2 +=i

print(num1-num2)