grid =[]
output = 0

start_position = []

with open('input.txt') as f:
    for line in f:
        row = []
        for element in line:
            row.append(element)
            if element == '^':
                start_position=[len(grid), len(row)-1]
        grid.append(row)

print(start_position)
print(grid[start_position[0]][start_position[1]])

visited = set() # to keep unique counts
# While guard is in bounds:
x, y = start_position[0], start_position[1]
direction = 'U'

def helper(x,y):
    global output
    if (x,y) not in visited:
        visited.add((x,y))
        output+=1


while x>=0 and x<len(grid)-1 and y>=0 and y<len(grid[0])-1:
    if direction == 'U':
        # if no obstackle
        if grid[x-1][y] != '#':
            x = x-1
            helper(x,y)
        else:
            direction = 'R'
            continue
        
    elif direction == 'R':
        # if no obstackle
        if grid[x][y+1] != '#':
            y= y+1
            helper(x,y)
        else:
            direction = 'D'
            continue

    elif direction == 'D':
        # if no obstackle
        if grid[x+1][y] != '#':
            x= x+1
            helper(x,y)
        else:
            direction = 'L'
            continue

    elif direction == 'L':
        # if no obstackle
        if grid[x][y-1] != '#':
            y = y-1
            helper(x,y)
        else:
            direction = 'U'
            continue

print(output)
