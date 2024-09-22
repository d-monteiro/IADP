# Given a sequence of n values ​​and their respective weights, calculates the weighted average (Xi - Values; Pi - Weights) using a for loop. (input order: n; X0; P0; X1; P1;...)

n = int(input("n:"))
sum1=0
sum2=0

for i in range(0,n):
    x = int(input(f"X{i}:"))
    p = int(input(f"P{i}:"))
    sum1 += x*p
    sum2 += p
    
print(f"Weighted average = {sum1/sum2:.2f}")