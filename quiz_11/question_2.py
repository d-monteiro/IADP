# Given a text insert spaces between words so that all lines have the same number of characters.

n = int(input())

i = 0
max_length = 0
max_index = 0
lines = []
for i in range(n):
    lines.append(input())

for line in lines:
    if len(line) > max_length:
        max_length = len(line)
        max_index = lines.index(line)
    
justified_lines = []

for line in lines:
    
    words = line.split()
    for i in range(len(words) - 1):
        words[i] += ' '
    num_spaces = max_length - len(line)
    num_gaps = len(words) - 1
    
    if num_gaps > 0:
        # Calculate the number of spaces to add between words
        spaces_per_gap = num_spaces // num_gaps
        extra_spaces = num_spaces % num_gaps
        
        # Create the justified line
        justified_line = words[0]
        for i in range(1, len(words)):
            spaces_to_add = spaces_per_gap + (1 if i <= extra_spaces else 0)
            justified_line += ' ' * spaces_to_add + words[i]
    else:
        # If there's only one word, just add spaces at the end
        justified_line = words[0] + ' ' * num_spaces
    
    justified_lines.append(justified_line)
    
    
for line in justified_lines:
    print(line)