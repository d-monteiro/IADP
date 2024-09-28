# Given a matrix calculate the transpose matrix.

n = int(input("Number of rows ="))
m = int(input("Number of columns ="))

a = []



for i in range(n):
    row = []
    for j in range(m):
        element = float(input(f"a[{i}][{j}]="))
        row.append(element)
    a.append(row)
        
for i in range(n):
    print(a[i])

print("Matrix transpose:")

t = [[0 for _ in range(n)] for _ in range(m)]

for i in range(n):
    for j in range(m):
        t[j][i] = a[i][j]
        
for i in range(m):
    print(t[i])