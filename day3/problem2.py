import math

pos = 0
hit = [0,0,0,0,0]
steps = [1,3,5,7]

lines = []

with open("day3/input.txt","r") as input:
    for line in input:
        lines.append(line.rstrip("\n"))

for i,step in enumerate(steps):
    pos = 0
    for line in lines[1:]:
        pos = (pos + step) % 31

        if line[pos] == "#":
            hit[i] += 1
pos = 0
for line in lines[2::2]:
    pos = (pos + 1) % 31

    if line[pos] == "#":
        hit[4] += 1

print(math.prod(hit))