from string import ascii_lowercase

f = open("aoc_6.txt", "r")

customs = []
curr = ""

for line in f.readlines():
    if line != "\n":
        curr += line.strip("\n")
    else:
        customs.append(curr)
        curr = ""
customs.append(curr)

count = 0

for x in customs:
    x = [y for y in list(set(x)) if y in ascii_lowercase]
    count += len(x)

print (count)
