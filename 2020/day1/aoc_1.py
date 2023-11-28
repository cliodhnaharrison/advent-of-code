f = open("aoc_1.txt", "r")
expenses = [int(x) for x in f.read().split('\n')[:-1]]

for i in range(len(expenses)):
    x = expenses[i]
    tmp = expenses[:i] + expenses[i+1:]
    for y in tmp:
        if (x + y) == 2020:
            print (x * y)
            break
