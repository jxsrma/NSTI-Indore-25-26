def add(*nums):
    result = 0
    for num in nums:
        result += num
    return result


sum = add(5, 6, 44, 6, 8, 6, 4, 3, 2, 35, 8, 9, 97, 5, 6, 5, 4)
print(sum)


def printDetail(**StudentDetail):

    for key, value in StudentDetail.items():
        print(f'{key}: {value}')


# printDetail("Ram",5,15,12308104785,"Indore")
printDetail(name="Ram", roll=5, age=15, phone=12308104785, city="Indore")
printDetail(FirstName="Ram", LastName="Verma", roll=5, age=15, phone=12308104785,
            city="Indore", addhar=123456789012)
