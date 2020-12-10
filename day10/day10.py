import functools

with open("input.txt") as file:
    lines = file.read().splitlines()

def find_joltage_distribution():
    i = 0

    ones = 0
    threes = 0

    while i != limit:
        if i + 1 in numbers or i + 1 == limit:
            i += 1
            ones += 1
        elif i + 3 in numbers or i + 3 == limit:
            i += 3
            threes += 1

    print(ones * threes)

@functools.lru_cache
def count_arrangements(i = 0):
    count = 0

    for delta in [1, 2, 3]:
        new = i + delta

        if new in numbers:
            count += count_arrangements(new)
        elif new == limit:
            count += 1

    return count

numbers = [int(line) for line in lines]
limit = max(numbers) + 3

find_joltage_distribution()
print(count_arrangements())
