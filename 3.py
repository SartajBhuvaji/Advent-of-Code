def increasing(levels):
    print("In inc")
    for i in range(len(levels)-1):
        if levels[i] > levels[i+1]:
            #print(levels[i], '<', levels[i+1])
            return 0
        elif abs(levels[i] - levels[i+1]) < 1 or abs(levels[i] - levels[i+1]) > 3:
            #print(levels[i] - levels[i+1] ,'< 1' , ' or' , levels[i] - levels[i+1], '> 3')
            return 0
    return 1

def decreasing(levels):
    print("In dec")
    for i in range(len(levels)-1):
        if levels[i] < levels[i+1]:
           # print(levels[i], '>', levels[i+1])
            return 0
        elif levels[i] - levels[i+1] < 1 or levels[i] - levels[i+1] > 3:
            #print(levels[i] - levels[i+1] ,'< 1' , ' or' , levels[i] - levels[i+1], '> 3')
            return 0
    return 1

safe_count = 0
with open('input.txt') as f:
    for line in f:
        levels =  list(map(int, line.split()))
        print("dsdsd", levels)
        if len(levels)> 2 and levels[0] < levels[1]:
            value = increasing(levels)
            print(value, levels)
            safe_count+=value

        elif len(levels)> 2 and levels[0] > levels[1]:
            value = decreasing(levels)
            print(value, levels)
            safe_count+=value
        else:
            print("invalid input")

print("Final count: ", safe_count)


