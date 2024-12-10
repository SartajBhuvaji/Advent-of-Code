from collections import deque
grid = []
start_location = []
with open('input.txt') as f:
    for line in f:
        row = []
        for no in line.strip():
            if no == '0':
                start_location.append((len(grid), len(row)))
            row.append(int(no))
        grid.append(row)

rows = len(grid)
cols = len(grid[0])

# for i in range(rows):
#     for j in range(cols):
#         print(grid[i][j], end=' ')
#     print()

# print(start_location)

def bfs(i,j):
    q = deque([(i,j)])
    visited = set()
    visited.add((i,j))
    output = 0
    while q:
        x,y = q.popleft()
        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != grid[x][y]+1: continue
            #if (nx,ny) in visited: continue
            if grid[nx][ny] == 9 and (nx,ny)not in visited:
                visited.add((nx,ny))
                #print("9: ", nx, ny)
                output += 1
            q.append((nx,ny))
    
    return output
            
total_count = 0
for i, j in start_location:
    print(i, j)
    counts = bfs(i,j)
    #print(counts)
    total_count += counts
    #break

print(total_count)
