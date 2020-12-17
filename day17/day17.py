with open("input.txt") as file:
    lines = file.read().splitlines()

size = {
    "x": [0, len(lines[0]) - 1],
    "y": [0, len(lines) - 1],
    "z": [0, 0]
}

active = "#"
inactive = "."

def construct_space():
    space = {}

    for y, line in enumerate(lines):
        for x, state in enumerate(line):
            space[(x, y, 0)] = state

    return space

def get_state(space, x, y, z, w = None):
    if w == None:
        return space.get((x, y, z), inactive)
    return space.get((x, y, z, w), inactive)

def find_adjacent_active(space, x, y, z, w = None):
    count = 0

    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                if w == None:
                    if dx == 0 and dy == 0 and dz == 0:
                        continue
                    
                    if get_state(space, x + dx, y + dy, z + dz) == active:
                        count += 1
                else:
                    for dw in range(-1, 2):
                        if dx == dy == dz == dw == 0:
                            continue

                        if get_state(space, x + dx, y + dy, z + dz, w + dw) == active:
                            count += 1

    return count

def conduct_cycle_3d(space):
    for dimension in "xyz":
        size[dimension][0] -= 1
        size[dimension][1] += 1
    
    new = space.copy()

    for x in range(size["x"][0], size["x"][1] + 1):
        for y in range(size["y"][0], size["y"][1] + 1):
            for z in range(size["z"][0], size["z"][1] + 1):
                state = get_state(space, x, y, z)
                adjacent = find_adjacent_active(space, x, y, z)

                if state == active and adjacent != 2 and adjacent != 3:
                    del new[(x, y, z)]
                elif state == inactive and adjacent == 3:
                    new[(x, y, z)] = active

    return new

def convert_to_4d(space):
    size["w"] = [0, 0]
    return {(x, y, z, 0): state for ((x, y, z), state) in space.items()}

def conduct_cycle_4d(space):
    for dimension in "xyzw":
        size[dimension][0] -= 1
        size[dimension][1] += 1

    new = space.copy()

    for x in range(size["x"][0], size["x"][1] + 1):
        for y in range(size["y"][0], size["y"][1] + 1):
            for z in range(size["z"][0], size["z"][1] + 1):
                for w in range(size["w"][0], size["w"][1] + 1):
                    state = get_state(space, x, y, z, w)
                    adjacent = find_adjacent_active(space, x, y, z, w)

                    if state == active and adjacent != 2 and adjacent != 3:
                        del new[(x, y, z, w)]
                    elif state == inactive and adjacent == 3:
                        new[(x, y, z, w)] = active
                    
    return new

def count_active_after_cycles(space, cycle_function):
    for i in range(6):
        space = cycle_function(space)
    
    print(list(space.values()).count(active))

space = construct_space()
count_active_after_cycles(space, conduct_cycle_3d)

space = convert_to_4d(space)
count_active_after_cycles(space, conduct_cycle_4d)
                    
