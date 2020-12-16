import functools
import re

with open("input.txt") as file:
    lines = file.read().splitlines()

def parse_fields():
    fields = {}
    
    for line in lines[:lines.index("")]:
        groups = re.match("(.+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)", line).groups()
        fields[groups[0]] = ((int(groups[1]), int(groups[2])), (int(groups[3]), int(groups[4])))

    return fields

def within_range(field, number):
    ranges = fields[field]
    return ranges[0][0] <= number <= ranges[0][1] or ranges[1][0] <= number <= ranges[1][1]

def matches_any_field(number):
    for field in fields:
        if within_range(field, number):
            return True
    return False

def parse_ticket(line):
    return [int(x) for x in line.split(",")]

def find_errors_and_valids():
    error_rate = 0
    valid_tickets = []
    
    for ticket in map(parse_ticket, lines[lines.index("nearby tickets:") + 1:]):
        valid = True
        
        for number in ticket:
            if not matches_any_field(number):
                error_rate += number
                valid = False
                break

        if valid:
            valid_tickets.append(ticket)

    return error_rate, valid_tickets

def valid_for_all_tickets(field, field_index, tickets):
    for ticket in tickets:
        if not within_range(field, ticket[field_index]):
            return False
    return True

def determine_possible_fields(field_index, tickets):
    possible = []
    
    for field in fields:
        if valid_for_all_tickets(field, field_index, tickets):
            possible.append(field)

    return possible
        
def determine_fields(valid_tickets):
    possible = {}
        
    for field_index in range(len(fields)):
        possible_fields = determine_possible_fields(field_index, valid_tickets)
        possible[field_index] = possible_fields

    possible = dict(sorted(possible.items(), key = lambda item: len(item[1])))
    seen = []
    
    for (field_index, possible_fields) in possible.items():
        if len(possible_fields) == 1:
            field = possible_fields[0]
        else:
            field = list(filter(lambda field: field not in seen, possible_fields))[0]
            
        seen.append(field)
        possible[field_index] = field

    return possible

def multiply_departure_fields():
    my_ticket = parse_ticket(lines[lines.index("your ticket:") + 1])
    product = 1

    for i, value in enumerate(my_ticket):
        if fields[i].startswith("departure"):
            product *= value

    print(product)

fields = parse_fields()

error_rate, valid_tickets = find_errors_and_valids()
print(error_rate)

fields = determine_fields(valid_tickets)
multiply_departure_fields()
