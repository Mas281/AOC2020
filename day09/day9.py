with open("input.txt") as file:
    lines = file.read().splitlines()

preamble_length = 25
numbers = [int(line) for line in lines]

def is_sum_of_previous(wanted, start, end):
    for num1 in numbers[start:end]:
        for num2 in numbers[start + 1:end]:
            if num1 + num2 == wanted:
                return True

    return False

def find_invalid_number():
    for i in range(preamble_length, len(numbers)):
        number = numbers[i]
        
        if not is_sum_of_previous(number, i - preamble_length, i):
            return number

def is_sum_of_n_contiguous(n, wanted):
    for i in range(len(numbers) - (n - 1)):
        sublist = numbers[i:i + n]

        if sum(sublist) == wanted:            
            return True, min(sublist) + max(sublist)

    return False, 0

def find_sum_to_invalid(invalid):
    n = 2

    while True:
        found, min_plus_max = is_sum_of_n_contiguous(n, invalid)

        if found:
            print(min_plus_max)
            return

        n += 1

invalid = find_invalid_number()
print(invalid)
find_sum_to_invalid(invalid)
