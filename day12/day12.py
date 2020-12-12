with open("input.txt") as file:
    lines = file.read().splitlines()

instructions = [(line[:1], int(line[1:])) for line in lines]

def find_final_distance():
    x, y, = 0, 0
    
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    facing = directions[0]

    for (action, number) in instructions:
        if action == "N":
            y += number
        elif action == "S":
            y -= number
        elif action == "E":
            x += number
        elif action == "W":
            x -= number
        elif action == "L":        
            facing = directions[(directions.index(facing) - number // 90) % 4]
        elif action == "R":
            facing = directions[(directions.index(facing) + number // 90) % 4]
        elif action == "F":
            x += facing[0] * number
            y += facing[1] * number

    print(abs(x) + abs(y))

def find_actual_distance():
    x, y = 0, 0
    wx, wy = 10, 1

    for (action, number) in instructions:
        if action == "N":
            wy += number
        elif action == "S":
            wy -= number
        elif action == "E":
            wx += number
        elif action == "W":
            wx -= number
        elif action == "L":    
            for _ in range(number // 90):
                wx, wy = -wy, wx
        elif action == "R":
            for _ in range(number // 90):
                wx, wy = wy, -wx
        elif action == "F":
            x += wx * number
            y += wy * number

    print(abs(x) + abs(y))

find_final_distance()
find_actual_distance()
