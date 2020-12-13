import math

with open("input.txt") as file:
    lines = file.read().splitlines()

earliest = int(lines[0])
buses = [0 if bus == "x" else int(bus) for bus in lines[1].split(",")]

def find_first_earliest():
    time = earliest

    while True:
        for bus in buses:
            if bus == 0:
                continue
            
            if time % bus == 0:
                print((time - earliest) * bus)
                return

        time += 1

def lcm(a, b):
    return (a * b) // math.gcd(a, b)

def find_matching_time():
    bus_offsets = list(filter(lambda tup: tup[1] != 0, [(i, bus) for i, bus in enumerate(buses)]))
    increment = bus_offsets[0][1]
    
    found = 1
    time = increment

    while True:
        offset, bus = bus_offsets[found]
        
        if (time + offset) % bus == 0:
            found += 1

            if found == len(bus_offsets):
                print(time)
                return

            increment = lcm(increment, bus)

        time += increment

find_first_earliest()
find_matching_time()
