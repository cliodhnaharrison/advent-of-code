f = open("day1.txt", "r")
elves = []
batch = []
for line in f.readlines():
    if line == "\n":
      elves.append(sum(batch))
      batch = []
    else:
      batch.append(int(line.strip("\n")))

# print (max(elves))

# Day 1 Part 2
print (sum(sorted(elves, reverse=True)[0:3]))
