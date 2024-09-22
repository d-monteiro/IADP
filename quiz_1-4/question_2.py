n = int(input("number:"))

print("Numbers:")

a = n // 100

b = n // 10 - a*10

c = n // 1 - a*100 - b*10

print(a * 100 + b * 10 + c)
print(a * 100 + c * 10 + b)
print(b * 100 + c * 10 + a)
print(b * 100 + a * 10 + c)
print(c * 100 + b * 10 + a)
print(c * 100 + a * 10 + b)