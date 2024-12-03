import re
# Regex pattern
pattern = r"mul\((\d{1,3}),(\d{1,3})\)" # mul(x,y)

with open('input.txt') as f:
    line = f.readline()
    matches = re.findall(pattern, line)
    #print(matches)

output = 0
for a,b in matches:
    output += int(a) * int(b)

print(output) 