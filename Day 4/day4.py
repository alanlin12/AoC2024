instances = 0
pattern = ["MAS", "SAM"]

def check_pattern(grid, r, c):
    if r < 1 or r >= len(grid) - 1 or c < 1 or c >= len(grid[0]) - 1: return False
    
    dia1 = grid[r-1][c-1] + grid[r][c] + grid[r+1][c+1]
    dia2 = grid[r-1][c+1] + grid[r][c] + grid[r+1][c-1]
    
    if(dia1 in pattern and dia2 in pattern): return True
    return False

with open('input.txt', 'r') as file:
    grid = [list(x) for x in file.read().splitlines()]
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "A":
                if check_pattern(grid, r, c): 
                    instances += 1
                
print(instances)