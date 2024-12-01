
from collections import defaultdict
total_similarity = 0

left = []
counts = defaultdict(int)
with open('input.txt') as f:
    for line in f:
        l, r = line.split()
        left.append(int(l))
        counts[int(r)] += 1
        

for i in range(len(left)):
    total_similarity += left[i]*counts[left[i]]

print(total_similarity)