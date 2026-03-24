nums = [2, 7, 11, 15]
target = 26
count = 1
for i in nums:
    for j in nums:
        count += 1
        if i + j == target:
            print(f"{i} + {j} = {target}")
            break

print(count)
