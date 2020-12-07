with open("input.txt") as file:
    lines = file.read().splitlines()

def parse_rules():
    rules = {}

    for line in lines:
        split = line[:-1].split(" bags contain ")

        colour = split[0]
        rules[colour] = {}

        for item in split[1].split(", "):
            inner_split = item.split(" ")

            if inner_split[0] == "no":
                continue

            inner_colour = " ".join(inner_split[1:3])
            amount = int(inner_split[0])

            rules[colour][inner_colour] = amount

    return rules

def can_have_shiny_gold(colour):
    if colour == shiny_gold:
        return False

    for inner_colour in rules[colour]:
        if inner_colour == shiny_gold or can_have_shiny_gold(inner_colour):
            return True

    return False

def count_can_have_shiny_gold():
    print(len(list(filter(lambda colour: can_have_shiny_gold(colour), rules))))

def count_total_bags(colour):
    count = 0

    for (inner_colour, amount) in rules[colour].items():
        count += amount * (1 + count_total_bags(inner_colour))

    return count

shiny_gold = "shiny gold"

rules = parse_rules()

count_can_have_shiny_gold()
print(count_total_bags(shiny_gold))
