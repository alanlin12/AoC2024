
def check_in_bounds(grid, row, col):
    if row < 0 or row > len(grid) - 1 or col < 0 or col > len(grid[0]) - 1:
        return False
    return True

def simulate_guard(grid, row, col):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction_index = 0
    visited = set()

    while True:
        dr, dc = directions[direction_index]
        
        state = (row, col, direction_index)
        if state in visited: return True
        visited.add(state)
        
        if not check_in_bounds(grid, row + dr, col + dc):
            return False
        
        if grid[row + dr][col + dc] == "#":
            direction_index = (direction_index + 1) % 4
        else:
            row = row + dr
            col = col + dc
    
with open("input.txt", "r") as file:
    positions = 0
    grid = [list(x) for x in file.read().splitlines()]
    starting_r, starting_c = 0, 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "^":
                starting_r = row
                starting_c = col
                break
    for cr in range(len(grid)):
        for cc in range(len(grid[0])):
            if grid[cr][cc] != ".":
                continue
            grid[cr][cc] = "#"
            if simulate_guard(grid, starting_r, starting_c):
                positions += 1
            grid[cr][cc] = "."
    print(positions)