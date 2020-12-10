with open("input.txt") as file:
    lines = file.read().splitlines()

def split_line(line):
    split = line.split(" ")

    length = split[0].split("-")
    minimum = int(length[0])
    maximum = int(length[1])

    char = split[1][0]
    password = split[2]

    return (minimum, maximum, char, password)

def count_valid(lines):
    lines = [split_line(line) for line in lines]

    print(len(list(filter(lambda line: valid_occurrences(line), lines))))
    print(len(list(filter(lambda line: valid_positions(line), lines))))

def valid_occurrences(line):
    occurrences = len(list(filter(lambda c: c == line[2], line[3])))
    return line[0] <= occurrences <= line[1]

def valid_positions(line):
    return (line[3][line[0] - 1] == line[2]) ^ (line[3][line[1] - 1] == line[2])

count_valid(lines)
