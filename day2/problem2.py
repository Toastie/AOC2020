valid = 0
with open('input.txt','r') as input:
    for line in input:
        temp = line.split(" ")
        first = int(temp[0].split("-")[0])
        second = int(temp[0].split("-")[1])
        char = temp[1][0]

        if ((temp[2][first - 1] == char) ^ (temp[2][second - 1] == char)):
            valid += 1

print(valid)