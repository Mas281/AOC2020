with open("input.txt") as file:
    lines = file.read().splitlines()

def parse_line(line):
    split = line.split(" ")
    return [split[0], int(split[1])]

def last_acc_value():
    done = []
    
    accumulator = 0
    i = 0

    while True:
        if i >= len(instructions):
            return True, accumulator
        
        if i in done:
            return False, accumulator
        
        done.append(i)
        opcode, operand = instructions[i]

        if opcode == "acc":
            accumulator += operand

        i += operand if opcode == "jmp" else 1

def find_terminating_acc_value():
    for (i, (opcode, _)) in enumerate(instructions):
        if opcode == "jmp":
            instructions[i][0] = "nop"
        elif opcode == "nop":
            instructions[i][0] = "jmp"
        else:
            continue
            
        terminates, last_acc = last_acc_value()

        if terminates:
            print(last_acc)
            return

        instructions[i][0] = opcode

instructions = [parse_line(line) for line in lines]

print(last_acc_value()[1])
find_terminating_acc_value()
