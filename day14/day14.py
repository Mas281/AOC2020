with open("input.txt") as file:
    lines = file.read().splitlines()

def find_memory_sum(mask_function):
    memory = {}

    for line in lines:
        split = line.split(" = ")

        if "mask" in line:
            mask = split[1]
        else:
            address = int(split[0].split("[")[1].split("]")[0])
            value = split[1]

            mask_function(memory, address, mask, value)
        
    print(sum(memory.values()))

def to_binary(value):
    return bin(int(value))[2:].zfill(36)

def mask_function_v1(memory, address, mask, value):
    value = to_binary(value)
    
    result = "".join([value[i] if mask[i] == "X" else mask[i] for i in range(36)])
    memory[address] = int(result, 2)

def mask_function_v2(memory, address, mask, value):
    address = to_binary(address)
    addresses = [""]

    for i in range(36):
        if mask[i] == "0":
            addresses = [addr + address[i] for addr in addresses]
        elif mask[i] == "1":
            addresses = [addr + "1" for addr in addresses]
        else:
            new = []

            for addr in addresses:
                new.append(addr + "0")
                new.append(addr + "1")

            addresses = new

    for addr in addresses:
        memory[addr] = int(value)
    
find_memory_sum(mask_function_v1)
find_memory_sum(mask_function_v2)
