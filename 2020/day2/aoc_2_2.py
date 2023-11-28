f = open("aoc_2.txt", "r")

passwords = []

for l in f.read().split("\n")[:-1]:
    p = l.split(" ")
    passwords.append([p[-1]] + [int(x) - 1 for x in p[0].split("-")] + [p[1].strip(":")])

count = 0
for x in passwords:
    first = second = False
    password = x[0]
    letter = x[-1]
    if len(password) > x[1]:
        if password[x[1]]  == letter:
            first = True

    if len(password) > x[2]:
        if password[x[2]] == letter:
            second = True

    if first and second:
        continue
    elif first or second:
        count += 1

print (count)
