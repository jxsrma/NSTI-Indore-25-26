def rotate(li, n):
    length = len(li)
    li1 = li[:length-n]
    print("First Half", li1)

    li2 = li[length-n:]
    print("Second Half", li2)
    return li2+li1


li = [1, 2, 3, 4, 5]
n = 2

print(rotate(li, n))
