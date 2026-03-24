
# for num in user_list_1:
#     n = 1
#     factorial = 1
#     while factorial <= num:
#         factorial = n * factorial
#         if factorial != 1 and factorial == num:
#             break
#         n+=1
#         # print(num, factorial)
#     print(f"Is Factorial equal or not {num} {factorial}", num == factorial)


user_list_1 = [1, 5, 6, 24, 100, 120, 720]
factorial = [1]

for i in range(1, 16):
    factorial.append(i*factorial[i-1])
print(factorial)

for num in user_list_1:
    try:
        print("In List:", factorial.index(num))
    except ValueError:
        print("Not in List: ", num)
