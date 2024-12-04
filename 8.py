output = 0
matrix = []
with open('input.txt') as f:
    for line in f:
        lines = list(line.strip()) 
        matrix.append(lines)

rows = len(matrix)
cols = len(matrix[0])

def search(i, j):
 
    if (i+1 < rows and j+1 < cols and i-1 >= 0 and j-1 >= 0):
        corners = [
            matrix[i - 1][j - 1],   # rotating corners
            matrix[i - 1][j + 1],  
            matrix[i + 1][j + 1],  
            matrix[i + 1][j - 1],  
        ]
        if "".join(corners) in ("MMSS", "MSSM", "SSMM", "SMMS"):
            return 1
    return 0

for i in range(rows-1):
    for j in range(cols-1):
        if matrix[i][j] == 'A':
            output+=search(i,j)

print(output)
