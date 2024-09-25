# Given a list of N values determine the number that appears more often and the positions in the list where it appears.

n = int(input())
ns = [int(input()) for i in range(n)]

i = 0
count = {}

for i, value in enumerate(ns):
    if value in count:
        count[value] += 1
    else:
        count[value] = 1

most_frequent = max(count, key=count.get)
max_count = count[most_frequent]

positions = [i for i, value in enumerate(ns) if value == most_frequent]

print(f"Number that appears most often = {most_frequent:.2f}")

j = 0
for j in positions:
    print(f"Position: {j}")