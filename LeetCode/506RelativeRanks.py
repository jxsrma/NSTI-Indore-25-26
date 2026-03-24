# score = [5,4,3,2,1]
# score = [10,3,8,9,4]
score = [1]
if len(score) == 1:
    return ["Gold Medal"]


ranking = sorted(score,reverse=True)

rankingDict = {
    ranking[0]: "Gold Medal",
    ranking[1]: "Silver Medal",
    ranking[2]: "Bronze Medal"
}

for i in range(3,len(ranking)):
    rankingDict[ranking[i]] = i+1

answer = []

for i in score:
    answer.append(str(rankingDict.get(i)))

print(answer)