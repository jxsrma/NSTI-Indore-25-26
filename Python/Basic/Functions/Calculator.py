def add(a: float, b):
    print(f'{a} + {b} = {a+b}')


def sub(a, b):
    print(f'{a} - {b} = {a-b}')


def mult(a, b):
    print(f'{a} * {b} = {a*b}')


def div(a, b):
    if b == 0:
        print('Cannot Divide By ZERO')
    else:
        print(f'{a} / {b} = {a/b}')


add(5, 3)
sub(456, 249)
mult(8, 4)
div(8, 0)

# add 3

def add3(a,b,c):
    print(a+b+c)

add3(1,2,5)


