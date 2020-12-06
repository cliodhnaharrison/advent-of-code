from string import ascii_lowercase

f = open("aoc_6.txt", "r")

customs = []
curr = []

for line in f.readlines():
    if line != "\n":
        curr.append(line.strip("\n"))
    else:
        customs.append(curr)
        curr = []
customs.append(curr)

count = 0

for x in customs:
    if x:
        x = [set(y) for y in x]
        u = set.intersection(*x)
        count += len(u)

print (count)
