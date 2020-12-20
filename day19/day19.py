with open("input.txt") as file:
    lines = file.read().splitlines()

def parse_rules():
    rules = {}

    for line in lines[:lines.index("")]:
        split = line.split(" ")
        number = int(split[0][:-1])

        if len(split) == 2:
            if split[1].isdigit():
                rules[number] = int(split[1])
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

def find_patterns(rule_no):
    rule = rules[rule_no]

    if type(rule) == str:
        return [rule]
    elif type(rule) == int:
        return find_patterns(rule)

    patterns = []

    for subrule in rule:
        temp = []
        
        for subrule_no in subrule:
            subrule_patterns = find_patterns(subrule_no)

            if len(temp) == 0:
                for subrule_pattern in subrule_patterns:
                    temp.append("".join(subrule_pattern))
            else:
                temp_deep = []

                for temp_item in temp:
                    for subrule_pattern in subrule_patterns:
                        subrule_pattern_string = "".join(subrule_pattern)
                        temp_deep.append(temp_item + subrule_pattern_string)

                temp = temp_deep
            
        patterns.extend(temp)
        
    return patterns

def count_matching(messages):
    print(len(list(filter(lambda msg: msg in patterns, messages))))

rules = parse_rules()
patterns = find_patterns(0)

messages = lines[lines.index("") + 1:]
count_matching(messages)
