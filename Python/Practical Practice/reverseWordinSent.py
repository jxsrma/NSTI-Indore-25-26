s = "Python programming is fun"

words = s.split()
revereList = []
for i in words:
    revereList.append(i[::-1])

sResult = ""

for i in revereList:
    sResult = sResult+ " " + i

sResult = sResult.strip()

print(sResult)