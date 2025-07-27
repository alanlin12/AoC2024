infile = open('input.txt', 'r')
maxdist = 0
similarity = 0
value1 = []
value2 = []
with infile as f:
    for line in f:
        value1.append(line.split()[0])
        value2.append(line.split()[1])
value2 = sorted(value2)
for i, val1 in enumerate(sorted(value1)):
    val1 = int(val1)
    val2 = int(value2[i])
    maxdist += max(val1, val2) - min(val1, val2)
    similarity += (val1 * int(value2.count(str(val1))))

print(maxdist)
print(similarity)
