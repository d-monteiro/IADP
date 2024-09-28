name = input("Filename:")
estado1 = input("'estado' column value:")

file = open(name,'r')

lines = file.readlines()
data = lines[1:11]

header = lines[0].strip() + ';sexo'
print(header)

for line in data:
    columns = line.strip().split(';')
    estado2 = columns[6]
    
    if estado1[0] == estado2[0]:
        sexo = 'M'
        if estado2.endswith('a'):
            sexo = 'F'
    else:
        sexo = ''
        
    columns.append(sexo)
    
    print(';'.join(columns))