# Write a Python program that takes a number as input and generates all its divisors, displaying each number that divides the given number exactly without leaving a remainder.

num = int(input("Enter Number to Check:: "))

for i in range(1, 100):
    if num % i == 0:
        print(i, end=' ')
