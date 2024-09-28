# Calculate the maximum value of a matrix and its position (row, column).

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

max_element = 0
max_i = 0
max_j = 0

for i in range(n):
    for j in range(m):
        if a[i][j] >= max_element:
            max_element = a[i][j]
            max_i = i
            max_j = j

print(f"the maximum = {max_element:.1f} in row {max_i} column {max_j}")