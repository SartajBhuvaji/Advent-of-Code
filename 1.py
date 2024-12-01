
total_distance = 0
left = []
right = []

with open('input.txt') as f:
    for line in f:
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))

left.sort()
right.sort()

for i in range(len(left)):
    total_distance += abs(left[i] - right[i])

print(total_distance)
        