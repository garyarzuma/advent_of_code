import fileinput

input = fileinput.input('input')
line = ''

for line in input:
    line = list(line)
    line.pop()

# print(line)

# Expand
expanded = []
id = '0'
freeBlock = False
for i, num in enumerate(line):
    if freeBlock:
        expanded += ['.']*int(num)
        freeBlock = False
    else:
        expanded += [id]*int(num)
        freeBlock = True
        id = str(int(id) + 1)

# Compress
for i, num in enumerate(expanded):
    while i < len(expanded) and expanded[i] == '.':
        test = expanded.pop()
        if test != '.':
            expanded[i] = test

# Checksum
checksum = 0
for i, num in enumerate(expanded):
    checksum += i*int(num)

print(checksum)
