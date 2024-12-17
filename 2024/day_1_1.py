f = open("day_1_1.txt", "r")
left = []
right = []

for line in f.readlines():
    l, r = map(int, line.split())
    left.append(l)
    right.append(r)

left = sorted(left)
right = sorted(right)
total_distance = 0

for x, y in zip(left, right):
    total_distance += abs(x - y)

print(total_distance)

f.close()