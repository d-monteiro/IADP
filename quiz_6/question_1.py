# For a given integer, print the respective multiplication table (from 1 to 10) using a for loop.

n = int(input("n:"))

for i in range(1,11):
    print(f"{n} x {i} = {n*i}")