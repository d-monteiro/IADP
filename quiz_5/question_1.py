# Given a list of N values determine the two elements of higher value using a while loop. Assume that these values are distinct.

n = int(input("n:"))
i = 1
m = 0
m2 = 0

while i <= n:
    v = int(input(f"value {i}:"))
    if v > m:
        m2 = m
        m = v
    elif v > m2:
        m2 = v
    i = i + 1
    
print(f"Highest value = {m} 2nd. Highest value = {m2}")