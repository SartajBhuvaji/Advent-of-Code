#670-685
def increasing(levels):
    print("In inc")
    for i in range(len(levels)-1):
        if levels[i] >= levels[i+1]:
            return (i, i+1)
        elif abs(levels[i] - levels[i+1]) < 1 or abs(levels[i] - levels[i+1]) > 3:
            return (i, i+1)
    return (1, -1)

def decreasing(levels):
    print("In dec")
    for i in range(len(levels)-1):
        if levels[i] <= levels[i+1]:
            return (i, i+1)
        elif levels[i] - levels[i+1] < 1 or levels[i] - levels[i+1] > 3:
            return (i, i+1)
    return (1,-1)

safe_count = 0
with open('input.txt') as f:
    for line in f:
        levels =  list(map(int, line.split()))
        print(levels)
        
        if len(levels)> 2 and levels[0] <= levels[1]:
            a,b = increasing(levels)
            if b == -1:
                safe_count +=1
            else:
                possible = 0
                levels_copy = levels.copy()
                del levels_copy[a] # deleting i
                a1,b1 = increasing(levels_copy)
                if b1 == -1: # worked
                    safe_count +=1
                    continue
                a2, b2 = decreasing(levels_copy)
                if b2 == -1:
                    safe_count +=1
                    continue

                levels_copy = levels.copy()
                del levels_copy[b] # deleting i+1
                a3,b3 = increasing(levels_copy)
                if b3 == -1: # worked
                    safe_count +=1
                    continue
                a4, b4 = decreasing(levels_copy)
                if b4 == -1:
                    safe_count +=1
                    continue
                
                levels_copy = levels.copy()
                del levels_copy[0] # deleting i=0 #edge case!
                a5,b5 = increasing(levels_copy)
                if b5 == -1: # worked
                    safe_count +=1
                    continue
                a6, b6 = decreasing(levels_copy)
                if b6 == -1:
                    safe_count +=1
                    continue
                
        elif len(levels)> 2 and levels[0] >= levels[1]:
            a,b = decreasing(levels)
            if b == -1:
                safe_count +=1
            else:
                possible = 0
                levels_copy = levels.copy()
                del levels_copy[a] # deleting i
                a1,b1 = increasing(levels_copy)
                if b1 == -1: # worked
                    safe_count +=1
                    continue
                a2, b2 = decreasing(levels_copy)
                if b2 == -1:
                    safe_count +=1
                    continue

                levels_copy = levels.copy()
                del levels_copy[b] # deleting i+1
                a3,b3 = increasing(levels_copy)
                if b3 == -1: # worked
                    safe_count +=1
                    continue
                a4, b4 = decreasing(levels_copy)
                if b4 == -1:
                    safe_count +=1
                    continue

                levels_copy = levels.copy()
                del levels_copy[0] # deleting i=0 #edge case!
                a5,b5 = increasing(levels_copy)
                if b5 == -1: # worked
                    safe_count +=1
                    continue
                a6, b6 = decreasing(levels_copy)
                if b6 == -1:
                    safe_count +=1
                    continue
                
                    
        else:
            print("invalid input")
            break

print("Final count: ", safe_count)
