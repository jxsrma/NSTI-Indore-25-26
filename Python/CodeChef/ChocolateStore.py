Days = 4

perDay = [
    [3, 1],
    [5, 5],
    [4, 7],
    [2, 3],
]

for day in perDay:
    target = day[0]
    totalSale = day[1]

    if totalSale > target:
        extra = totalSale - target
        print(target+extra*2)
    else:
        print(totalSale)
