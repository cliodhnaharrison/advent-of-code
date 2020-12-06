f = open("aoc_inputs/aoc_2.txt", "r")

passwords = []

for l in f.read().split("\n")[:-1]:
    p = l.split(" ")
    passwords.append([p[-1]] + [int(x) for x in p[0].split("-")] + [p[1].strip(":")])

count = 0
for x in passwords:
    c = x[0].count(x[-1])
    if c >= x[1] and c <= x[2]:
        count += 1

print (count)
