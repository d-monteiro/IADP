# Create program that reads a list of names in a given text file. After reading the file, the program should print all names sorted alphabetically, and the total number of names in that file.

name = input("Filename:")

file = open(name,'r')

names = file.readlines()

names.sort()

i = 0
for name in names:
    i = i + 1
    print(name)
    
print(f"Count of names: {i}")