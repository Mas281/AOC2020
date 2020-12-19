with open("input.txt") as file:
    lines = [line.replace(" ", "") for line in file.read().splitlines()]

def find_bracket_section(expression, start):
    depth = 0

    for i, char in enumerate(expression[start:]):
        if char == "(":
            depth += 1
        elif char == ")":
            depth -= 1

        if depth == 0:
            return expression[start:i + start + 1]

def parse_terms(expression):
    terms = []
    i = 0

    while i < len(expression):
        char = expression[i]
        
        if char.isdigit():
            terms.append(int(char))
            i += 1
        elif char == "+" or char == "*":
            terms.append(char)
            i += 1
        elif char == "(":
            bracket_section = find_bracket_section(expression, i)
            terms.append(bracket_section)

            i += len(bracket_section)
            
    return terms

def evaluate_left_to_right(terms):
    current = terms[0]

    for i in range(1, len(terms), 2):
        if terms[i] == "+":
            current += terms[i + 1]
        else:
            current *= terms[i + 1]

    return current

def evaluate_with_precedence(terms):
    while "+" in terms:
        for i in range(1, len(terms) - 1):
            term = terms[i]

            if term == "+":
                terms[i] = terms[i - 1] + terms[i + 1]
                terms[i - 1] = ""
                terms[i + 1] = ""

                terms = list(filter(lambda string: string != "", terms))
                break

    return evaluate_left_to_right(terms)

def evaluate_terms(terms, evaluate_function):
    for i, term in enumerate(terms):
        if str(term).startswith("("):
            terms[i] = evaluate_expression(term[1:-1], evaluate_function)
            
    return evaluate_function(terms)

def evaluate_expression(expression, evaluate_function):
    terms = parse_terms(expression)
    return evaluate_terms(terms, evaluate_function)
    
def find_sum_of_values(evaluate_function):
    print(sum([evaluate_expression(line, evaluate_function) for line in lines]))

find_sum_of_values(evaluate_left_to_right)
find_sum_of_values(evaluate_with_precedence)
