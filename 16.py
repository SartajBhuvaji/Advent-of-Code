from collections import defaultdict

matrix = []
nodes = defaultdict(list)

# Reading input and populating the matrix and nodes
with open('input.txt') as f:
    for line in f:
        row = []
        for element in line.strip():
            if element != '.':
                nodes[element].append([len(matrix), len(row)])
            row.append(element)
        matrix.append(row)

rows = len(matrix)
cols = len(matrix[0])

output = 0
# Function to find antinodes
def mark_antinodes(x1, y1, x2, y2):
    global output
    dx = x2 - x1
    dy = y2 - y1

    # Calculate potential antinode positions
    p1x, p1y = x1 - dx, y1 - dy
    p2x, p2y = x2 + dx, y2 + dy

    # Mark antinodes if they are within bounds
    if 0 <= p1x < rows and 0 <= p1y < cols and matrix[p1x][p1y] in ['.', '#']: 
        output+=1
        antinodes.add((p1x, p1y))
        matrix[p1x][p1y] = '#'

    if 0 <= p2x < rows and 0 <= p2y < cols and matrix[p2x][p2y] in ['.', '#']: 
        output+=1
        antinodes.add((p2x, p2y))
        matrix[p2x][p2y] = '#'


# Set to track unique antinode locations
antinodes = set()

# Process each frequency group to find antinodes
for k, v in nodes.items():
    print(k, v)
    for i in range(len(v) - 1):
        for j in range(i + 1, len(v)):
            x1, y1 = v[i]
            x2, y2 = v[j]
            mark_antinodes(x1, y1, x2, y2)

# Print the resulting matrix
# for i in range(rows):
#     for j in range(cols):
#         print(matrix[i][j], end=' ')
#     print()

# Output the count of unique antinodes
print(len(antinodes))
print(output)
