valid = 0
with open("day4/input.txt","r") as input:
    passports = input.read().split("\n\n")

for entry in passports:
    temp = entry.replace("\n"," ").split(" ")

    if len(temp) == 8 or (len(temp) == 7 and not entry.count("cid")):
        valid += 1

print(valid)