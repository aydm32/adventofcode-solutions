"""Advent of Code 2025 day 7 part 1"""

with open("puzzle_input_1.txt") as file:
    lines = [line.strip() for line in file if line.strip()]

beams = set()                  
split = 0

for line in lines:
    new_beams = set()
    for col in beams:
        if line[col] == '^':   
            split += 1
            new_beams.add(col - 1)
            new_beams.add(col + 1)
        else:                  
            new_beams.add(col)
    if 'S' in line:         
        new_beams.add(line.index('S'))
    beams = new_beams

print(split)
