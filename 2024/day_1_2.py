from collections import defaultdict

f = open("day_1_1.txt", "r")
left_count = defaultdict(int)
right_count = defaultdict(int)

for line in f.readlines():
    l, r = map(int, line.split())
    left_count[l] += 1
    right_count[r] += 1

similarity = 0

for i in range(1, max(max(left_count.keys()), max(right_count.keys())) + 1):
    similarity += left_count[i] * i * right_count[i]

print(similarity)
f.close()