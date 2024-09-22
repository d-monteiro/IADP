import math

x = float(input("x:"))
y = float(input("y:"))

a = 3*y + math.sqrt((2*x) * (y+10))
b = 4*x + y
answer = a / b

print(f"f({x:.2f},{y:.2f}) = {answer:.2f}")