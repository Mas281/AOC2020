import functools

with open("input.txt") as file:
    lines = file.read().splitlines()

def grid(x, y):
    line = lines[y]
    return line[x % len(line)]

def count_trees(delta_x, delta_y):
    pos_x = 0
    pos_y = 0

    trees = 0

    for _ in range(len(lines)):
        if grid(pos_x, pos_y) == "#":
            trees += 1
    
        pos_x += delta_x
        pos_y += delta_y

        if pos_y >= len(lines):
            break

    return trees

def count_deltas(deltas):
    trees = [count_trees(dx, dy) for (dx, dy) in deltas]
    print(functools.reduce(lambda x, y: x * y, trees, 1))

count_deltas([(3, 1)])
count_deltas([(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)])
