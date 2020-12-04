import re

with open("input.txt") as file:
    lines = file.read().splitlines()

def parse_passports():
    passports = []
    current = {}

    for line in lines:
        if line == "":
            passports.append(current)
            current = {}
        else:
            for (key, value) in [section.split(":") for section in line.split(" ")]:
                current[key] = value

    passports.append(current)
    return passports

def count_present(passports):
    print(len(list(filter(lambda passport: is_present(passport), passports))))

def is_present(passport):
    return len(passport.keys()) == (8 if "cid" in passport.keys() else 7)

def count_valid(passports):
    print(len(list(filter(lambda passport: is_present(passport) and is_valid(passport), passports))))

def in_range(value, minimum, maximum):
    return minimum <= int(value) <= maximum

def is_valid(passport):
    if not in_range(passport["byr"], 1920, 2002):
        return False

    if not in_range(passport["iyr"], 2010, 2020):
        return False

    if not in_range(passport["eyr"], 2020, 2030):
        return False

    hgt = passport["hgt"]

    if hgt[-2:] == "cm":
        if not in_range(hgt[:-2], 150, 193):
            return False
    else:
        if not in_range(hgt[:-2], 59, 76):
            return False

    if re.match("#[0-9a-f]{6}", passport["hcl"]) == None:
        return False

    if not passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False

    return len(passport["pid"]) == 9

passports = parse_passports()

count_present(passports)
count_valid(passports)
