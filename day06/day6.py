import string

with open("input.txt") as file:
    lines = file.read().splitlines()

def sum_groups(function, default = ""):
    count = 0
    current = set(default)
    
    for line in lines:
        if line == "":
            count += len(set(current))
            current = set(default)
            continue
        
        current = function(current, set(line))

    count += len(current)
    print(count)

sum_groups(lambda current, line: current | line)
sum_groups(lambda current, line: current & line, string.ascii_lowercase)
