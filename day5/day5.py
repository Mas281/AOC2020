with open("input.txt") as file:
    lines = file.read().splitlines()

def find_max_id():
    print(max([seat_id(seat) for seat in lines]))

def interpret_binary(string, zero, one):
    return int(string.replace(zero, "0").replace(one, "1"), 2)

def seat_id(seat):
    row = interpret_binary(seat[:7], "F", "B")
    column = interpret_binary(seat[7:], "L", "R")

    return 8 * row + column

def find_missing_id():
    ids = sorted([seat_id(seat) for seat in lines])

    for i, sid in enumerate(ids):
        if ids[i+1] != sid + 1:
            print(sid + 1)
            return

find_max_id()
find_missing_id()
