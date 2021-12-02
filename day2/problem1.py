valid = 0
with open('input.txt','r') as input:
    for line in input:
        temp = line.split(" ")
        min = int(temp[0].split("-")[0])
        max = int(temp[0].split("-")[1])
        char = temp[1][0]

        if (temp[2].count(char) >= min and temp[2].count(char) <= max):
            valid += 1

print(valid)
