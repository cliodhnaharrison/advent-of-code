f = open("aoc_inputs/aoc_3.txt", "r")

map = []

for l in f.read().split("\n")[:-1]:
    map.append(list(l))

def num_trees(dx, dy, map):
    x = y = 0
    finish_y = len(map) - 1
    trees = 0

    while y <= finish_y:
        if x > len(map[-1]) - 1:
            x -= len(map[-1])
        if map[y][x] == "#":
            trees += 1
        x += dx
        y += dy
    return trees

tests = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
result = 1
for t in tests:
    result *= num_trees(t[0], t[1], map)

print (result)
