def check_Safe(levels):
    safe = True
    increasing = False
    decreasing = False
    
    for i in range(len(levels)-1):
        diff = levels[i] - levels[i + 1]
        if abs(diff) < 1 or abs(diff) > 3:
            return False

        if diff > 0: increasing = True
        elif diff < 0: decreasing = True
        
        if increasing and decreasing:
            safe = False
        
    return safe

def check_Dampened(levels):
    if(check_Safe(levels)): return True
    
    for i in range(len(levels)):
        new_levels = levels[:i] + levels[i+1:]
        if(check_Safe(new_levels)): return True
    return False

ans = 0

with open('input.txt', 'r') as file:
    for line in file:
        line = [int(x) for x in line.split()]
        if(check_Dampened(line)): ans += 1
    

print(ans)