# DP ? i guess

output = 0 

def calculate(ans, numbers):
    if len(numbers) == 1:
        if numbers[0] == ans:
            return True
        return False

    if numbers[0] > ans:
        return False
    
    # multiple numbers[0], numbers[1]
    mul = numbers[0] * numbers[1]
    new_array1 = [mul] + numbers[2:]

    # add numbers[0], numbers[1]
    add = numbers[0] + numbers[1]
    new_array2 = [add] + numbers[2:]

    return calculate(ans, new_array1) or calculate(ans, new_array2)


with open('input.txt') as f:
    for line in f:
        ans, inp = line.split(':')
        ans = int(ans)
        numbers = [int(no) for no in inp.split(' ')[1:]]
        #print(ans, numbers)
        #print(numbers[2:])

        if calculate(ans, numbers): output+=ans

print(output)