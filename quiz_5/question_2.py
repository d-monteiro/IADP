# Given an integer value determine its factors (numbers that divide the given number) using the while loop.

n = int(input("Factors of:"))
    
i = 1
while i <= n:
    if n % i == 0:
        print(i)
    i += 1