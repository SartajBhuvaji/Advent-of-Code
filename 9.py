from collections import defaultdict

output = 0
adj_list = defaultdict(set)
updates = []

with open('input.txt') as f:
    for line in f:
        line = line.strip() 
        if '|' in line:
            # page ordering rule
            a, b = map(int, line.split('|'))
            adj_list[a].add(b)
        elif ',' in line:
            #comma-separated 
            updates.append(list(map(int, line.split(','))))
        else:
            # space-separated
            updates.append(list(map(int, line.split())))


#print(adj_list[61])
# print(updates)

def correct_order_check(update):
    #75,47,61,53,29
    if len(update) == 0:
        return False
    if len(update) == 1:
        return True
    
    first = update[0]
    for no in update[1:]:
        if no not in adj_list[first]:
            return False
    
    return correct_order_check(update[1:])

output = 0
for update in updates:
    if correct_order_check(update):
        mid = len(update) // 2
        output+= update[mid]

print(output)
