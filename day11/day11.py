with open("input.txt") as file:
    lines = file.read().splitlines()

rows = len(lines)
columns = len(lines[0])

empty = "L"
occupied = "#"

def print_grid(grid):
    for row in grid:
        print(row)

def get_grid(grid, row, column):
    if 0 <= row < rows and 0 <= column < columns:
        return grid[row][column]
    return ""

def count_adj_occupied(grid, row, column):
    count = 0

    for dr in range(-1, 2):
        for dc in range(-1, 2):
            if dr == 0 and dc == 0:
                continue
            
            if get_grid(grid, row + dr, column + dc) == occupied:
                count += 1

    return count

def count_vis_occupied(grid, row, column):
    count = 0

    for dr in range(-1, 2):
        for dc in range(-1, 2):
            if dr == 0 and dc == 0:
                continue
            
            for i in range(1, max(rows - row, columns - column) + 1):
                status = get_grid(grid, row + dr * i, column + dc * i)
                
                if status == occupied:
                    count += 1
                    break
                if status == empty or status == "":
                    break
                
    return count

def string_replace(string, char, position):
    return string[:position] + char + string[position + 1:]
            
def simulate_iteration_adj(grid):
    new = grid.copy()
    changes = 0

    for row in range(rows):
        for column in range(columns):
            status = get_grid(grid, row, column)

            if status == empty and count_adj_occupied(grid, row, column) == 0:
                new[row] = string_replace(new[row], occupied, column)
                changes += 1
            elif status == occupied and count_adj_occupied(grid, row, column) >= 4:
                new[row] = string_replace(new[row], empty, column)
                changes += 1

    return new, changes

def simulate_iteration_visible(grid):
    new = grid.copy()
    changes = 0

    for row in range(rows):
        for column in range(columns):
            status = get_grid(grid, row, column)

            if status == empty and count_vis_occupied(grid, row, column) == 0:
                new[row] = string_replace(new[row], occupied, column)
                changes += 1
            elif status == occupied and count_vis_occupied(grid, row, column) >= 5:
                new[row] = string_replace(new[row], empty, column)
                changes += 1

    return new, changes

def count_occupied(grid):
    return len(list(filter(lambda char: char == occupied, "".join(grid))))

def simulate_seats(grid, simulation_function):
    while True:
        grid, changes = simulation_function(grid)

        if changes == 0:
            print(count_occupied(grid))
            break

simulate_seats(lines, simulate_iteration_adj)
simulate_seats(lines, simulate_iteration_visible)
