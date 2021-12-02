data = []
with open('input.txt', 'r') as input:
    for lines in input:
        data.append(int(lines.rstrip("\n")))

for i,v in enumerate(data):
    for v2 in data[i:]:
        if (v + v2 == 2020):
            print(v*v2)
