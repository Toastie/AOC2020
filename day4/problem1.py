valid = 0
fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
with open("day4/input.txt","r") as input:
    passports = input.read().split("\n\n")

for entry in passports:
    temp = entry.replace("\n"," ").split(" ")

    valid += 1

    if len(temp) != 8:
        for value in fields:
            if not entry.count(value):
                valid -= 1
                break

print(valid)
