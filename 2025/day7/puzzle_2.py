"""Advent of Code 2025 day 7 part 2"""

with open("puzzle_input_1.txt") as file:
    lines = [line.strip() for line in file if line.strip()]

beams = {}                      

for line in lines:
    new_beams = {}
    for col in beams:
        n = beams[col]          
        if line[col] == '^':   
            new_beams[col - 1] = new_beams.get(col - 1, 0) + n
            new_beams[col + 1] = new_beams.get(col + 1, 0) + n
        else:                  
            new_beams[col] = new_beams.get(col, 0) + n
    if 'S' in line:            
        c = line.index('S')
        new_beams[c] = new_beams.get(c, 0) + 1
    beams = new_beams

total = 0
for col in beams:
    total += beams[col]
print(total)                   
