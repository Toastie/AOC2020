data = []
with open('input.txt', 'r') as input:
    for lines in input:
        data.append(int(lines.rstrip("\n")))

#this is O(n^3), sooo not good
for v in data:
    for v2 in data:
        for v3 in data:
            if (v + v2 + v3 == 2020):
                print(v,v2,v3)
                print(v * v2 * v3)
