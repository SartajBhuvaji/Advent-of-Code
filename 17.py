# with open('input.txt') as f:
#     inp = f.readline()
# print(len(inp))


inp = '2333133121414131402'

disc = ''
id = 0

for i in range(0, len(inp), 2):
    disc += str(id) * int(inp[i])
    if i + 1 < len(inp):
        disc += str('.') * int(inp[i + 1])
    id += 1

#print(disc)

output = 0
left, right = 0, len(disc) - 1

id = 0
while left <= right:
    while left <= right and disc[left] != '.':
        output += int(disc[left]) * id
        #print(int(disc[left]), " * ", id)
        id += 1
        left += 1

    while left <= right and disc[left] == '.' and disc[right] != '.':
        output += int(disc[right]) * id
        #print(int(disc[right]), " * ", id)
        id += 1
        right -= 1
        left += 1

    while right >= left and disc[right] == '.':
        right -= 1

print(output)
