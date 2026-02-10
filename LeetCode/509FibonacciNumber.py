def fib(n: int) -> int:
    n1 = 0
    n2 = 1

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(2,n+1):
            n3 = n1+n2
            print(n1,n2,n3)
            n1 = n2
            n2 = n3
        return n3

print(fib(7))