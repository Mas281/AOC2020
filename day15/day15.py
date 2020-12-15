numbers = [1, 17, 0, 10, 18, 11, 6]

def find_nth_number(n):
    indexes = {n: i for i, n in enumerate(numbers[:-1])}
    last = numbers[-1]

    for i in range(len(numbers), n):
        if last in indexes:
            new = (i - 1) - indexes[last]
        else:
            new = 0
            
        indexes[last] = i - 1
        last = new

    print(last)

find_nth_number(2020)
find_nth_number(30000000)
