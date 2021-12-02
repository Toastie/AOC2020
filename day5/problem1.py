import math


def rowOfPass(part:str,row:list):
    if len(part) == 1:
        if part[0] == "B":
            return row[1]
        else:
            return row[0]

    if part[0] == "B":
        return rowOfPass(part[1:],row[int(len(row)/2):])
    else:
        return rowOfPass(part[1:],row[:-int((len(row)/2))])

def columnOfPass(part:str,col:list):
    if len(part) == 1:
        if part[0] == "L":
            return col[0]
        else:
            return col[1]

    if part[0] == "R":
        return columnOfPass(part[1:],col[int(len(col)/2):])
    else:
        return columnOfPass(part[1:],col[:-int(len(col)/2)])

with open('day5/input.txt','r') as input:
    ids = []
    for lines in input:
        lines = lines.rstrip("\n")
        ids.append((rowOfPass(lines[:7],list(range(128))) * 8) + columnOfPass(lines[-3:],list(range(8))))

print(max(ids))
