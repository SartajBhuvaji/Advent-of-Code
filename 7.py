
output = 0
matrix = []
with open('input.txt') as f:
    for line in f:
        lines = list(line.strip()) 
        matrix.append(lines)

rows = len(matrix)
cols = len(matrix[0])
# print(rows, cols)

# Seatch 'XMAS' 
'''
This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words.
'''
def search(i,j):
    occurance = 0
    # Horizontal forward search
    if j + 3 < cols and matrix[i][j+1] == 'M' and matrix[i][j+2] == 'A' and matrix[i][j+3] == 'S':
        occurance += 1

    # Horizontal backward search
    if j - 3 >= 0 and matrix[i][j-1] == 'M' and matrix[i][j-2] == 'A' and matrix[i][j-3] == 'S':
        occurance += 1

    # Vertical downward search
    if i + 3 < rows and matrix[i+1][j] == 'M' and matrix[i+2][j] == 'A' and matrix[i+3][j] == 'S':
        occurance += 1

    # Vertical upward search
    if i - 3 >= 0 and matrix[i-1][j] == 'M' and matrix[i-2][j] == 'A' and matrix[i-3][j] == 'S':
        occurance += 1

    # positive diagonals
    if i + 3 < rows and j + 3 < cols and \
        matrix[i+1][j+1] == 'M' and \
        matrix[i+2][j+2] == 'A' and \
        matrix[i+3][j+3] == 'S':
        occurance += 1

    if i + 3 < rows and j - 3 >= 0 and \
        matrix[i+1][j-1] == 'M' and \
        matrix[i+2][j-2] == 'A' and \
        matrix[i+3][j-3] == 'S':
        occurance += 1

    # negative diagonals
    if i - 3 >= 0 and j - 3 >= 0 and \
        matrix[i-1][j-1] == 'M' and \
        matrix[i-2][j-2] == 'A' and \
        matrix[i-3][j-3] == 'S':
        occurance += 1

    if i - 3 >= 0 and j + 3 < cols and \
        matrix[i-1][j+1] == 'M' and \
        matrix[i-2][j+2] == 'A' and \
        matrix[i-3][j+3] == 'S':
        occurance += 1

    return occurance


for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == 'X':
            output += search(i, j)
            #print(i,j)


print(output)
# for i in range(rows):
#     for j in range(cols):
#         print(matrix[i][j], end= '')
#     print('\n')
