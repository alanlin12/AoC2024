import re

ans = 0
pattern = r"(mul\(([0-9]{1,3}),([0-9]{1,3})\)|do\(\)|don't\(\))"
enabled = True

with open('input.txt', 'r') as file:
    content = file.read()
    matches = re.finditer(pattern, content)
    
    for match in matches:
        request = match.group(1)
        if request == "do()": 
            enabled = True
        elif request == "don't()": 
            enabled = False
            
        elif request.startswith("mul(") and enabled:
            num1 = match.group(2)
            num2 = match.group(3)
            ans += int(num1) * int(num2)

print(ans)