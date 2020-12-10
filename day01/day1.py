with open("input.txt") as file:
    lines = file.read().splitlines()

numbers = [int(line) for line in lines]

def find_two_sum(numbers):
    for num1 in numbers:
        for num2 in numbers:
            if num1 + num2 == 2020:
                print(num1 * num2)
                return

def find_three_sum(numbers):
    for num1 in numbers:
        for num2 in numbers:
            for num3 in numbers:
                if num1 + num2 + num3 == 2020:
                    print(num1 * num2 * num3)
                    return

find_two_sum(numbers)
find_three_sum(numbers)
