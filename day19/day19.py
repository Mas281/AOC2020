import functools
import re

with open("input.txt") as file:
    lines = file.read().splitlines()

def parse_rules():
    rules = {}

    for line in lines[:lines.index("")]:
        split = line.split(" ")
        number = int(split[0][:-1])

        if len(split) == 2:
            if split[1].isdigit():
                rules[number] = [[int(split[1])]]
            else:
                rules[number] = split[1][1:-1]
        else:
            subrules = []
            current = []

            for section in split[1:]:
                if section == "|":
                    subrules.append(current)
                    current = []
                else:
                    current.append(int(section))

            subrules.append(current)
            rules[number] = subrules
        
    return rules

def make_regex(rule_no, eight_depth = 0, eleven_depth = 0):
    if type(rule := rules[rule_no]) == str:
        return rule

    if rule_no == 8:
        eight_depth += 1
    elif rule_no == 11:
        eleven_depth += 1

    return "" if eight_depth > 5 or eleven_depth > 4 else "(" + "|".join([functools.reduce(lambda current, subrule_no:
        current + make_regex(subrule_no, eight_depth, eleven_depth), subrule, "") for subrule in rule
    ]) + ")"

def count_matching():
    messages = lines[lines.index("") + 1:]
    pattern = make_regex(0)
    print(len(list(filter(lambda msg: re.fullmatch(pattern, msg) != None, messages))))

rules = parse_rules()
count_matching()

rules[8] = [[42], [42, 8]]
rules[11] = [[42, 31], [42, 11, 31]]

count_matching()
