def split(word:str):
    return [char for char in word]

with open('day6/input.txt','r') as input:
    temp = input.read()

    groups = temp.split("\n\n")

groups = [str.replace("\n"," ") for str in groups]

groups = [str.split() for str in groups]


sum = 0

for group in groups:
    for question in group[0]:
        all = True
        for person in group[1:]:
            if not person.count(question):
                all = False
                break
        if all:
            sum += 1

print(sum)