f = open("aoc_inputs/aoc_3.txt", "r")

map = []

for l in f.read().split("\n")[:-1]:
    map.append(list(l))

x = y = 0
finish_y = len(map) - 1
trees = 0

while y <= finish_y:
    if x > len(map[-1]) - 1:
        x -= len(map[-1])
    if map[y][x] == "#":
        trees += 1
        map[y][x] = "X"
    else:
        map[y][x] = "O"
    x += 3
    y += 1

#for x in map:
    #print (x)
print (trees)
