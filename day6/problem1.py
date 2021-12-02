def split(word:str):
    return [char for char in word]

with open('day6/input.txt','r') as input:
    temp = input.read()

    groups = temp.split("\n\n")

groups = [str.replace("\n","") for str in groups]

sets = [set((split(group))) for group in groups]

sum = 0
for set in sets:
    sum += len(set)

print(sum)