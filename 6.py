import re

mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"   # Matches mul(x,y)
control_pattern = r"(do\(\)|don't\(\))"       # Matches do() or don't()

lines = ''
with open('input.txt') as f:
    for line in f:
        lines+=line
    

enabled = True
output = 0

for match in re.finditer(f"{control_pattern}|{mul_pattern}", lines):
    match_str = match.group(0)
    
    if match_str == "do()":
        enabled = True
    elif match_str == "don't()":
        enabled = False
    
    elif match.group(1) is None:  #not a control one
        if enabled: 
            a, b = map(int, match.groups()[1:3])
            output += a * b

print(output)
