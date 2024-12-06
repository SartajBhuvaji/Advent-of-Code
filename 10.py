from collections import defaultdict
import itertools

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
   # print("func call")
    #75,47,61,53,29
    if len(update) == 0:
       # print("FALSE")
        return False
    if len(update) == 1:
        #print("TRUE")
        return True
    
    first = update[0]
    for no in update[1:]:
        if no not in adj_list[first]:
            return False
    return correct_order_check(update[1:])


failed_updates = []
for update in updates:
    if len(update)>0:
        if not correct_order_check(update):
            failed_updates.append(update)

output = 0
for update in failed_updates:
   permutations = list(itertools.permutations(update))
   for permute in permutations:
        if correct_order_check(permute):
            mid = len(permute) // 2
            output += permute[mid]
            break

print(output)