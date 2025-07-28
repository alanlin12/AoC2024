def check_valid(sequencing, counter):
    for i in range(len(sequencing)):
        for j in range(i + 1, len(sequencing)):
            if (sequencing[i], sequencing[j]) in graph:
                if graph[(sequencing[i], sequencing[j])] == -1:
                    temp = sequencing[i]
                    sequencing[i] = sequencing[j]
                    sequencing[j] = temp
                    counter += 1
                    check_valid(sequencing, counter)
    if(counter > 0): return True
    return False

with open("sequence.txt", "r") as sequence, open("updates.txt", "r") as updates:
    rules = updates.readlines()
    lines = sequence.readlines()
    
    sum = 0
    
    incorrect_pairs = []
    correct_pairs = []
    ordering = []
    for line in rules:
        ordering.append(list(line.strip().split("|")))
    
    graph = {}
    for x, y in ordering:
        graph[(x, y)] = 1
        graph[(y, x)] = -1
        
    for line in lines:
        sequencing = list(line.strip().split(","))
        if check_valid(sequencing, 0):
            correct_pairs.append(sequencing)
            
    for i in range(len(correct_pairs)):
        sum += int(correct_pairs[i][len(correct_pairs[i]) // 2])
    
    print(sum)
            