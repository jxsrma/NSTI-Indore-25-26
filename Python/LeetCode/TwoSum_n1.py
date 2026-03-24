nums = [2, 7, 11, 15]
target = 26

count = 0

checkSet = set(nums)

for i in nums:
    count += 1
    if (target - i) in nums:
        print(f"{i} + {target - i} = {target}")
        # print(nums.index(i), nums.index(target-i))
        break

print(count)