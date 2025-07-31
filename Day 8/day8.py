with open("input.txt", "r") as file:
    grid = [x.strip() for x in file.read().splitlines()]
    row, col = len(grid), len(grid[0])
    antennas = {}
    
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char != ".":
                if char not in antennas: antennas[char] = []
                antennas[char].append((i, j))
    
    antinodes = set()
    
    for ant, positions in antennas.items():
        if(len(positions) < 2): break
        for i in range(len(positions)):
            for j in range(len(positions)):
                if i == j: continue
                r1, c1 = positions[i]
                r2, c2 = positions[j]
                dr, dc = r2 - r1, c2 - c1
                r, c = r1, c1
                while(0 <= r < col and 0 <= c < col):
                    antinodes.add((r, c))
                    r += dr
                    c += dc
    
    print(len([x for x in antinodes]))