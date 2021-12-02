pos = 0
hit = 0
with open("day3/input.txt","r") as input:
    for line in input.readlines()[1:]:
        pos = (pos + 3) % 31

        if line[pos] == "#":
            hit += 1
print(hit)